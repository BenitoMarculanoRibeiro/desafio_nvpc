from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    posts = [{'title': 'Hello'},{'title': 'Ola'}]
    return render_template('i.html', posts=posts)


@app.route('/contatos')
def contatos():
    return 'Essa é a pagina de contatos'


app.run()
