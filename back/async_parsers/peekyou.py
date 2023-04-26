import asyncio
import json

from bs4 import BeautifulSoup
import aiohttp
import requests
from helpers import states_dict

async def peekyou(*args, **kwargs):
    first_name = kwargs["first_name"]
    middle_name = kwargs["middle_name"]
    last_name = kwargs["last_name"]
    city = kwargs["city"]
    state = states_dict[kwargs["state"]]
    if state:
        url = f'https://www.peekyou.com/usa/{state}/{first_name}_{last_name}'
    else:
        url = f'https://www.peekyou.com/usa/{first_name}_{last_name}'

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'accept-language': 'en-US,en',
        'DNT': '1',
        'Connection': 'keep-alive',
        # 'Cookie': 'PHPSESSID=686a35b2fb9f5382de74f9836665401e',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url, ssl=False) as response:
            content = await response.text()

            soup = BeautifulSoup(content, 'html.parser')

            all_items = soup.find_all('div', class_='resultCell')
            mentions = []
            for item in all_items:
                try:
                    age = item.find('span', class_='age')
                    name = item.find('h2').text.strip()
                    also_name = item.find('span', class_='userName')
                    if age is not None:
                        age = age.text
                        name = name.replace(age, '').strip()
                        age = age.replace('Age', '').strip()
                    else:
                        age = ''
                    if also_name:
                        name = f"{name} also knows as: {also_name.text.strip()}"
                    locations = []
                    all_locs = item.find('p', class_='locations').find_all(('a', 'span'))
                    for loc in all_locs:
                        locations.append(loc.text)

                    mentions.append({'name': name, 'age': age, 'lived': locations})

                except:
                    print('error in peekyou')

    return mentions


#
# d = asyncio.run(peekyou(first_name='john', middle_name='', last_name='doe', city='Los Angeles', state='CA'))
#
# print(json.dumps(d, indent=4))