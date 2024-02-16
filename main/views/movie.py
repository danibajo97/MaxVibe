from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from MaxVibe.settings import TMDB_API_KEY
import requests


# @login_required(login_url='Login')
def MovieGrid(request):
    now_playing_movies_request = requests.get("https://api.themoviedb.org/3/movie/now_playing?api_key=" + TMDB_API_KEY)
    now_playing_movies_results = now_playing_movies_request.json()
    now_playing_movies = now_playing_movies_results['results']
    movies_quantity = now_playing_movies_results['total_results']

    context = {
        'now_playing_movies': now_playing_movies,
        'movies_quantity': movies_quantity,
    }

    return render(request, 'movies/moviegrid.html', context=context)


def MovieList(request):
    now_playing_movies_request = requests.get("https://api.themoviedb.org/3/movie/now_playing?api_key=" + TMDB_API_KEY)
    now_playing_movies_results = now_playing_movies_request.json()
    now_playing_movies = now_playing_movies_results['results']
    movies_quantity = now_playing_movies_results['total_results']

    context = {
        'now_playing_movies': now_playing_movies,
        'movies_quantity': movies_quantity,
    }

    return render(request, 'movies/movielist.html', context=context)


# @login_required(login_url='Login')
def MovieDetails(request, movie_id):
    movie_details_request = requests.get(
        "https://api.themoviedb.org/3/movie/" + str(movie_id) + "?api_key=" + TMDB_API_KEY)
    movie_details_results = movie_details_request.json()
    movie_details = movie_details_results

    movie_video_request = requests.get(
        "https://api.themoviedb.org/3/movie/" + str(movie_id) + "/videos?api_key=" + TMDB_API_KEY)
    movie_video_results = movie_video_request.json()
    movie_videos = movie_video_results['results']
    newDict = dict()
    for movie in movie_videos:
        if movie['type'] == 'Trailer':
            newDict['key'] = movie['key']

    return render(request, 'Movie Details.html',
                  {'movie_details': movie_details, 'movie_id': movie_id, 'newDict': newDict})
