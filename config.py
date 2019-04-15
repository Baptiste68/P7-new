import os

# To generate a new secret key:
# >>> import random, string
# >>> "".join([random.choice(string.printable) for _ in range(24)])
SECRET_KEY = "#d#JCqTTW\nilK\\7m\x0bp#\tj~#H"
basedir = os.path.abspath(os.path.dirname(__file__))
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

