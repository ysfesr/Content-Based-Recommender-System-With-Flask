from flask import Flask, render_template, request
import numpy as np
import pandas as pd

app = Flask(__name__)

def import_data():
    titles = pd.read_csv('ressources/movie_title.csv')
    cosin_sim = np.load('ressources/cosin_sim.npy')
    return titles, cosin_sim

def get_recommendation(title):
    try:
        titles.head()
        cosin_sim.shape
    except:
        titles, cosin_sim = import_data()
    
    indices = pd.Series(titles.index, index=titles['movie_title'])
    idx = indices[title]
    sim_scores = list(enumerate(cosin_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    movies = titles['movie_title'].iloc[movie_indices]
    return list(movies)


@app.route("/", methods=['POST', 'GET'])
def home():
    titles = pd.read_csv('ressources/movie_title.csv')['movie_title'].values.tolist()
    if request.method == "POST":
        title = request.form['movie_title']
        movies_title = get_recommendation(title)
        return render_template('home.html',title=title, movies_title=movies_title, titles=titles)
    else:
        return render_template('home.html', titles=titles)



if __name__ == '__main__':
    app.run(debug=True)