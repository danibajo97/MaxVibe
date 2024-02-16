import requests
from django import template

from django.conf import settings

register = template.Library()

TMDB_API_KEY = settings.TMDB_API_KEY

movie_genre_list_request = requests.get(f"https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}")
movie_genre_list_results = movie_genre_list_request.json()
movie_genre_list = {genre['id']: genre['name'] for genre in movie_genre_list_results['genres']}

@register.filter
def get_movie_genre_name(genre_id):
    return movie_genre_list.get(genre_id, False)



