from flask import Flask, render_template, request, jsonify

from .models import Question
from config import ERROR_MSG

app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')

@app.route('/question', methods=['POST'])
def question():
    # If textquestion exist and then if not empty
    if "textquestion" in request.form:

        if request.form['textquestion'] is not '':

            # Then, create a Question
            question = Question(request.form['textquestion'])
            # Parsing the question
            my_parse = question.parse_my_question()
            # Preparing the answer on JSON format
            wiki = {'question': request.form['textquestion']}
            # Managing the parsing errors

            if ERROR_MSG['PARSED_FAILED'] in my_parse:
                wiki.update({'result': my_parse})

            else:
                maps_step1 = question.maps_info()
                print(maps_step1)
                wiki.update(maps_step1)
                """
                wiki.update({'result': question.wiki_info()})
                if not ERROR_MSG['NOTHING_FOUND'] in question.wiki_info():
                    wiki.update({'link_wiki': question.get_link_wiki()})
                """
                wiki.update({'result': 'res'})
                wiki.update({'coord': maps_step1['candidates'][0]['geometry']['location']})
                print(wiki)
            return jsonify(wiki)
    return 'QQ'

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()