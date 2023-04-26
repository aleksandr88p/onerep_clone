import json

import aiohttp
import asyncio
from bs4 import BeautifulSoup

async def propeoplesearch(*args, **kwargs):
    first_name = kwargs["first_name"]
    middle_name = kwargs["middle_name"]
    last_name = kwargs["last_name"]
    city = kwargs["city"]
    state = kwargs["state"]

    cookies = {
        'XSRF-TOKEN': 'eyJpdiI6IjBJZ0srY2NpMDJPNElUeWs2bHp3aHc9PSIsInZhbHVlIjoiOEtTR0dlWTNHdTgwdzhCT1MvMzZXWGQ3blloN0VuNVhydU03VWZXaUtKOUZ5Sk9kVkVKaDBDTE1qd3hxMWNsRUNCUk1LY1ZwU3JUU3NkK0tEV1VyT3c1bFJ6YTJaSGxueVdxb0hheVhBMWlxWDJtaTBqM2R4YmVrMkxLYmhrb0QiLCJtYWMiOiIwZmVhOTZjZTYzYjFjMTllZTRkYzYxNzY1ZDhmNWZkYWVmMmE0MGY1OGI5ZjUwN2UyZmRiMjFkMzdhNTg3ZWYxIn0%3D',
        'propeoplesearch_session': 'eyJpdiI6IlkyeXhWT3dHdVNBSG5SRys4QlAySXc9PSIsInZhbHVlIjoiQ0ltdVJFMWlsQ1ZRdEFmekJENzhiVjVRS1ZJdnptMng3VW54YndJWHVhVDY3LzJXcU1yY1V1c0phQWhhSkFLU25saHJrUUkvdmtoaDdGdWxFYXp2Tis4dUtWYnFrU1NIVzNtSnBUUVQxUHVYeGJUYWJHZ0F0V09QRnN3UFpQTk8iLCJtYWMiOiJlZTg0MWEwOTRhYWNkOGYwNDIyMjdhMGQwODMzMjEzYjdkYmQxNjYxZmE4ZjY5Nzg5MDZkM2JiN2E0Y2VkMDNmIn0%3D',
        '_gcl_au': '1.1.507348705.1679230577',
        '_ga': 'GA1.2.1029574918.1679230577',
        '_gid': 'GA1.2.64114197.1679230577',
        '_gat_gtag_UA_207509932_1': '1',
    }

    headers = {
        'authority': 'propeoplesearch.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'XSRF-TOKEN=eyJpdiI6IjBJZ0srY2NpMDJPNElUeWs2bHp3aHc9PSIsInZhbHVlIjoiOEtTR0dlWTNHdTgwdzhCT1MvMzZXWGQ3blloN0VuNVhydU03VWZXaUtKOUZ5Sk9kVkVKaDBDTE1qd3hxMWNsRUNCUk1LY1ZwU3JUU3NkK0tEV1VyT3c1bFJ6YTJaSGxueVdxb0hheVhBMWlxWDJtaTBqM2R4YmVrMkxLYmhrb0QiLCJtYWMiOiIwZmVhOTZjZTYzYjFjMTllZTRkYzYxNzY1ZDhmNWZkYWVmMmE0MGY1OGI5ZjUwN2UyZmRiMjFkMzdhNTg3ZWYxIn0%3D; propeoplesearch_session=eyJpdiI6IlkyeXhWT3dHdVNBSG5SRys4QlAySXc9PSIsInZhbHVlIjoiQ0ltdVJFMWlsQ1ZRdEFmekJENzhiVjVRS1ZJdnptMng3VW54YndJWHVhVDY3LzJXcU1yY1V1c0phQWhhSkFLU25saHJrUUkvdmtoaDdGdWxFYXp2Tis4dUtWYnFrU1NIVzNtSnBUUVQxUHVYeGJUYWJHZ0F0V09QRnN3UFpQTk8iLCJtYWMiOiJlZTg0MWEwOTRhYWNkOGYwNDIyMjdhMGQwODMzMjEzYjdkYmQxNjYxZmE4ZjY5Nzg5MDZkM2JiN2E0Y2VkMDNmIn0%3D; _gcl_au=1.1.507348705.1679230577; _ga=GA1.2.1029574918.1679230577; _gid=GA1.2.64114197.1679230577; _gat_gtag_UA_207509932_1=1',
        'dnt': '1',
        'origin': 'https://propeoplesearch.com',
        'referer': 'https://propeoplesearch.com/',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    }

    data = {
        '_token': 'qMLdM1C1TNTq2JQTfuENCBu8CsAxAM9o27FxHiAT',
        'affid': '2',
        'tc': '2',
        'firstName': f'{first_name}',
        'lastName': f'{last_name}',
        'city': f'{city}',
        'state': f'{state}',
    }

    async with aiohttp.ClientSession(cookies=cookies, headers=headers) as session:
        async with session.post('https://propeoplesearch.com/ld/people/default/processing', data=data) as response:
            if response.status == 200:
                async with session.get('https://propeoplesearch.com/ld/people/default/loading-results') as response2:
                    content = await response2.text()
                    soup = BeautifulSoup(content, 'html.parser')
                    all_items = soup.find_all('li', attrs={'class': 'result-list-item'})
                    mentions = []
                    for num_, item in enumerate(all_items):
                        num = num_ + 1
                        info_needed = item.find_all('div', attrs={'class': 'result-info'})
                        name = info_needed[1].text
                        age = info_needed[2].text
                        lived = []
                        locations = info_needed[3].find_all('span')
                        try:
                            for location in locations:
                                loca = location.text.strip().split('; ')[1].split(' *')[0]
                                lived.append(loca)
                        except:
                            print('bad loc')
                        mentions.append({'name': name, 'age': age, 'lived': lived})

                    return mentions



# async def main():
#     mentions = await propeoplesearch(first_name='alex', last_name='popov', middle_name='', state='NY', city='new york')
#     return mentions
#
# d = asyncio.run(main())
#
#
# print(json.dumps(d, indent=4))