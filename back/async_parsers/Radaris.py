import time

import requests
from bs4 import BeautifulSoup
from helpers import states_dict
from playwright.async_api import async_playwright

async def radaris(*args, **kwargs):
    first_name = kwargs["first_name"]
    middle_name = kwargs["middle_name"]
    last_name = kwargs["last_name"]
    city = kwargs["city"]
    if kwargs['state']:
        state = states_dict[kwargs["state"]]
    else:
        state = ""

    cookies = {
        '_pgt': 'B23B',
        'g_uvh': '505517572297304361',
        '_gid': 'GA1.2.274127436.1680642609',
        '_ga_24CE6DFC9D': 'GS1.1.1680642608.4.1.1680642706.0.0.0',
        '_ga': 'GA1.2.985038774.1678468473',
    }

    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    }

    params = {
        'ff': f'{first_name}',
        'fl': f'{last_name}',
        'fs': f'{state}',
        'fc': f'{city}',
    }

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        await page.set_extra_http_headers(headers)

        url = f'https://radaris.com/ng/search?ff={first_name}&fl={last_name}&fs={state}&fc={city}'

        # print(url)
        # Navigate to the URL
        await page.goto(url, timeout=1200000)

        # time.sleep(30)
        # Get page content
        content = await page.content()

        soup = BeautifulSoup(content, 'html.parser')
        all_items = soup.find_all('div', attrs={"class": "card teaser-card"})
        mentions = []
        try:
            for num, item in enumerate(all_items):
                name_elem = item.find('a', class_='card-title')
                if name_elem:
                    name = name_elem.text.strip()
                else:
                    name = ""
                age_elem = item.find('div', class_='age-wr')
                if age_elem:
                    age = age_elem.text.strip()
                else:
                    age = ""
                lived_elems = item.find_all('dd', class_='nowrap')
                if lived_elems:
                    lived = [elem.text.strip() for elem in lived_elems]
                else:
                    lived = [""]
                if name.split()[0].lower() == first_name.lower():

                    mentions.append({'name': name, 'age': age, 'lived': lived})
        except Exception as e:
            print(f'error in item   {e}')
        finally:
            await browser.close()

    return mentions


# import asyncio
# #
# #
# import json
# #
# d = asyncio.run(radaris(first_name="billie", middle_name="", last_name="bones", state="AK", city="Cantwell"))
# print(json.dumps(d, indent=4))