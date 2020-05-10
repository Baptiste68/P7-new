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
        """
        try:
            with open(os.path.dirname(os.path.abspath(__file__)) +
                      '/word_list.json') as f:
                useless_word_list = json.load(f)
        except IOError as err:
            final_list_paresed = ERROR_MSG['PARSED_FAILED'] + str(err)
        """
        useless_word_list = ["a","abord","absolument","afin","ah","ai","aie","ailleurs","ainsi","ait","allaient","allo","allons","allô","alors","anterieur","anterieure","anterieures","apres","après","as","assez","attendu","au","aucun","aucune","aujourd","aujourd'hui","aupres","auquel","aura","auraient","aurait","auront","aussi","autre","autrefois","autrement","autres","autrui","aux","auxquelles","auxquels","avaient","avais","avait","avant","avec","avoir","avons","ayant","b","bah","bas","basee","bat","beau","beaucoup","bien","bigre","boum","bravo","brrr","c","car","ce","ceci","cela","celle","celle-ci","celle-là","celles","celles-ci","celles-là","celui","celui-ci","celui-là","cent","cependant","certain","certaine","certaines","certains","certes","ces","cet","cette","ceux","ceux-ci","ceux-là","chacun","chacune","chaque","cher","chers","chez","chiche","chut","chère","chères","ci","cinq","cinquantaine","cinquante","cinquantième","cinquième","clac","clic","combien","comme","comment","comparable","comparables","compris","concernant","contre","couic","crac","d","da","dans","de","debout","dedans","dehors","deja","delà","depuis","dernier","derniere","derriere","derrière","des","desormais","desquelles","desquels","dessous","dessus","deux","deuxième","deuxièmement","devant","devers","devra","different","differentes","differents","différent","différente","différentes","différents","dire","directe","directement","dit","dite","dits","divers","diverse","diverses","dix","dix-huit","dix-neuf","dix-sept","dixième","doit","doivent","donc","dont","douze","douzième","dring","du","duquel","durant","dès","désormais","e","effet","egale","egalement","egales","eh","elle","elle-même","elles","elles-mêmes","en","encore","enfin","entre","envers","environ","es","est","et","etant","etc","etre","eu","euh","eux","eux-mêmes","exactement","excepté","extenso","exterieur","f","fais","faisaient","faisant","fait","façon","feront","fi","flac","floc","font","g","gens","h","ha","hein","hem","hep","hi","ho","holà","hop","hormis","hors","hou","houp","hue","hui","huit","huitième","hum","hurrah","hé","hélas","i","il","ils","importe","j","je","jusqu","jusque","juste","k","l","la","laisser","laquelle","las","le","lequel","les","lesquelles","lesquels","leur","leurs","longtemps","lors","lorsque","lui","lui-meme","lui-même","là","lès","m","ma","maint","maintenant","mais","malgre","malgré","maximale","me","meme","memes","merci","mes","mien","mienne","miennes","miens","mille","mince","minimale","moi","moi-meme","moi-même","moindres","moins","mon","moyennant","multiple","multiples","même","mêmes","n","na","naturel","naturelle","naturelles","ne","neanmoins","necessaire","necessairement","neuf","neuvième","ni","nombreuses","nombreux","non","nos","notamment","notre","nous","nous-mêmes","nouveau","nul","néanmoins","nôtre","nôtres","o","oh","ohé","ollé","olé","on","ont","onze","onzième","ore","ou","ouf","ouias","oust","ouste","outre","ouvert","ouverte","ouverts","o|","où","p","paf","pan","par","parce","parfois","parle","parlent","parler","parmi","parseme","partant","particulier","particulière","particulièrement","pas","passé","pendant","pense","permet","personne","peu","peut","peuvent","peux","pff","pfft","pfut","pif","pire","plein","plouf","plus","plusieurs","plutôt","possessif","possessifs","possible","possibles","pouah","pour","pourquoi","pourrais","pourrait","pouvait","prealable","precisement","premier","première","premièrement","pres","probable","probante","procedant","proche","près","psitt","pu","puis","puisque","pur","pure","q","qu","quand","quant","quant-à-soi","quanta","quarante","quatorze","quatre","quatre-vingt","quatrième","quatrièmement","que","quel","quelconque","quelle","quelles","quelqu'un","quelque","quelques","quels","qui","quiconque","quinze","quoi","quoique","r","rare","rarement","rares","relative","relativement","remarquable","rend","rendre","restant","reste","restent","restrictif","retour","revoici","revoilà","rien","s","sa","sacrebleu","sait","sans","sapristi","sauf","se","sein","seize","selon","semblable","semblaient","semble","semblent","sent","sept","septième","sera","seraient","serait","seront","ses","seul","seule","seulement","si","sien","sienne","siennes","siens","sinon","six","sixième","soi","soi-même","soit","soixante","son","sont","sous","souvent","specifique","specifiques","speculatif","stop","strictement","subtiles","suffisant","suffisante","suffit","suis","suit","suivant","suivante","suivantes","suivants","suivre","superpose","sur","surtout","t","ta","tac","tant","tardive","te","tel","telle","tellement","telles","tels","tenant","tend","tenir","tente","tes","tic","tien","tienne","tiennes","tiens","toc","toi","toi-même","ton","touchant","toujours","tous","tout","toute","toutefois","toutes","treize","trente","tres","trois","troisième","troisièmement","trop","très","tsoin","tsouin","tu","té","u","un","une","unes","uniformement","unique","uniques","uns","v","va","vais","vas","vers","via","vif","vifs","vingt","vivat","vive","vives","vlan","voici","voilà","vont","vos","votre","vous","vous-mêmes","vu","vé","vôtre","vôtres","w","x","y","z","zut","à","â","ça","ès","étaient","étais","était","étant","été","être","ô"]
        if useless_word_list == "":
            useless_word_list = "0"
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
            wiki_article = wiki_article + " votre question parser retourne "+\
                " une chaine vide"

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

        """
        my_search_term = self.parse_my_question()
        payload = {'input': my_search_term, }
        payload.update(**API_MAPS['PARAM'])
        """
        my_search_term = self.parse_my_question()
        unformated_term = self.parse_my_question()
        my_search_term=my_search_term.replace(" ", "+")
        print("//////////////////////////////////")
        print(my_search_term)
        # print(payload)
        # Try to request info from the API
        try:
            url = API_MAPS['ADDR_URL']+my_search_term+"&format=json"
            result = requests.get(url)
            maps_json = json.loads(result.text)
            """
            result = requests.get(API_MAPS['ADDR_URL'], params=payload)
            maps_json = json.loads(result.text)
            """

        # If not, set the error message for connection issues
        except requests.ConnectionError as co_err:
            maps_fail = ERROR_MSG['CONNECTION_FAILED_MAPS']
            maps_fail = maps_fail + "  // LA RAISON EST:  //   "
            maps_fail = maps_fail + repr(co_err.args[0].reason)
            print(repr(co_err.args[0].reason))

        else:
            # We try to receive information on an articale
            maps_addr = maps_json
            print(maps_addr)
            #self.coord = maps_json[0]['lat']
            try:
                maps_addr = maps_json[0]['display_name']
                print(maps_addr)
                maps_lat = maps_json[0]['lat']
                maps_lon = maps_json[0]['lon']
                self.coord = {'lat': float(maps_lat), 'lng': float(maps_lon)}
                """
                maps_addr = maps_json['candidates'][0]['formatted_address']
                print(maps_addr)
                self.coord = maps_json['candidates'][0]['geometry']['location']
                """

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
                        maps_json == []
                        #useless_va = maps_json['status']
                        maps_fail = maps_fail + " Aucune correspondance pour " + unformated_term + ". Vérifiez l'orthographe"

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
