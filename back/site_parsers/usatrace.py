"""
https://www.usatrace.com/people-search/billie-jo-bones/New-York-NY
                                имя среднее имя, фамилия, город, штат

usatrace.com/people-search/Cahek-Pyl/New-York-NM/ нету результатов
https://www.usatrace.com/people-search/billie-jo-bones/New-York-NY нету результатов

"""

import requests


def usatrace(first_name, last_name, state, city=None):
    '''

    :param first_name:
    :param last_name:
    :param state:
    :param city:
    :return:
    '''

    cookies = {
        'PHPSESSID': 'eae732f95a69de1cc892cef56d54c7ea',
        '_ga': 'GA1.2.1179357062.1678837740',
        '_gid': 'GA1.2.1465235612.1678837740',
    }

    headers = {
        'authority': 'www.usatrace.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6',
        'cache-control': 'max-age=0',
        # 'cookie': 'PHPSESSID=eae732f95a69de1cc892cef56d54c7ea; _ga=GA1.2.1179357062.1678837740; _gid=GA1.2.1465235612.1678837740',
        'dnt': '1',
        'if-modified-since': 'Wed, 15 Mar 2023 20:39:04 GMT',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    }

    from bs4 import BeautifulSoup

    if not city:
        url = f"https://www.usatrace.com/people-search/{first_name}-{last_name}/{state}"
    else:
        url = f"https://www.usatrace.com/people-search/{first_name}-{last_name}/{city}-{state}"


    response = requests.get(url, cookies=cookies, headers=headers)



    # with open('result.html', 'a') as f:
    #     f.write(response.text)
    # f1 = open('result.html')
    # content = f1.read()

    content = response.text
    soup = BeautifulSoup(content, 'lxml')
    table_res = soup.find('table', attrs={'id': 'usatrace-result-table'})
    if not table_res:
        return None # нету результатов

    all_tr = table_res.find_all('tr')
    if len(all_tr) < 2:
        return None # что то не так

    mentions = {}
    for tr in all_tr[1::]: # так как первый tr это шапка таблицы
        all_td = tr.find_all('td')
        num = all_td[0].text
        name = all_td[1].text
        age = all_td[2].text
        # lived = all_td[3].text
        lived = []
        all_br = all_td[3].find_all('br')

        for br in all_br:
            place = br.previous_sibling.strip()
            lived.append(place)
        mentions[num] = {'name': name, 'age': age, 'lived': lived}



    # f1.close()
    return mentions






import json

print(json.dumps(usatrace('billie', 'bones', 'CA'), indent=4))
# usatrace('billie', 'bones', 'CA')