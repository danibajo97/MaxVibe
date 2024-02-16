import requests
from django import template

from django.conf import settings

register = template.Library()

TMDB_API_KEY = settings.TMDB_API_KEY

tv_genre_list_request = requests.get(f"https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}")
tv_genre_list_results = tv_genre_list_request.json()
tv_genre_list = {genre['id']: genre['name'] for genre in tv_genre_list_results['genres']}


@register.filter
def get_tv_genre_name(genre_id):
    return tv_genre_list.get(genre_id, 'Unknown')
