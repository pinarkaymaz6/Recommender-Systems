import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

moviemat = pd.read_pickle("movie_matrix.pkl")
ratings = pd.read_pickle("ratings.pkl")

@app.route('/')
def root():
    return render_template('index.html')


@app.route('/movies')
def get_movies():
    movie_list = list(moviemat.columns)
    return render_template('movies.html', mlist=movie_list)


@app.route('/movies/<movie>')
def get_similar(movie):
    user_ratings = moviemat[movie]
    similar_movies = moviemat.corrwith(user_ratings)
    corr = pd.DataFrame(similar_movies, columns=['Correlation'])
    corr.dropna(inplace=True)
    corr = corr.join(ratings['num of ratings'])
    recommend = corr[corr['num of ratings'] > 100].sort_values(
    'Correlation', ascending=False)
    results = list(recommend.iloc[1:4].index)
    html = "".join([f"<p>{movie}</p>" for movie in results])
    return html


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
