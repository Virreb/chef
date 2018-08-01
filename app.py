from flask import Flask, render_template

app = Flask(__name__)


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


if __name__ == "__main__":
    app.run()
