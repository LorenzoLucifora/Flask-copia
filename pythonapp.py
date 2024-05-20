from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def hello_world():
    bottoni = {
        'b1' : 'film',
        'b2' : 'libri',
        'b3' :'musica'
    }
    return render_template('home.html', titolo='Benvenuti nel nostro sito'.upper(), bottoni=bottoni)

if __name__ == '__main__':
    app.run(debug=True)