import asyncio
import json

from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import re


async def anywho(*args, **kwargs):
    first_name = kwargs["first_name"]
    middle_name = kwargs.get("middle_name", "")
    last_name = kwargs["last_name"]
    city = kwargs.get("city", "").strip().replace(" ", "+")
    state = kwargs.get("state", "")
    proxy = kwargs['proxy']

    if state:
        if city:
            url = f'https://www.anywho.com/people/{first_name}+{last_name}/{city}+{state}/'
        else:
            url = f'https://www.anywho.com/people/{first_name}+{last_name}/{state}/'
    else:
        url = f'https://www.anywho.com/people/{first_name}+{last_name}/'

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(ignore_https_errors=True)
        page = await context.new_page()

        headers = {
            'authority': 'www.anywho.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6',
            'cache-control': 'max-age=0',
            'dnt': '1',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        }

        await page.set_extra_http_headers(headers)
        await page.goto(url, timeout=1200000)

        html = await page.content()

        soup = BeautifulSoup(html, 'html.parser')
        all_item = soup.find_all('div', {'class': 'person-info'})
        mentions = []
        for item in all_item:
            try:
                # Извлечение имени
                name_tag = item.find('a', {'class': 'name-link'})
                name = name_tag.text.strip()


                # Извлечение возраста
                age_match = re.search(r'Age\s(\d+)', item.text)
                if age_match:
                    age = age_match.group(1)
                else:
                    age = None

                lived = []
                # Извлечение адреса
                address_tag = item.find('p')
                address = address_tag.text.strip()
                lived.append(address)

                mentions.append({'name': name, 'age': age, 'lived': lived})
            except Exception as e:
                print(f'error in item anywho\n{e}')
        await browser.close()
        return mentions

# d = asyncio.run(anywho(first_name='john', middle_name='', last_name='smith', state='', city=''))
#
#
# print(json.dumps(d, indent=4))