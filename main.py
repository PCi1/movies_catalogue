from flask import Flask, render_template, request
import tmdb_client
import random

app = Flask(__name__)

#homepage z top8
@app.route('/')
def homepage():
    all_lists = ['now_playing', 'popular', 'upcoming', 'top_rated']
    selected_list = request.args.get('list_type')
    movies = tmdb_client.get_movies(how_many=8, list_type=selected_list)
    return render_template('homepage.html', movies=movies, current_list = selected_list, all_lists = all_lists)

#homepage z losowymi filmami
# @app.route("/")
# def homepage():
#     selected_list = request.args.get('list_type', 'popular')
#     movies = tmdb_client.get_random_movies(how_many=8)
#     return render_template('homepage.html', movies=movies, current_list=selected_list)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

@app.route('/movie/<movie_id>')
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_credits(movie_id)
    movie_images = tmdb_client.get_single_movie_images(movie_id)
    selected_backdrop = random.choice(movie_images['backdrops'])
    selected_backdrop_file_path = selected_backdrop.get('file_path')
    return render_template("movie_details.html", movie = details, cast = cast, selected_backdrop = selected_backdrop_file_path)

if __name__ == "__main__":
    app.run()