"""
https://www.quickpeopletrace.com/search/?addresssearch=1&tabid=1&teaser-firstname=billie&teaser-middlename=j&teaser-lastname=bones&teaser-city=eagle&teaser-state=ID&teaser-submitted=Search
"""
import aiohttp
import asyncio
import re
from bs4 import BeautifulSoup
import json

async def quikpeopletrace(*args, **kwargs):
    first_name = kwargs["first_name"]
    middle_name = kwargs["middle_name"]
    last_name = kwargs["last_name"]
    city = kwargs["city"]
    state = kwargs["state"]


    cookies = {
        '_ga': 'GA1.2.738786664.1678919181',
    }

    headers = {
        'authority': 'www.quickpeopletrace.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en',
        'cache-control': 'max-age=0',
        'dnt': '1',
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
    params = {
        'addresssearch': '1',
        'tabid': '1',
        'teaser-firstname': f'{first_name}',
        'teaser-middlename': f'{middle_name}',
        'teaser-lastname': f'{last_name}',
        'teaser-city': f'{city}',
        'teaser-state': f'{state}',
        'teaser-submitted': 'Search',
    }
    async with aiohttp.ClientSession(cookies=cookies, headers=headers) as session:
        async with session.get('https://www.quickpeopletrace.com/search/', params=params) as response:
            content = await response.text()
            soup = BeautifulSoup(content, 'html.parser')
            big_table = soup.find('table', attrs={'id': 'usatrace-result-table'})
            all_tr_tags = big_table.find_all('tr')[1::]
            mentions = []
            for tr_tag in all_tr_tags:
                all_td_tags = tr_tag.find_all('td')
                num = all_td_tags[0].text
                name = all_td_tags[1].text
                name = re.sub('\s+', ' ', name).strip() # удаляю лишние пробелы между словами
                age = all_td_tags[2].text
                lived = []
                all_br_tags = all_td_tags[3].find_all('br')
                for br_tag in all_br_tags:
                    place = br_tag.previous_sibling.strip()
                    lived.append(place)
                mentions.append({'name': name, 'age': age, 'lived': lived})

            return mentions




# import asyncio
# async def main():
#     mentions = await quikpeopletrace(first_name='billie', last_name='bones', middle_name='', state='', city='')
#     return mentions
#
# d = asyncio.run(main())
# print(json.dumps(d, indent=4))

