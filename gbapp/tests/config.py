import os


SECRET_KEY = "#d#JCqTTW\nilK\\7m\x0bp#\tj~#H"
basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

MAPS_KEY = "AIzaSyBWGDqVszmpzIc9jxeUMZbJc3lQuQZPC-k"

# Active le debogueur
DEBUG = True
TESTING = True
LIVESERVER_PORT = 8943
LIVESERVER_TIMEOUT = 10

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

API_WIKI = {
    'ROOT_URL' : 'https://fr.wikipedia.org/w/api.php',

    'PARAM' : {
        'action': 'query',
        'prop': 'extracts',
        'exintro': 1,
        'explaintext': 1,
        'format': 'json',
        'indexpageids': 1,
        'exsentences': 5,
        'generator': 'search',
        'gsrlimit': 1,
    }
    
}

ERROR_MSG = {
    'PARSED_FAILED' : 'Je ne suis pas parvenu a parser votre question à cause de:',

    'NOTHING_FOUND_WIKI' : 'Oups, je ne connais rien sur ce sujet',

    'NOTHING_FOUND_MAP' : 'Oups, je ne parviens pas à trouver la localisation',

    'CONNECTION_FAILED_WIKI' : 'Aie, je n\'ai pas pu me connecter sur Wikipedia...',
    
    'CONNECTION_FAILED_MAPS' : 'Aie, je n\'ai pas pu me connecter sur Google Maps...'
}


API_MAPS = {
    'ADDR_URL': 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json',

    'PARAM': {
        'key': MAPS_KEY,
        'inputtype': 'textquery',
        'language': 'fr',
        'type': 'street_address',
        'fields': 'formatted_address,geometry'
    }
    
}