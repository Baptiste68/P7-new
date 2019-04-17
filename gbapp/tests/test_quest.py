import pytest
import os
import sys
sys.path.append(".")
from models import Question

"""
def create_app(self):
    # Fichier de config uniquement pour les tests.
    app.config.from_object('gbapp.tests.config')
    return app
"""
my_quest = Question("coucou, Paris")
print(my_quest.text_to_analyse)

print(my_quest.parse_my_question())

