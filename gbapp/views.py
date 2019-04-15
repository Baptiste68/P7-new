from flask import Flask, render_template, request

from .models import Question

app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

@app.route('/question', methods=['POST'])
def question():
    if "textquestion" in request.form:
        print(request.form['textquestion'])
        question = Question(request.form['textquestion'])
        my_parse = question.parse_my_question()
        print(my_parse)
        wiki = question.wiki_info()
        print (wiki)
    return "Vous avez envoyé un message..."

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()