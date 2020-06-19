import requests

class Movie:
    def get_indonesian_movies(self):
        url = requests.get("https://api.themoviedb.org/3/discover/movie?api_key=6ee5671a60dffcfba9b370c145061ef8&language=id-ID&region=ID&sort_by=popularity.asc&include_adult=false&include_video=false&page=1")
        respon = url.json()
        print(respon)

    def get_movie_by_keanureeves(self):
        url = requests.get("https://api.themoviedb.org/3/person/6384/movie_credits?api_key=6ee5671a60dffcfba9b370c145061ef8&language=en-US")
        respon = url.json()
        print(respon)

    def get_movie_by_RobertDowney(self):
        url = requests.get("https://api.themoviedb.org/3/person/3223/movie_credits?api_key=6ee5671a60dffcfba9b370c145061ef8&language=en-US")
        respon = url.json()
        print(respon)

    def get_movie_by_TomHolland(self):
        url = requests.get(" https://api.themoviedb.org/3/person/1136406/movie_credits?api_key=6ee5671a60dffcfba9b370c145061ef8&language=en-US")
        respon = url.json()
        print(respon)

    def get_popular_movie_2016(self):
        url = requests.get("https://api.themoviedb.org/3/discover/movie?api_key=6ee5671a60dffcfba9b370c145061ef8&language=en-US&sort_by=popularity.asc&include_adult=false&include_video=false&page=1&year=2016&vote_count.gte=7.5")
        respon = url.json()
        print(respon)



movie = Movie()
# movie.get_indonesian_movies()
# movie.get_popular_movie_2016()
# movie.get_movie_by_keanureeves()
# movie.get_movie_by_RobertDowney()
# movie.get_movie_by_TomHolland()
