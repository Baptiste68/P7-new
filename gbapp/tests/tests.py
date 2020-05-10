import pytest
import os
import sys
import re
import requests
import json
from gbapp import models as script
from selenium import webdriver


def create_app(self):
    # Fichier de config uniquement pour les tests.
    app.config.from_object('gbapp.tests.config')
    return app


class FakeRequest:
    def __init__(self, response):
        self.text = response


#############################################
################## Page #####################
#############################################

class TestPage:
    #-- Basic page test
    browser = webdriver.Chrome(executable_path =r'D:\OCR_Codes\P7\chromedriver.exe')
    browser.get("http://127.0.0.1:5000")
    #   - Url is sending to the right place 
    def test_app(self):
        page_url = self.browser.current_url
        select = self.browser.find_element_by_tag_name('header')
        select = select.text
        assert page_url == "http://127.0.0.1:5000/"
        assert select == "Bienvenue sur la page de Granpy bot"

    #   - At launch, the body is an empty area
    def test_rep_area(self):
        select = self.browser.find_element_by_xpath("//*[@class='col-sm-10']")
        select = select.text
        assert select == ""

    #   - The header display adequat information 
    def test_header(self):
        select = self.browser.find_element_by_tag_name('header')
        select = select.text
        assert select == "Bienvenue sur la page de Granpy bot"

    #   - The footer display adequat information 
    def test_footer(self):
        select = self.browser.find_element_by_tag_name('footer')
        select = select.text
        assert "Baptiste" in select
        self.browser.close()



#############################################
################ Question ###################
#############################################

class TestQuest:
    # -- Question tests
    question = script.Question('Coucou, ou est l\'endroit Paris?')

    #   - The question is well buffered
    def test_qbuffer(self):
        assert self.question.parse_my_question() == 'paris'

    #   - The displaying is auto adapting 
    @pytest.mark.skip(reason="to be check manualy")
    def test_adapting():
        assert hello('toi') == 'toit'


#############################################
################# Answer ####################
#############################################


class TestAnswer():
#-- Answer management 
#   - API connection 

    #   - Correct adress field return Maps API     
    def test_maps_return(self, monkeypatch):
        result = '{"candidates": [{"formatted_address": "140 George St, The Rocks NSW 2000, Australie", "geometry": {"location": {"lat": -33.8599358, "lng": 151.2090295}, "viewport": {"northeast": {"lat": -33.85824767010727, "lng": 151.2102470798928}, "southwest": {"lat": -33.86094732989272, "lng": 151.2075474201073}}}}], "status": "OK"}'

        def mockreturn(API_MAPS, params):
            return FakeRequest(result)

        monkeypatch.setattr(requests, 'get', mockreturn)

        my_quest = script.Question("museum of contemporary art australia")

        assert my_quest.maps_info() == json.loads(result)['candidates'][0]['formatted_address']


    # - Correct wiki info
    def test_wiki_return(self, monkeypatch):
        result = '{"batchcomplete": "", "continue": {"gsroffset": 1, "continue": "gsroffset||"}, "query": {"pageids": ["4338589"], "pages": {"4338589": {"pageid": 4338589, "ns": 0, "title": "OpenClassrooms", "index": 1, "extract": "OpenClassrooms est une école en "}}}}'

        def mockreturn(API_WIKI, params):
            return FakeRequest(result)

        monkeypatch.setattr(requests, 'get', mockreturn)

        my_quest = script.Question("Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ? ")

        article_id = json.loads(result)['query']['pageids'][0]
        assert my_quest.wiki_info() == json.loads(result)['query']['pages'][article_id]['extract']



    # - Test quota API Google
    def test_api_quota(self, monkeypatch):
        result = '{"candidates": [], "error_message": "You have exceeded your daily request quota for this API. If you did not set a custom daily request quota, verify your project has an active billing account: http://g.co/dev/maps-no-account", "status": "OVER_QUERY_LIMIT"}'

        def mockreturn(API_WIKI, params):
            return FakeRequest(result)

        monkeypatch.setattr(requests, 'get', mockreturn)

        my_quest = script.Question("Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ? ")

        assert json.loads(result)['error_message'] in my_quest.maps_info()


#   - Correct link
    def test_link(self, monkeypatch):
        result = '{"batchcomplete": "", "continue": {"gsroffset": 1, "continue": "gsroffset||"}, "query": {"pageids": ["4338589"], "pages": {"4338589": {"pageid": 4338589, "ns": 0, "title": "OpenClassrooms", "index": 1, "extract": "OpenClassrooms est une école en "}}}}'

        def mockreturn(API_WIKI, params):
            return FakeRequest(result)

        monkeypatch.setattr(requests, 'get', mockreturn)

        my_quest = script.Question("Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ? ")
        my_quest.wiki_info()

        assert my_quest.get_link_wiki() == "https://fr.wikipedia.org/?curid=4338589"
