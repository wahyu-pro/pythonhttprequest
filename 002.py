import requests, datetime

class FindEmployees:
    url = "https://mul14.github.io/data/employees.json"
    def whice_have_salary(self):
        respon = requests.get(self.url)
        json = respon.json()
        result = filter(lambda a: (a['salary'] > 15000000), json)
        print(list(result))

    def which_life_in_Jakarta(self):
        respon = requests.get(self.url)
        json = respon.json()
        rep = filter(lambda a: a['addresses'][0]['city'] == "DKI Jakarta", json)
        print(list(rep))

    def whice_have_department(self):
        respon = requests.get(self.url)
        json = respon.json()
        result = filter(lambda a: (a['department']['name'] == "Research and development"), json)
        print(list(result))
    
    def whice_have_month(self):
        respon = requests.get(self.url)
        res = respon.json()
        result = filter(lambda a: (a['birthday']), res)
        obj = []
        for i in result:
            date_str = i['birthday']
            date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
            month = date_obj.month
            obj.append(month)

        hasil = filter(lambda a: a == 3, obj)
        print(list(hasil))

    def absence(self):
        respon = requests.get(self.url)
        json = respon.json()
        rep = lambda a: [x for x in a if datetime.datetime.strptime(x, "%Y-%m-%d").month == 10]
        # result = list(map(lambda a: "{} {} = {}".format(a["first_name"], a["last_name"], len(a["presence_list"]))), rep)
        result = list(map(lambda a: "{} {} = {} hari".format(a['first_name'], a['last_name'], len(rep(a['presence_list']))), json))
        print(result)
        # print(rep)


fetch = FindEmployees()
fetch.whice_have_salary()
fetch.which_life_in_Jakarta()
fetch.whice_have_month()
fetch.whice_have_department()
fetch.absence()