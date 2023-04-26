"""
https://www.usatrace.com/people-search/billie-jo-bones/New-York-NY
                                имя среднее имя, фамилия, город, штат

usatrace.com/people-search/Cahek-Pyl/New-York-NM/ нету результатов
https://www.usatrace.com/people-search/billie-jo-bones/New-York-NY нету результатов

"""
import aiohttp
from bs4 import BeautifulSoup
import json
async def usatrace(*args, **kwargs):
    first_name = kwargs["first_name"]
    middle_name = kwargs["middle_name"]
    last_name = kwargs["last_name"]
    city = kwargs["city"].replace(' ', '-')
    state = kwargs["state"]
    cookies = {
        'PHPSESSID': 'eae732f95a69de1cc892cef56d54c7ea',
        '_ga': 'GA1.2.1179357062.1678837740',
        '_gid': 'GA1.2.1465235612.1678837740',
    }

    headers = {
        'authority': 'www.usatrace.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en',
        'cache-control': 'max-age=0',
        # 'cookie': 'PHPSESSID=eae732f95a69de1cc892cef56d54c7ea; _ga=GA1.2.1179357062.1678837740; _gid=GA1.2.1465235612.1678837740',
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

    if not city:
        url = f"https://www.usatrace.com/people-search/{first_name}-{last_name}/{state}/"
    else:
        url = f"https://www.usatrace.com/people-search/{first_name}-{last_name}/{city}-{state}/"
    print(url)
    async with aiohttp.ClientSession(cookies=cookies, headers=headers) as session:
        async with session.get(url) as response:
            content = await response.text()

            soup = BeautifulSoup(content, 'lxml')
            table_res = soup.find('table', attrs={'id': 'usatrace-result-table'})

            if not table_res:
                return None  # нету результатов

            all_tr = table_res.find_all('tr')

            if len(all_tr) < 2:
                return None  # что то не так

            mentions = []

            for tr in all_tr[1::]:  # так как первый tr это шапка таблицы
                try:
                    all_td = tr.find_all('td')
                    num = all_td[0].text
                    name = all_td[1].text
                    age = all_td[2].text
                    all_locs = all_td[3]
                    locations = []
                    for string in all_locs.stripped_strings:
                        if ',' in string:
                            locations.append(string)


                    mentions.append({'name': name, 'age': age, 'lived': locations})
                except Exception as e:
                    print(f'error in item usatrace')
            return mentions

# #
# import asyncio
# # async def main():
# #     mentions = await usatrace(first_name='john', last_name='smith', middle_name='', state='NY', city='new york')
# #     return mentions
#
# d = asyncio.run(usatrace(first_name='john', last_name='smith', middle_name='', state='NY', city='new york'))
# print(json.dumps(d, indent=4))
