import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

moviemat = pd.read_pickle("movie_matrix.pkl")

@app.route('/')
def root():
    return render_template('index.html')


@app.route('/movies')
def movies():
    movie_list = list(moviemat.columns[:5])
    return render_template('movies.html', mlist=movie_list)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
