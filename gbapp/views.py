from random import randint

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
            res = {'question': request.form['textquestion']}
            res.update({'err_parse': ''})
            # Managing the parsing errors
            if ERROR_MSG['PARSED_FAILED'] in my_parse:
                res.update({'err_parse': my_parse})
                res.update(
                    {'error_bla': question.blabla_sentence(
                        "error", randint(0, 2))})

            else:
                # Maps API
                maps_ans = question.maps_info()
                print(maps_ans)
                res.update({'err_map': ''})

                if ERROR_MSG['CONNECTION_FAILED_MAPS'] in maps_ans:
                    res.update({'err_map': maps_ans})
                    res.update(
                        {'error_bla': question.blabla_sentence(
                            "error", randint(0, 2))})

                elif ERROR_MSG['NOTHING_FOUND_MAP'] in maps_ans:
                    res.update({'err_map': maps_ans})
                    res.update(
                        {'error_bla': question.blabla_sentence(
                            "error", randint(0, 2))})

                else:
                    res.update({'addr': maps_ans})
                    res.update({'coord': question.get_coord()})
                    res.update({'blabla_google': question.blabla_sentence(
                        "maps_true", randint(0, 2))})

                # WIKI API
                wiki_ans = question.wiki_info()
                res.update({'err_wiki': ''})

                if ERROR_MSG['CONNECTION_FAILED_WIKI'] in wiki_ans:
                    res.update({'err_wiki': wiki_ans})
                    res.update(
                        {'error_bla': question.blabla_sentence(
                            "error", randint(0, 2))})

                elif ERROR_MSG['NOTHING_FOUND_WIKI'] in wiki_ans:
                    res.update({'err_wiki': wiki_ans})
                    res.update(
                        {'error_bla': question.blabla_sentence(
                            "error", randint(0, 2))})

                else:
                    res.update({'wiki_ans': wiki_ans})
                    res.update({'link_wiki': question.get_link_wiki()})
                    res.update({'blabla_wiki': question.blabla_sentence(
                        "wiki_true", randint(0, 2))})

                print(res)

            return jsonify(res)

    return 'Undefined failed'


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
