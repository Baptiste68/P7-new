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
from selenium import webdriver
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

"""
class FakeRequest:
    def __init__(self, response):
        self.text = response


def test_wiki_return(monkeypatch):
    result = '{"batchcomplete": "", "continue": {"gsroffset": 1, "continue": "gsroffset||"}, "query": {"pageids": ["4338589"], "pages": {"4338589": {"pageid": 4338589, "ns": 0, "title": "OpenClassrooms", "index": 1, "extract": "OpenClassrooms est une école en "}}}}'

    def mockreturn(API_WIKI, params):
        return FakeRequest(result)

    monkeypatch.setattr(requests, 'get', mockreturn)

    my_quest = script.Question("Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ? ")
    my_quest.wiki_info()
    a = my_quest.wiki_info.payload

    assert my_quest.get_link_wiki() == "https://fr.wikipedia.org/?curid=4338589"
"""

URL = 'http://localhost:5000'



def test_app():
    browser = webdriver.Chrome(executable_path =r'C:\Users\TAASIBA2\Documents\Pypy\P7\chromedriver.exe')
    browser.visit("https://google.com")
    assert browser.is_text_present('Bonjour !')
    browser.quit()