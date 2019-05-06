import pytest
import os
import sys
import re
import requests
import json
from gbapp import models as script


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
    #   - Url is sending to the right place 
    @pytest.mark.skip(reason="no way of currently testing this")
    def test_url():
        assert hello('toi') == 'toit'

    #   - The header display adequat information 
    @pytest.mark.skip(reason="no way of currently testing this")
    def test_header():
        assert hello('toi') == 'toit'

    #   - The footer display adequat information 
    @pytest.mark.skip(reason="no way of currently testing this")
    def test_footer():
        assert hello('toi') == 'toit'

    #   - At launch, the body is an empty area with a form to enter question
    @pytest.mark.skip(reason="no way of currently testing this")
    def test_body():
        assert hello('toi') == 'toit'


#############################################
################ Question ###################
#############################################

class TestQuest:
    # -- Question tests
    question = script.Question('Coucou, ou est l\'endroit Paris?')

    #   - The question is well buffered
    def test_qbuffer(self):
        assert self.question.parse_my_question() == 'paris'

    #   - The question is then display in the free area
    @pytest.mark.skip(reason="no way of currently testing this")
    def test_qdisplay():
        assert hello('toi') == 'toit'

    #   - The displaying is auto adapting 
    @pytest.mark.skip(reason="no way of currently testing this")
    def test_adapting():
        assert hello('toi') == 'toit'


#############################################
################# Answer ####################
#############################################


class TestAnswer():
#-- Answer management 
#   - API connection 
    @pytest.mark.skip(reason="no way of currently testing this")
    def test_api_co():
        assert hello('toi') == 'toit'

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


#   - The story of GranPy is displayed 
    @pytest.mark.skip(reason="no way of currently testing this")
    def test_stories():
        assert hello('toi') == 'toit'

#   - Correct link
    def test_link(self, monkeypatch):
        result = '{"batchcomplete": "", "continue": {"gsroffset": 1, "continue": "gsroffset||"}, "query": {"pageids": ["4338589"], "pages": {"4338589": {"pageid": 4338589, "ns": 0, "title": "OpenClassrooms", "index": 1, "extract": "OpenClassrooms est une école en "}}}}'

        def mockreturn(API_WIKI, params):
            return FakeRequest(result)

        monkeypatch.setattr(requests, 'get', mockreturn)

        my_quest = script.Question("Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ? ")
        my_quest.wiki_info()

        assert my_quest.get_link_wiki() == "https://fr.wikipedia.org/?curid=4338589"

