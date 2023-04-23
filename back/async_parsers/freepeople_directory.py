import json

import asyncio
import aiohttp
from bs4 import BeautifulSoup

async def freepeople_directory(*args, **kwargs):
    first_name = kwargs["first_name"]
    middle_name = kwargs["middle_name"]
    last_name = kwargs["last_name"]
    city = kwargs["city"].replace(' ', '-')
    state = kwargs['state']

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'accept-language': 'en-US,en',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
    }
    if state:
        if city:
            url = f'https://freepeopledirectory.com/name/{first_name}-{last_name}/{state}/{city}'
        else:
            url = f'https://freepeopledirectory.com/name/{first_name}-{last_name}/{state}'
    else:
        url = f'https://freepeopledirectory.com/name/{first_name}-{last_name}'

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url=url, ssl=False) as response:
            print(response.url)
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')

            all_items = soup.find_all('div', class_='whole-card result-card row')
            mentions = []
            for item in all_items:
                try:
                    name = item.find('h2', class_='card-title').text
                    age = ''
                    lived = []
                    place = item.find('h3', class_='city').text
                    lived.append(place)

                    mentions.append({'name': name, 'age': age, 'lived': lived})

                except:
                    print('error in item')

            return mentions

#
# d = asyncio.run(freepeople_directory(first_name='elliot', middle_name='', last_name='smith', city='new york', state='NY'))
# print(json.dumps(d, indent=4))