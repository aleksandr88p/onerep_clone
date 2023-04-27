

import aiohttp
import asyncio
from _helpers import states_dict
from bs4 import BeautifulSoup


async def people_search(*args, **kwargs):
    first_name = kwargs["first_name"]
    middle_name = kwargs["middle_name"]
    last_name = kwargs["last_name"]
    city = kwargs["city"]
    # state = states_dict[kwargs["state"]]
    state = kwargs['state']
    proxy = kwargs['proxy']


    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'accept-language': 'en-US,en',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
    }

    params = {
        's_name': f'{first_name} {last_name}',
        's_loc': f'{city}, {state}',
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get('https://peoplesearch.com/search', params=params, ssl=False) as response:
            print(response.url)
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')
            all_items = soup.find_all('div', attrs={
                'class': 'text-ps-black bg-white 2xl:ml-3 gap-3 grid grid-cols-1 hover:bg-ps-white hover:ring-1 hover:ring-inset hover:ring-ps-grey-border hover:shadow-lg lg:ml-6 lg:mr-3 lg:mx-0 lg:p-6 mb-6 md:grid-cols-4 md:p-6 p-3 rounded-none shadow-md sm:mx-6 sm:p-4 sm:rounded-xl'})
            mentions = []
            for item in all_items:
                try:
                    name_age = item.find_all('div', attrs={
                        'class': 'flex flex-row items-center flex-wrap md:flex-col md:items-start md:row-span-2'})

                    name = name_age[0].find('h2', class_='font-semibold text-lg md:text-xl').text.strip()
                    try:
                        age = name_age[0].find('h3', class_='flex').find('span', class_='font-medium').text.replace('s',
                                                                                                                    '')
                    except:
                        age = ''
                        print('error age')

                    location = []
                    try:
                        cur_loc = name_age[0].find('div',
                                                   class_='flex flex-row flex-wrap md:flex-col font-medium').find_all(
                            'div')
                        loc = ''
                        for i in cur_loc:
                            loc += f'{i.text} '
                        location.append(loc.strip())
                    except:
                        print('error in location')

                    mentions.append({'name': name, 'age': age, 'lived': location})
                except:
                    print('error in item n people_search')

            return mentions

# d = asyncio.run(people_search(first_name='billie', middle_name='', last_name='bones', city='new york', state='NY'))
# print(json.dumps(d, indent=4))