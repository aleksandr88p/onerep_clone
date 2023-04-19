import requests

headers = {
    'authority': 'api.intelius.com',
    'accept': '*/*',
    'accept-language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6',
    'api-key': 'KMyvOP3HPen9GqoWGSQJ1HcZz4vuh01mVLpyqVRIDgE',
    'app-id': 'intelius-web',
    'device-id': 'dbfb40b3-d9e5-4116-a197-6779c20a2499',
    'dnt': '1',
    'origin': 'https://www.intelius.com',
    'referer': 'https://www.intelius.com/search/?affid=1117&campid=3120&mdm=&src=DIME&sid=www.peoplefinder.com&utm_source=DIME&utm_campaign=www.peoplefinder.com&utm_medium=&utm_content=&utm_term=&mdm=&page=h&origin=icm&traffic[source]=DIME&traffic[medium]=&traffic[campaign]=:www.peoplefinder.com&traffic[term]=&traffic[content]=&s1=www.peoplefinder.com&s2=&s3=&s4=&s5=&traffic[funnel]=bg&traffic[placement]=&firstName=billie&lastName=bones&city=eagle&state=ID',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

params = {
    'firstName': 'Billie',
    'lastName': 'Bones',
    'fields': 'names,locations,related_persons',
    'state': 'ID',
    'city': 'eagle',
}

response = requests.get('https://api.intelius.com/v1/people/', params=params, headers=headers)


import json
print(json.dumps(response.json(), indent=4))
# print(response.json())



# import requests
#
# headers = {
#     'authority': 'api.intelius.com',
#     'accept': '*/*',
#     'accept-language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6',
#     'access-control-request-headers': 'api-key,app-id,device-id',
#     'access-control-request-method': 'GET',
#     'origin': 'https://www.intelius.com',
#     'referer': 'https://www.intelius.com/search/?affid=1117&campid=3120&mdm=&src=DIME&sid=www.peoplefinder.com&utm_source=DIME&utm_campaign=www.peoplefinder.com&utm_medium=&utm_content=&utm_term=&mdm=&page=h&origin=icm&traffic[source]=DIME&traffic[medium]=&traffic[campaign]=:www.peoplefinder.com&traffic[term]=&traffic[content]=&s1=www.peoplefinder.com&s2=&s3=&s4=&s5=&traffic[funnel]=bg&traffic[placement]=&firstName=billie&lastName=bones&city=&state=Select+state',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-site',
#     'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
# }
#
# params = {
#     'firstName': 'Billie',
#     'lastName': 'Bones',
#     'fields': 'names,locations,related_persons',
# }
#
# response = requests.options('https://api.intelius.com/v1/people/', params=params, headers=headers)