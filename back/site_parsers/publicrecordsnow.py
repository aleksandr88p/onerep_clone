"""
https://www.publicrecordsnow.com/name/Billie+Bones/eagle/ID/
https://www.publicrecordsnow.com/name/billie+bones/-none-/-none-/
"""
import json

import requests
from bs4 import BeautifulSoup


def publicrecordsnow(name, surename, city='-none-', state='-none-'):
    cookies = {
        '_gcl_au': '1.1.1114480529.1678919287',
        '_gid': 'GA1.2.2058094499.1678919287',
        'session': 'eyJkZXZpY2UiOm51bGwsIm5ldHdvcmsiOm51bGwsInB1Ymxpc2hlciI6IlVOS05PV04ifQ.ZBRN2g.EbXVHxRVmOj_XDCcZf7h2R4Q9hA',
        '_uetsid': 'a8f18bf0c38011edafe069b492fb43e6',
        '_uetvid': 'a8f1e640c38011edaa2daba43c656837',
        '_ga': 'GA1.1.1972518481.1678919287',
        '_ga_M4X6ZNH0MB': 'GS1.1.1679051947.5.1.1679052256.0.0.0',
    }

    headers = {
        'authority': 'www.publicrecordsnow.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6',
        'cache-control': 'max-age=0',
        # 'cookie': '_gcl_au=1.1.1114480529.1678919287; _gid=GA1.2.2058094499.1678919287; session=eyJkZXZpY2UiOm51bGwsIm5ldHdvcmsiOm51bGwsInB1Ymxpc2hlciI6IlVOS05PV04ifQ.ZBRN2g.EbXVHxRVmOj_XDCcZf7h2R4Q9hA; _uetsid=a8f18bf0c38011edafe069b492fb43e6; _uetvid=a8f1e640c38011edaa2daba43c656837; _ga=GA1.1.1972518481.1678919287; _ga_M4X6ZNH0MB=GS1.1.1679051947.5.1.1679052256.0.0.0',
        'dnt': '1',
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

    url = f'https://www.publicrecordsnow.com/name/{name}+{surename}/{city}/{state}/'

    response = requests.get(url, cookies=cookies, headers=headers)
    #
    #
    # with open('result.html', 'w') as f:
    #     f.write(response.text)

    # f1 = open('result.html', 'r')
    # content = f1.read()
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    result_container = soup.find('div', attrs={'class': 'search-results-container'})
    all_div_res = result_container.find_all('div', attrs={'class': 'result'})
    mentions = {}
    for num_, div_res in enumerate(all_div_res):
        num = num_ + 1
        name_age = div_res.find(attrs={'class': 'result-name'})
        name = name_age.find(attrs={"itemprop": "name"}).text.strip()
        age = name_age.text.replace(name, '').strip().replace('(', '').replace(')', '')

        lived = []
        try:
            cur_address = div_res.find(attrs={'class': 'result-current-address'}).text
            lived.append(cur_address)
            all_address = div_res.find_all(attrs={'class': 'address'})
            for address in all_address:
                lived.append(address.text.strip())
        except:
            continue
        mentions[num] = {'name': name, 'age': age, 'lived': lived}

    # f1.close()

    return mentions





d = publicrecordsnow('bille', 'bones', city='eagle', state='id')
# d = publicrecordsnow('bille', 'bones')


print(json.dumps(d, indent=4))