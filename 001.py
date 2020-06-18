import requests, json

class Fetcher:
    @staticmethod
    def Get(url):
        respon = requests.get(url)
        json = respon.json()
        print(json)

    @staticmethod
    def Post(url, data):
        r = requests.post(url, data)
        print(r.json())

    @staticmethod
    def Delete(url):
        r = requests.delete(url)
        print(r.json())
    
    @staticmethod
    def Put(url, data):
        r = requests.put(url, data)
        print(r.json())
    
    @staticmethod
    def Patch(url, data):
        r = requests.put(url, data)
        print(r.json())

Fetcher.Get('https://httpbin.org/get')
data ={
    "id": 30,
    "name": "Wahyu"}
Fetcher.Post("https://httpbin.org/post", data)
Fetcher.Delete("https://httpbin.org/delete")
Fetcher.Put("https://httpbin.org/put", data)
Fetcher.Patch("https://httpbin.org/put", data)
