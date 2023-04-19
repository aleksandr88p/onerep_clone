import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

async def fast_people_search(*args, **kwargs):
    # Extract search parameters from keyword arguments
    first_name = kwargs["first_name"]
    middle_name = kwargs["middle_name"]
    last_name = kwargs["last_name"]
    city = kwargs["city"].strip()
    if len(city.split(' ')) > 1:
        city = kwargs['city'].replace(' ', '-')
    state = kwargs["state"]

    if state:
        if city:
            url = f'https://www.fastpeoplesearch.com/name/{first_name}-{last_name}_{city}-{state}'
        else:
            url = f'https://www.fastpeoplesearch.com/name/{first_name}-{last_name}_{state}'
    else:
        url = f'https://www.fastpeoplesearch.com/name/{first_name}-{last_name}'

    # настройки прокси-сервера
    proxy_url = 'http://45.145.58.25:8000'
    proxy_username = '4UsLX7'
    proxy_password = 'tCDbq9'
    proxy = {"server": proxy_url, "username": proxy_username, "password": proxy_password}

    async with async_playwright() as p:
        # Launch the browser
        browser = await p.chromium.launch(headless=True, proxy=proxy)

        # Create a new page
        page = await browser.new_page()

        # Set the user agent
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        }
        await page.set_extra_http_headers(headers)

        # Navigate to the URL
        await page.goto(url, timeout=1200000)

        # Get the HTML code
        html = await page.content()

        # Close the browser
        await browser.close()

    soup = BeautifulSoup(html, 'html.parser')
    all_items = soup.find_all('div', attrs={"class": "card-block"})
    mentions = []
    try:
        for item in all_items:
            age_element = item.find('h3', string='Age:')
            age = age_element.next_sibling.strip()

            full_name_element = item.find('h3', string='Full Name:')
            name = full_name_element.next_sibling.strip()

            lived = []

            try:
                first_adr = item.find("div", {'style': 'line-height:20px;margin-bottom:15px'}).text.replace('\n', ' ').strip()
                lived.append(first_adr)
                all_addr = item.find('div', {'class': 'row'}).find_all('a')
                for addr in all_addr:
                    lived.append(addr.text.replace('\n', ' ').strip())
            except Exception as ex:
                print(f'error in address in fastpeoplesearch.com {ex}')

            mentions.append({'name': name, 'age': age, 'lived': lived})
            # print(name, age)
            # print(lived)

    except Exception as e:
        print(f'error in item   {e}')
    print(url)

    return mentions


# d = asyncio.run(fast_people_search(first_name='aleks', middle_name='', last_name='smith', state='NY', city=''))
d = asyncio.run(fast_people_search(first_name='john', middle_name='', last_name='doe', state='NY', city='port-jefferson-station'))

import json

print(json.dumps(d, indent=4))
