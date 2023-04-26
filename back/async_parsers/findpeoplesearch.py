import json
import aiohttp
import asyncio
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup


async def findpeoplesearch(*args, **kwargs):
    first_name = kwargs["first_name"]
    middle_name = kwargs["middle_name"]
    last_name = kwargs["last_name"]
    city = kwargs["city"]
    state = kwargs["state"]
    name = f"{first_name} {last_name}"

    cookies = {

    }

    headers = {
        'authority': 'www.findpeoplesearch.com',
        'accept': '*/*',
        'accept-language': 'en-US,en',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.findpeoplesearch.com',
        'referer': 'https://www.findpeoplesearch.com/Billie+Bones/null/null/null/null/null/null/null/null/null/null/null/1/null/16787510919391',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'formData': f'&full_name={name}&age=null&state={state}&email=null&address=null&city={city}&zip=null&akas=null&phone=null&month=null&day=null&year=null&url_timestamp=16787510919391',
    }

    async with aiohttp.ClientSession(cookies=cookies, headers=headers) as session:
        async with session.post('https://www.findpeoplesearch.com/search_ajax.php', data=data) as response:

            content = await response.text()

            soup = BeautifulSoup(content, 'html.parser')

            all_items = soup.find_all(class_='panel panel-default')

            mentions = []

            for num, item in enumerate(all_items):
                try:
                    head_name = item.find(class_='head_name').text.replace('\n', '').replace('\t', '').split(' - ')
                    name = head_name[0]
                    age = head_name[1]
                    lived_raw = item.find('h6')
                    all_a = lived_raw.find_all('a')
                    lived = []
                    for a in all_a:
                        place = a.text
                        if place != 'View More':
                            lived.append(place.strip())

                    mentions.append({'name': name, 'age': age, 'lived': lived})
                except Exception as ex:
                    print(f'error in findpeoplesearch {ex}')
                    continue

            return mentions

# async def main():
#     mentions = await findpeoplesearch(first_name='John', middle_name='Doe', last_name='Smith', city='Los Angeles', state='CA')
#     print(mentions)
#
# asyncio.run(main())