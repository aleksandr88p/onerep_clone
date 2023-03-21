import requests
from bs4 import BeautifulSoup

def golookup(name, surename, state=''):
    '''

    :param name:
    :param surename:
    :param state:
    :return:
    '''

    cookies = {
        'laravel_session': 'eyJpdiI6IjUxTWYyVTFBTWhhS0w5b0laRk1NdXc9PSIsInZhbHVlIjoiVEpsMkhBeFVnaGZqT21uNjBubExFYk9PV3Q0WnJkRjdPS3ZSbmoxVFRGeldFWG82Qm1wSmE0MFlJOWY0ajl6UGN0aklWUWRKZXd2cnQ1UlU1SXNmU0lrRHlvKzdyNU5wdS8zTUZHaGowdkxacUVrYW05KzJ1bCtRQkV2RkpYL2YiLCJtYWMiOiI5ZGU0M2Y2NzZlNTcxMzNhN2FhMzQzOTcyMGNlMjE1NmEwY2ZjMzA1NjJiMTllMzlkNGM0MGJmMWFjOWRiZjI5IiwidGFnIjoiIn0%3D',
        '_gcl_au': '1.1.1975623024.1679164334',
        '_gid': 'GA1.2.974212858.1679164334',
        '_gat_gtag_UA_68116049_1': '1',
        '_ga_Q6QGWFP4LR': 'GS1.1.1679164333.1.0.1679164333.60.0.0',
        '_ga': 'GA1.1.2089458694.1679164334',
        '__ssid': '1c0688dfee9e58304de788bf0069c62',
    }

    headers = {
        'authority': 'golookup.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'laravel_session=eyJpdiI6IjUxTWYyVTFBTWhhS0w5b0laRk1NdXc9PSIsInZhbHVlIjoiVEpsMkhBeFVnaGZqT21uNjBubExFYk9PV3Q0WnJkRjdPS3ZSbmoxVFRGeldFWG82Qm1wSmE0MFlJOWY0ajl6UGN0aklWUWRKZXd2cnQ1UlU1SXNmU0lrRHlvKzdyNU5wdS8zTUZHaGowdkxacUVrYW05KzJ1bCtRQkV2RkpYL2YiLCJtYWMiOiI5ZGU0M2Y2NzZlNTcxMzNhN2FhMzQzOTcyMGNlMjE1NmEwY2ZjMzA1NjJiMTllMzlkNGM0MGJmMWFjOWRiZjI5IiwidGFnIjoiIn0%3D; _gcl_au=1.1.1975623024.1679164334; _gid=GA1.2.974212858.1679164334; _gat_gtag_UA_68116049_1=1; _ga_Q6QGWFP4LR=GS1.1.1679164333.1.0.1679164333.60.0.0; _ga=GA1.1.2089458694.1679164334; __ssid=1c0688dfee9e58304de788bf0069c62',
        'dnt': '1',
        'origin': 'https://golookup.com',
        'referer': 'https://golookup.com/',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    }

    data = {
        'affid': '14',
        'tc': '14',
        'firstName': f'{name}',
        'lastName': f'{surename}',
        'state': f'{state}',
    }

    # первый реквест что бы отправить запрос и найти ссылку для редиректа
    response = requests.post(
        'https://golookup.com/lander/people/default/processPeopleSearch',
        cookies=cookies,
        headers=headers,
        data=data,
    )

    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        response2 = requests.get(soup.find('lander-people-default-loading')['redirect-url'], cookies=cookies, headers=headers)

        # with open('result.html', 'a') as f:
        #     f.write(response2.text)
        # f1 = open('result.html', 'r')
        # content = f1.read()

        content = response2.text
        soup2 = BeautifulSoup(content, 'html.parser')

        all_items = soup2.find_all('div', attrs={"class": "process-record"})
        mentions = {}
        for num_, item in enumerate(all_items):
            num = num_ + 1
            name = item.find('div', attrs={'class': 'name'}).text.strip()
            age = item.find('div', attrs={'class': 'age'}).text.strip().replace('years old', '').strip()
            lived = []
            locations = item.find('ul')
            try:
                for location in locations:
                    loca = location.text.strip().split(';  ')
                    if len(loca) > 1:
                        loc = loca[1].split(' *')[0]
                        lived.append(loc)
            except:
                print('bad loc')

            mentions[num] = {'name': name, 'age': age, 'lived': lived}

        # f1.close()
        return mentions

    except Exception as ex:
        print('bad redirect\n{ex}')



print('старт')
d = golookup('billy', 'bones',state='CO')

import json

print(json.dumps(d, indent=4))

print("finish")