import pytest
import os
import sys
import re
sys.path.append(".")
import models as script


def create_app(self):
    # Fichier de config uniquement pour les tests.
    app.config.from_object('gbapp.tests.config')
    return app

def hello(name):
    return 'Hello ' + name

def test_hello():
    assert hello('Celine') == 'Hello Celine'



#############################################
################## Page #####################
#############################################

class TestPage:
    #-- Basic page test
    #   - Url is sending to the right place 
    def test_url():
        assert hello('toi') == 'toit'

    #   - The header display adequat information 
    def test_header():
        assert hello('toi') == 'toit'

    #   - The footer display adequat information 
    def test_footer():
        assert hello('toi') == 'toit'

    #   - At launch, the body is an empty area with a form to enter question
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
    def test_qdisplay():
        assert hello('toi') == 'toit'

    #   - The displaying is auto adapting 
    def test_adapting():
        assert hello('toi') == 'toit'


#############################################
################# Answer ####################
#############################################

class TestAnswer:
#-- Answer management 
#   - API connection 
    def test_api_co():
        assert hello('toi') == 'toit'

#   - Correct API field taken 
    def test_api_field():
        assert hello('toi') == 'toit'

#   - Errors are handeled 
    def test_errors():
        assert hello('toi') == 'toit'

#   - The story of GranPy is displayed 
    def test_stories():
        assert hello('toi') == 'toit'

#   - Possible link is clickable 
    def test_clickable():
        assert hello('toi') == 'toit'

