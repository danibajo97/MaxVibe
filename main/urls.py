from main import views
from django.urls import path

urlpatterns = [
    path('', views.Home, name='Home'),

    path('register', views.Register, name='Register'),
    path('login', views.Login, name='Login'),
    path('logout', views.Logout, name='Logout'),

    path('tv_shows/<int:tv_id>/details', views.TVDetails, name='TVDetails'),
    path('tv_shows/', views.TVGrid, name='TVGrid'),

    path('movies/', views.MovieGrid, name='MovieGrid'),
    path('movies/list/', views.MovieList, name='MovieList'),
    path('movies/<int:movie_id>/details', views.MovieDetails, name='MovieDetails'),

    path('persons/<int:person_id>/details', views.PersonDetails, name='PersonDetails'),
    path('persons/', views.PersonGrid, name='PersonGrid'),
]
