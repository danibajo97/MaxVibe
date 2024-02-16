from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from MaxVibe.settings import TMDB_API_KEY
import requests


# @login_required(login_url='Login')
def PersonGrid(request):
    now_playing_movies_request = requests.get("https://api.themoviedb.org/3/movie/now_playing?api_key=" + TMDB_API_KEY)
    now_playing_movies_results = now_playing_movies_request.json()
    now_playing_movies = now_playing_movies_results['results']

    return render(request, 'movies/moviegrid.html', context={'now_playing_movies': now_playing_movies})


# @login_required(login_url='Login')
def PersonDetails(request, person_id):
    tv_details_request = requests.get("https://api.themoviedb.org/3/tv/" + str(tv_id) + "?api_key=" + TMDB_API_KEY)
    tv_details_results = tv_details_request.json()
    tv_details = tv_details_results

    tv_video_request = requests.get("https://api.themoviedb.org/3/tv/" + str(tv_id) + "/videos?api_key=" + TMDB_API_KEY)
    tv_video_results = tv_video_request.json()
    tv_shows = tv_video_results['results']
    newDict = dict()
    for tv in tv_shows:
        if tv['type'] == 'Trailer':
            newDict['key'] = tv['key']

    return render(request, 'TV Details.html', {'tv_details': tv_details, 'tv_id': tv_id, 'newDict': newDict})
