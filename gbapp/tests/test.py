import gbapp.models as script
import pytest
from bs4 import BeautifulSoup


def hello(name):
    return 'Hello ' + name

def test_hello():
    assert hello('Celine') == 'Hello Celine'

#############################################
################## Page #####################
#############################################

html = """<div class="same-height-left" style="height: 20px;"><span class="value-frame">&nbsp;whatever</span></div>"""
soup = BeautifulSoup(html, 'html.parser')
method1 = soup.find('div').text
print 'Result of method 1:' + method1


class TestPage:
    #-- Basic page test
    #   - Url is sending to the right place 
    #   - The header display adequat information 
    #   - The footer display adequat information 
    #   - At launch, the body is an empty area with a form to enter question


#############################################
################ Question ###################
#############################################

class TestQuestion:
#-- Question management
#   - The question is buffered 
#   - The question is then display in the free area
#   - The displaying is auto adapting 


#############################################
################# Answer ####################
#############################################

class TestAnswer:
#-- Answer management 
#   - API connection 
#   - Correct API field taken 
#   - Errors are handeled 
#   - The story of GranPy is displayed 
#   - Possible link is clickable 

