import requests, json

get1 = requests.get("https://jsonplaceholder.typicode.com/posts") 
res1 = get1.json()

get2 = requests.get("https://jsonplaceholder.typicode.com/users") 
data = get2.json()
print(data)

# merge = requests.post("https://jsonplaceholder.typicode.com/posts", params=data)

# toJson = json.dumps(merge, indent=4)
# fwrite = open("file.json", 'w')
# fwrite.write(toJson)


