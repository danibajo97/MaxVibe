from django.shortcuts import render
from MaxVibe.settings import TMDB_API_KEY
import requests


def Home(request):
    trending_movies_request = requests.get("https://api.themoviedb.org/3/trending/movie/day?api_key=" + TMDB_API_KEY)
    trending_movies_results = trending_movies_request.json()
    trending_movies = trending_movies_results['results']

    now_playing_movies_request = requests.get("https://api.themoviedb.org/3/movie/now_playing?api_key=" + TMDB_API_KEY)
    now_playing_movies_results = now_playing_movies_request.json()
    now_playing_movies = now_playing_movies_results['results']

    top_rated_movies_request = requests.get("https://api.themoviedb.org/3/movie/top_rated?api_key=" + TMDB_API_KEY)
    top_rated_movies_results = top_rated_movies_request.json()
    top_rated_movies = top_rated_movies_results['results']

    upcoming_movies_request = requests.get("https://api.themoviedb.org/3/movie/upcoming?api_key=" + TMDB_API_KEY)
    upcoming_movies_results = upcoming_movies_request.json()
    upcoming_movies = upcoming_movies_results['results']

    popular_movies_request = requests.get("https://api.themoviedb.org/3/movie/popular?api_key=" + TMDB_API_KEY)
    popular_movies_results = popular_movies_request.json()
    popular_movies = popular_movies_results['results']

    airing_today_tv_request = requests.get("https://api.themoviedb.org/3/tv/airing_today?api_key=" + TMDB_API_KEY)
    airing_today_tv_results = airing_today_tv_request.json()
    airing_today_tv = airing_today_tv_results['results']

    on_the_air_tv_request = requests.get("https://api.themoviedb.org/3/tv/on_the_air?api_key=" + TMDB_API_KEY)
    on_the_air_tv_results = on_the_air_tv_request.json()
    on_the_air_tv = on_the_air_tv_results['results']

    popular_tv_request = requests.get("https://api.themoviedb.org/3/tv/popular?api_key=" + TMDB_API_KEY)
    popular_tv_results = popular_tv_request.json()
    popular_tv = popular_tv_results['results']

    top_rated_tv_request = requests.get("https://api.themoviedb.org/3/tv/top_rated?api_key=" + TMDB_API_KEY)
    top_rated_tv_results = top_rated_tv_request.json()
    top_rated_tv = top_rated_tv_results['results']

    person_popular_request = requests.get("https://api.themoviedb.org/3/person/popular?api_key=" + TMDB_API_KEY)
    person_popular_results = person_popular_request.json()
    person_popular = person_popular_results['results']

    context = {
        'trending_movies': trending_movies,
        'now_playing_movies': now_playing_movies,
        'top_rated_movies': top_rated_movies,
        'upcoming_movies': upcoming_movies,
        'popular_movies': popular_movies,

        'airing_today_tv': airing_today_tv,
        'on_the_air_tv': on_the_air_tv,
        'top_rated_tv': top_rated_tv,
        'popular_tv': popular_tv,

        'person_popular': person_popular
    }

    return render(request, 'index.html', context=context)
