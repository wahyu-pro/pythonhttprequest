import requests

class Movie:
    def get_indonesian_movies(self):
        url = requests.get(" https://api.themoviedb.org/3/discover/movie?api_key=6ee5671a60dffcfba9b370c145061ef8&language=id-ID&region=ID&sort_by=popularity.asc&include_adult=false&include_video=false&page=1")
        respon = url.json()
        result = list(map(lambda a: a['title'], respon['results']))
        print(result[0:10])

    def get_movie_by_keanureeves(self):
        url = requests.get("https://api.themoviedb.org/3/person/6384/movie_credits?api_key=6ee5671a60dffcfba9b370c145061ef8&language=en-US")
        respon = url.json()
        result = list(map(lambda a: a['title'], respon['cast']))
        print(result)

    def get_movie_played_by_RobertDowneyJr_and_TomHolland(self):
        respon1 = requests.get("https://api.themoviedb.org/3/person/3223/movie_credits?api_key=6ee5671a60dffcfba9b370c145061ef8&language=en-US")
        fetch1 = respon1.json()
        data1 = list(map(lambda a: a['title'], fetch1['cast']))
        respon2 = requests.get(" https://api.themoviedb.org/3/person/1136406/movie_credits?api_key=6ee5671a60dffcfba9b370c145061ef8&language=en-US")
        fetch2 = respon2.json()
        data2 = list(map(lambda a: a['title'], fetch2['cast']))
        new_data = []
        for i in data1:
            for b in data2:
                if i == b:
                    new_data.append(b)
        print(new_data)

    def get_popular_movie_2016(self):
        url = requests.get("https://api.themoviedb.org/3/discover/movie?api_key=6ee5671a60dffcfba9b370c145061ef8&language=en-US&sort_by=popularity.asc&include_adult=false&include_video=false&page=1&primary_release_year=2016&vote_count.gte=7.5")
        respon = url.json()
        result = list(map(lambda a: a['title'], respon['results']))
        print(result)



movie = Movie()
movie.get_indonesian_movies()
movie.get_popular_movie_2016()
movie.get_movie_by_keanureeves()
movie.get_movie_played_by_RobertDowneyJr_and_TomHolland()
