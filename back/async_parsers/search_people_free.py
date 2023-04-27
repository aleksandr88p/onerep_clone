import re
import asyncio
import time

from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

async def search_people_free(*args, **kwargs):
    first_name = kwargs["first_name"]
    middle_name = kwargs["middle_name"]
    last_name = kwargs["last_name"]
    city = kwargs["city"].strip().replace(' ', '-')
    state = kwargs["state"]
    proxy = kwargs['proxy']
    url = f"https://searchpeoplefree.com/find/{first_name}-{last_name}/{state}/{city}"
    async with async_playwright() as p:
        # Запуск браузера с указанием прокси
        browser = await p.chromium.launch(headless=True, proxy=proxy)

        context = await browser.new_context()
        page = await context.new_page()
        # Создание новой вкладки
        # page = await browser.new_page()
        # Установка таймаута на выполнение операции
        page.set_default_timeout(60000)
        headers = {
            'authority': 'searchpeoplefree.com',
            # 'authority': 'https://searchpeoplefree.com/',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            # 'cookie': '__cf_bm=sjW7B4ND44ZUTHyFsGlfCcI5ei53tZto5hR0ZE3rdr4-1681294341-0-Aeu7AfURtqQqx5J2oqikd7UVhUoPLybtSK+VGVVf04YpIyVrWDimPAf2+X6N2/ehtO0sDd+yfsVfu3VuY4aQTvQ=',
            'accept-language': 'en-US,en',
            'cache-control': 'max-age=0',
            'dnt': '1',
            'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        }

        await page.set_extra_http_headers(headers)
        # Переход на страницу
        await page.goto(url, timeout=120000)
        # Get the HTML code
        html = await page.content()
        soup = BeautifulSoup(html, 'html.parser')
        all_items = soup.find_all('li', attrs={'class': 'toc'})
        mentions = []
        for item in all_items:
            try:
                # contents[0] для извлечения первого элемента из списка дочерних элементов тега h2
                name = item.find('h2', {'class': 'h2'}).contents[0].strip()
                try:
                    age_str = item.find('h3', {'class': 'mb-3'}).find('span').get_text(strip=True)
                    age = re.findall('\d+', age_str)[0]
                except:
                    age = ''

                lived = []
                address_tags = item.find_all('a', href=True)

                for address_tag in address_tags:
                    if 'address' in address_tag['href']:
                        lived.append(address_tag.text.strip())

                mentions.append({'name': name, 'age': age, 'lived': lived})
            except Exception:
                print(f'error in item')

        return mentions




# import json
# d = asyncio.run(search_people_free(first_name='billie', middle_name='', last_name='bones', state='ID', city=''))
# print(json.dumps(d, indent=4))