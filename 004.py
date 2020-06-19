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

    # def get_movie_by_RobertDowney(self):
    #     url = requests.get("https://api.themoviedb.org/3/person/3223/movie_credits?api_key=6ee5671a60dffcfba9b370c145061ef8&language=en-US")
    #     respon = url.json()
    #     # print(respon)
    #     return respon

    # def get_movie_by_TomHolland(self):
    #     url = requests.get(" https://api.themoviedb.org/3/person/1136406/movie_credits?api_key=6ee5671a60dffcfba9b370c145061ef8&language=en-US")
    #     respon = url.json()
    #     # print(respon)
    #     return respon

    def tiga(self):
        respon1 = requests.get("https://api.themoviedb.org/3/person/3223/movie_credits?api_key=6ee5671a60dffcfba9b370c145061ef8&language=en-US")
        data1 = respon1.json()['cast']
        respon2 = requests.get(" https://api.themoviedb.org/3/person/1136406/movie_credits?api_key=6ee5671a60dffcfba9b370c145061ef8&language=en-US")
        data2 = respon2.json()['cast']
        new_data = []
        for i in data1:
            for b in data2:
                if i == b:
                    new_data.append()
        print(new_data)

    def get_popular_movie_2016(self):
        url = requests.get("https://api.themoviedb.org/3/discover/movie?api_key=6ee5671a60dffcfba9b370c145061ef8&language=en-US&sort_by=popularity.asc&include_adult=false&include_video=false&page=1&year=2016&vote_count.gte=7.5")
        respon = url.json()
        print(respon)



movie = Movie()
# movie.get_indonesian_movies()
# movie.get_popular_movie_2016()
# movie.get_movie_by_keanureeves()
movie.tiga()

# res1 = movie.get_movie_by_RobertDowney()
# res2 = movie.get_movie_by_TomHolland()

# def combine(res1, res2):
#     new_data = []
#     for a in res1:
#         for b in res2:
#             if a == b:
#                 new_data.append(a)
#     print(list(new_data))
# combine(res1, res2)
