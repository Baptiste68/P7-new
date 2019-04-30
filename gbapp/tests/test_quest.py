import pytest
import os
import sys
import requests
import json
import urllib.request
import json
from io import BytesIO
from gbapp import models as script
from config import API_WIKI, ERROR_MSG, API_MAPS
# sys.path.append("..")
# import models as script


"""
def create_app(self):
    # Fichier de config uniquement pour les tests.
    app.config.from_object('gbapp.tests.config')
    return app

my_quest = Question("coucou, Paris")
print(my_quest.text_to_analyse)

print(my_quest.parse_my_question())
"""


class FakeRequest:
    def __init__(self, response):
        self.text = response


def test_wiki_return(monkeypatch):
    result = '{"candidates": [], "error_message": "You have exceeded your daily request quota for this API. If you did not set a custom daily request quota, verify your project has an active billing account: http://g.co/dev/maps-no-account", "status": "OVER_QUERY_LIMIT"}'

    def mockreturn(API_WIKI, params):
        return FakeRequest(result)

    monkeypatch.setattr(requests, 'get', mockreturn)

    my_quest = script.Question("Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ? ")

    assert json.loads(result)['error_message'] in my_quest.maps_info()
