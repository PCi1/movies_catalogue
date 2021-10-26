import requests
import json
import random
from random import shuffle

API_TOKEN = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3MDdiYWJlMDE5ZThlZjFkMjgwNDM3Njg0NGNjODkyOCIsInN1YiI6IjYxNmRlYjU3MTNhMzIwMDAyNDQ2Mjg4MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.2CCKZcddjdskz5Kj0WEmg13GZmL1iEFsBYuerxU0Sd0'

def get_all_movies(list_name='popular'):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_name}"
    headers = {
        'Authorization': f'Bearer {API_TOKEN}'
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def get_all_movies_as_list():
    all_movies = get_all_movies()
    results = all_movies.get('results')
    return results

def get_poster_url(image_path, image_size = "w342"):
    base_url = "https://image.tmdb.org/t/p"
    image_url = f"{base_url}/{image_size}{image_path}"
    response = requests.get(image_url)
    return image_url

def get_movie_info(id):
    movie_title = get_all_movies['results'][id].get('title')
    poster_url = get_poster_url(get_all_movies['results'][id].get('poster_path'))
    return {movie_title: poster_url}

def get_movies(how_many, list_type):
    if list_type not in ['now_playing', 'popular', 'upcoming', 'top_rated']:
        list_type = 'popular'
    data = get_all_movies(list_name = list_type)
    data_as_list = data.get('results')
    return data_as_list[:how_many]

def get_random_movies(how_many):
    movies_list = get_all_movies['results']
    shuffle(movies_list)
    return movies_list[:how_many]

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        'Authorization': f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_credits(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        'Authorization': f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers = headers)
    return response.json()['cast']

def get_single_movie_images(movie_id):
    endpoint = f'https://api.themoviedb.org/3/movie/{movie_id}/images'
    headers = {
        'Authorization': f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers = headers)
    return response.json()