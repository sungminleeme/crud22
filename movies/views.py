import json
from django.views import View
from django.http import JsonResponse
from .models import Actor, Movie

class ActorView(View):
    def get(self, request):
        actors = Actor.objects.all()
        result = []

        for actor in actors:
            movies = actor.movie_set.all()
            movies_list = []

            for movie in movies:
                    movies_info = {
                            'title' : movie.title}
                    movies_list.append(movies_info)
            actor_info = {
                    'first_name'	: actor.first_name,
                    'last_name'	: actor.last_name,
                    'date_of_birth'	: actor.date_of_birth,
                    'movies'	: movies_list
            }

            result.append(actor_info)

        return JsonResponse({'result':result}, status=200)

class MovieView(View):
    def get(self, request):
        movies = Movie.objects.all()
        result = []

        for movie in movies:
            result.append(
                {
                    "first_name" : actor.first_name,
                    "last_name"  : actor.last_name,
                    "movies" : [{
                        'title'        : movie.title,
                        'release_date' : movie.release_date,
                        'running_time' : movie.running_time,
                        'actors'       : actors_list
                    } for actor in movies.actors.all()] # actors.movie_set.all()
                }
            )

        return JsonResponse({'result':result}, status=200)
