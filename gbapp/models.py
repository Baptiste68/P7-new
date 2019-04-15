from flask_sqlalchemy import SQLAlchemy
import logging as lg
import os
import re
import json
import requests

from config import API_WIKI

# from .views import app

# Create database connection object



class Question:

    def __init__(self, textquestion):
        my_useless_words = ['adresse', 'lieu', 'endroit', 'rue', 'avenue', 'av', 'place', 'coordonnées', 'ville', 'qui', 'quoi', 'quand', 'dis', 'salut', 'hello', 'bonjour', 'coucou']
       
        self.my_word_list = my_useless_words
        self.text_to_analyse = textquestion

        self.text_to_analyse_parsed = self.parse_my_question()


    def parse_my_question(self):
        """
            Function used to take out the usefull word of the question.
        """
        # Open the json file with many useless words    
        try:
            with open(os.path.dirname(os.path.abspath(__file__)) + '/word_list.json') as f:
                useless_word_list = json.load(f)
        except IOError as err:
            print('Error loading word file : ' + str(err))
            useless_word_list = "error"
        
        # Adding some custom words in the list
        useless_word_list.extend(self.my_word_list)

        # Remove all punctuation and change the text in lowercase with a regex
        string_without_punctuation = re.sub(r"[-,.;@#?!&$'()<>/]+ *", " ", self.text_to_analyse.lower(), )

        words_to_parse = string_without_punctuation.split()
        final_list = []

        # Go through the words in the question and check if useful or not
        for word in words_to_parse:
            if word not in useless_word_list:
                final_list.append(word)
        final_list_paresed = ' '.join(final_list)

        return final_list_paresed

    def wiki_info(self):

        my_search_term = self.text_to_analyse_parsed
        payload = {'gsrsearch': my_search_term,}
        payload.update(**API_WIKI['PARAM'])

        result = requests.get(API_WIKI['ROOT_URL'], params=payload)
        self.wiki_json = json.loads(result.text)

        try:
            article_id = self.wiki_json ['query']['pageids'][0]
            wiki_article_intro = self.wiki_json['query']['pages'][article_id]['extract']
            wiki_link = 'http://fr.wikipedia.org/?curid='+article_id
            wiki_article_intro = wiki_article_intro + ' <a href="' + \
                                 wiki_link + '" target="_blank">En savoir plus sur wikipédia.</a>'

        except KeyError:
           # TODO wiki_article_intro = self.wiki_response_html
           wiki_article_intro = "oupsy"

        return wiki_article_intro
