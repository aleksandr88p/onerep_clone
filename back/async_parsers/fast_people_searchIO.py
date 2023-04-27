import json
import time

import requests
import re



from playwright.async_api import async_playwright
from bs4 import BeautifulSoup


async def fast_people_IO(*args, **kwargs):
    first_name = kwargs["first_name"]
    middle_name = kwargs.get("middle_name", "")
    last_name = kwargs["last_name"]
    city = kwargs.get("city", "")
    state = kwargs.get("state", "")
    proxy = kwargs['proxy']

    if state:
        url = f'https://fastpeoplesearch.io/person/{first_name}-{last_name}/{state}'
    else:
        url = f'https://fastpeoplesearch.io/person/{first_name}-{last_name}/'

    # print(url) https://fastpeoplesearch.io/person/john-smith/ny  https://fastpeoplesearch.io/person/john-doe/ny
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, proxy=proxy)
        context = await browser.new_context(ignore_https_errors=True)
        page = await context.new_page()
        headers = {
            'authority': 'fastpeoplesearch.io',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en',
            'cache-control': 'no-cache',
            'cookie': '_ga=GA1.2.1858836356.1681938071; _gid=GA1.2.829514841.1681938071; __cf_bm=wHXaO1Xilr0rDPt7GPBm5LlS1IY0Z5tpWSPfiL4RUgw-1681938070-0-AS+1YWzrwNWbttLkjbgdtfdvDr+LhNqNRbkCkJAk17F4xRX+YwhttKUOMFm9/JnQRR49QrEI7mayi5ObJMMVQVxidGq0X1b8iXvDZBAzQM/X; cf_chl_2=08ca133f0ae137d; cf_chl_rc_i=1; _gat_UA-205149453-1=1',
            'pragma': 'no-cache',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        }

        await page.set_extra_http_headers(headers)

        await page.goto(url, timeout=1200000)
        content = await page.content()
        # with open('fast_people_IO.html', 'r') as f:
        #     content = f.read()

        soup = BeautifulSoup(content, 'html.parser')
        all_items = soup.find_all('div', attrs={'class': 'lg:w-full lg:mb-4 font-bold'})
        mentions = []
        for item in all_items:
            try:
                name_age = item.find('h2').text.split(' Age ')
                if len(name_age) == 2:
                    name = name_age[0]
                    age = name_age[1]
                else:
                    name = name_age[0]
                    age = ''
                location_regex = r'Known Locations:.*?([A-Z][a-z]+(?:\s[A-Z][a-z]+)*,\s*[A-Z]{2})'
                match = re.search(location_regex, item.text)
                lived = []
                if match:
                    location = match.group(1)
                    lived.append(location)
                else:
                    print('Location not found')
                lives_loc_regex = r'Lives:.*?([A-Z][a-z]+(?:\s[A-Z][a-z]+)*\s*[A-Z]{2})'
                match = re.search(lives_loc_regex, item.text)
                if match:
                    location = match.group(1)
                    lived.append(location)
                mentions.append({'name': name, 'age': age, 'lived': lived})
            except Exception as e:
                print(f'error in item fastpeopleIO\n {e}')
        # time.sleep(60)

        return mentions


import asyncio
# d = asyncio.run(fast_people_IO(first_name='marbin', middle_name='', last_name='jimenez', state='', city=''))
#
#
# print(json.dumps(d, indent=4))