from flask_sqlalchemy import SQLAlchemy
import logging as lg
import os
import re
import json
import requests

from config import API_WIKI, ERROR_MSG, API_MAPS, SUCESS_GOOGLE, SUCESS_WIKI,\
    ERROR_BLA

# from .views import app


class Question:
    """
        Class to manage the question and answers
    """

    def __init__(self, textquestion):
        """
            This function is used to initiate a question with a text and list \
                of word
        """
        my_useless_words = ['adresse', 'lieu', 'endroit', 'rue', 'avenue',
                            'av', 'place', 'coordonnées', 'ville',
                            'qui', 'quoi', 'quand', 'dis', 'salut', 'hello',
                            'bonjour', 'coucou', 'grandpy', 'papy', 'connais']

        self.my_word_list = my_useless_words
        self.text_to_analyse = textquestion
        self.link_wiki = ""
        self.coord = ""

    def parse_my_question(self):
        """
            Function used to take out the usefull word of the question.
        """
        # Open the json file with many useless words
        try:
            with open(os.path.dirname(os.path.abspath(__file__)) +
                      '/word_list.json') as f:
                useless_word_list = json.load(f)
        except IOError as err:
            final_list_paresed = ERROR_MSG['PARSED_FAILED'] + str(err)

        else:
            # Adding some custom words in the list
            useless_word_list.extend(self.my_word_list)

            # Remove all punctuation and
            # change the text in lowercase with a regex
            string_without_punctuation = re.sub(
                r"[-,.;@#?!&$'()<>/:]+ *", " ", self.text_to_analyse.lower(), )

            words_to_parse = string_without_punctuation.split()
            final_list = []

            # Go through the words in the question and check if useful or not
            for word in words_to_parse:
                if word not in useless_word_list:
                    final_list.append(word)
            final_list_paresed = ' '.join(final_list)

        return final_list_paresed

    def wiki_info(self):
        """
            Function that check Wikipedia info
        """
        my_search_term = self.parse_my_question()
        payload = {'gsrsearch': my_search_term, }
        payload.update(**API_WIKI['PARAM'])

        print(my_search_term)

        if my_search_term == "":
            wiki_article = ERROR_MSG['NOTHING_FOUND_WIKI']
            wiki_article = wiki_article + " votre question parser retourne une\
                chaine vide"

        else:
            # We try to connect using the CONFIG PARAM and the text parsed
            try:
                result = requests.get(API_WIKI['ROOT_URL'], params=payload)
                self.wiki_json = json.loads(result.text)
                print(self.wiki_json)

            # If failed, send connection error message
            except requests.ConnectionError as co_err:
                wiki_article = ERROR_MSG['CONNECTION_FAILED_WIKI']
                wiki_article = wiki_article + "  // LA RAISON EST:  //"
                wiki_article = wiki_article + repr(co_err.args[0].reason)
                print(repr(co_err.args[0].reason))

            else:
                # We try to receive information on an articale
                try:
                    article_id = self.wiki_json['query']['pageids'][0]
                    wiki_article = self.wiki_json['query']['pages'][article_id]\
                        ['extract']
                    self.link_wiki = 'https://fr.wikipedia.org/?curid='+\
                        article_id

                # If faileed we show an error message
                except Exception as e:
                    wiki_article = ERROR_MSG['NOTHING_FOUND_WIKI']
                    wiki_article = wiki_article + "  // LA RAISON EST:  //   "
                    wiki_article = wiki_article + repr(e)
                    print(repr(e))
                    pass

        # Return the result
        return wiki_article

    def get_link_wiki(self):
        return self.link_wiki

    def maps_info(self):
        """
            Function that check maps info
        """
        # Variable for issues
        maps_fail = ""

        maps_addr = ""

        my_search_term = self.parse_my_question()
        payload = {'input': my_search_term, }
        payload.update(**API_MAPS['PARAM'])

        print(payload)
        # Try to request info from the API
        try:
            result = requests.get(API_MAPS['ADDR_URL'], params=payload)
            maps_json = json.loads(result.text)

        # If not, set the error message for connection issues
        except requests.ConnectionError as co_err:
            maps_fail = ERROR_MSG['CONNECTION_FAILED_MAPS']
            maps_fail = maps_fail + "  // LA RAISON EST:  //   "
            maps_fail = maps_fail + repr(co_err.args[0].reason)
            print(repr(co_err.args[0].reason))

        else:
            # We try to receive information on an articale
            try:
                maps_addr = maps_json['candidates'][0]['formatted_address']
                print(maps_addr)
                self.coord = maps_json['candidates'][0]['geometry']['location']

            # If failed we show an error message
            except KeyError as e:
                maps_fail = ERROR_MSG['NOTHING_FOUND_MAP']
                maps_fail = maps_fail + "  // LA RAISON EST:  //   " + repr(e)
                pass

            except IndexError as e:
                maps_fail = ERROR_MSG['NOTHING_FOUND_MAP']
                maps_fail = maps_fail + "  // LA RAISON EST:  //   "
                pass

                # Checking if Quota is exceed
                try:
                    maps_fail = maps_fail + maps_json['error_message']

                # Otherwise, print error
                except:
                    try:
                        useless_va = maps_json['status']
                        maps_fail = maps_fail + " Aucune correspondance pour "
                        + my_search_term

                    except:
                        maps_fail = maps_fail + repr(e)
                        print(repr(e))
                        pass

        if maps_fail == "":
            return maps_addr
        else:
            return maps_fail

    def get_coord(self):
        return self.coord

    def blabla_sentence(self, type, nb):
        if type == "maps_true":
            return SUCESS_GOOGLE[nb]
        if type == "wiki_true":
            return SUCESS_WIKI[nb]
        if type == "error":
            return ERROR_BLA[nb]
