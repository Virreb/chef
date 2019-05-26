from flask import Flask, render_template
from flask_basicauth import BasicAuth
import json, os

app = Flask(__name__)

if os.path.exists('credentials.json') is False:
    print('Need credentials.json file, aborting!')
    exit()

with open('credentials.json', 'r') as f:
    credentials = json.load(f)

app.config['BASIC_AUTH_USERNAME'] = credentials['login']['username']
app.config['BASIC_AUTH_PASSWORD'] = credentials['login']['password']
app.config['BASIC_AUTH_FORCE'] = True

basic_auth = BasicAuth(app)


@app.route('/index')
@app.route('/')
def main():
    return render_template('index.html')


@app.route('/login')
def login_user():

    # show login page and get user credentials

    return render_template('login.html')


@app.route('/level_1')
def show_level_1():

    # get credentials and show available categories for that user

    return render_template('level_1.html')


@app.route('/level_2')
def show_level_2():

    # get credentials and show available categories for that user

    return render_template('level_2.html')


@app.route('/level_3')
def show_level_3():

    # get credentials and show available categories for that user

    return render_template('level_3.html')


@app.route('/level_4')
def show_level_4():

    # get credentials and show available categories for that user

    return render_template('level_4.html')


@app.route('/summaries')
def show_text_summaries():

    # Show titles of texts for the given wanted category

    return render_template('summaries.html')


@app.route('/text')
def show_text():

    # Show full wanted article

    return render_template('text.html')


@app.route('/tal/<name>')
def show_speech(name):
    print(name)

    if name == 'all':
        filename = 'level_2_tal.html'
    else:
        filename = f'tal_{name}.html'

    return render_template(filename)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
