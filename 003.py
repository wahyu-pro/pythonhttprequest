import requests, json

def combinePostAndUsers(res1, res2):
    new_data = []
    for data in  res1:
        if 'users' in res1:
            pass
        else:
            for x in res2:
                if data['userId'] == x['id']:
                    data.update({'user' : x})
        new_data.append(data)
    
    toJson =  json.dumps(new_data, indent=4)
    fwrite = open('file.json', 'w')
    fwrite.write(toJson)


get1 = requests.get("https://jsonplaceholder.typicode.com/posts") 
res1 = get1.json()

get2 = requests.get("https://jsonplaceholder.typicode.com/users") 
res2 = get2.json()

json = combinePostAndUsers(res1, res2)