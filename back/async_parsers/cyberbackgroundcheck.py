import asyncio
import json
import time

from playwright.async_api import async_playwright
from bs4 import BeautifulSoup


async def cyberbackgroundcheck(*args, **kwargs):
    first_name = kwargs["first_name"]
    middle_name = kwargs["middle_name"]
    last_name = kwargs["last_name"]
    city = kwargs["city"].strip().replace(' ', '-')
    state = kwargs["state"]
    if state:
        if city:
            url = f'https://www.cyberbackgroundchecks.com/people/{first_name}-{last_name}/{state}/{city}'
        else:
            url = f'https://www.cyberbackgroundchecks.com/people/{first_name}-{last_name}/{state}'
    else:
        url = f'https://www.cyberbackgroundchecks.com/people/{first_name}-{last_name}'
    headers = {
        'authority': 'www.cyberbackgroundchecks.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en',
        'cache-control': 'max-age=0',
        # 'cookie': '_gcl_au=1.1.2026433346.1682536694; __gads=ID=4a21b2d135bc949f-22197034afdd004a:T=1682536694:RT=1682536694:S=ALNI_MaO82fkyy9F0qn-AC4HR8Cjj22Afg; __gpi=UID=00000bf15d97bd46:T=1682536694:RT=1682536694:S=ALNI_MY4CrbcaPIyqn9ajLMekS8YErZEkQ; _ga=GA1.2.840778125.1682536694; _gid=GA1.2.142999026.1682536695; __cf_bm=NmN0C2vZoC9FCMs7DbklMSYCLcX_ityKEbLIpQKWHIY-1682536695-0-Ad5agYzLpqz0o5C3ew/Pgp+ssGsbLJilFARAm0fRHCNdZmxISl0PAtjnM4j1LkOSsoKM4qFmAj6ybRNMLwG6q0n1y08nZ7OewffO73dOxtaAh629rQ0t6etcVLxvoN5C3+iKFusX+4ni19dGfI5g7n0=; _ga_ETWB2J0GG5=GS1.1.1682536694.1.1.1682536804.0.0.0; cf_chl_2=3478024b7b9eddc; cf_chl_rc_m=1',
        'pragma': 'no-cache',
        'referer': f'{url}',
        'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    }
    async with async_playwright() as p:
        try:
            browser = await p.chromium.launch(headless=True, proxy={
                "server": "http://45.155.201.162:8000",
                "username": "4UsLX7",
                "password": "tCDbq9"})

            context = await browser.new_context()
            page = await context.new_page()
            await page.set_extra_http_headers(headers)
            await page.goto(url, timeout=1200000)

            html = await page.content()
            soup = BeautifulSoup(html, 'html.parser')
            mentions = []
            all_items = soup.find_all('div', attrs={'class': 'card card-hover'})
            for item in all_items:
                try:
                    name = item.find('span', attrs={'class': ['name-given', 'name-searched-on']})
                    if name is not None:
                        name = name.text.strip()
                    else:
                        continue

                    age = item.find('span', attrs={'class': 'age'})
                    if age is not None:
                        age = age.text
                    else:
                        age = ''

                    locations = []
                    try:
                        all_address = item.find_all('a', attrs={'class': 'address'})
                        for i in all_address:
                            locations.append(i.text)
                    except:
                        print('error in location cyberbackgr')
                    mentions.append({'name': name, 'age': age, 'lived': locations})

                except Exception as e:
                    print(f'error in item in cyber\n{e}')

            await context.close()
            return mentions
        except Exception as e:
            print('error in cyber')



#
# d = asyncio.run(cyberbackgroundcheck(first_name='MARK', middle_name='', last_name='Smith', state='NY', city='new york'))
# print(json.dumps(d, indent=4))