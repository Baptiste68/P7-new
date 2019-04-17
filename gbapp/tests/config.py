import os

# To generate a new secret key:
# >>> import random, string
# >>> "".join([random.choice(string.printable) for _ in range(24)])
SECRET_KEY = "#d#JCqTTW\nilK\\7m\x0bp#\tj~#H"
basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

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

    'NOTHING_FOUND' : 'Oups, je ne connais rien sur ce sujet',

    'CONNECTION_FAILED' : 'Aie, je n\'ai pas pu me connecter...'
}