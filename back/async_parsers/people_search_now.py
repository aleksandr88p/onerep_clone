from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import asyncio


async def people_search_now(*args, **kwargs):
    first_name = kwargs["first_name"]
    middle_name = kwargs["middle_name"]
    last_name = kwargs["last_name"]
    city = kwargs["city"].strip().replace(' ', '-')
    state = kwargs["state"]
    proxy = kwargs['proxy']


    if state:
        if city:
            url = f'https://www.peoplesearchnow.com/person/{first_name}-{last_name}_{city}_{state}'
        else:
            url = f'https://www.peoplesearchnow.com/person/{first_name}-{last_name}_{state}'
    else:
        url = f'https://www.peoplesearchnow.com/person/{first_name}-{last_name}'


    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, proxy=proxy)

        headers = {
            'authority': 'www.peoplesearchnow.com',
            'authority': 'www.peoplesearchnow.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        }

        page = await browser.new_page()
        await page.set_extra_http_headers(headers)
        await page.goto(url, timeout=1200000)

        content = await page.content()

        soup = BeautifulSoup(content, 'html.parser')

        all_items = soup.find_all('div', attrs={'class': 'result-search-block'})
        mentions = []
        for item in all_items:
            try:
                name = item.find('p', attrs={'itemprop': 'name'}).text
                # Находим первый элемент span и получаем его текстовое значение
                age_span = item.find('span', string='Approximate Age:').find_next_sibling('span')
                age = age_span.get_text(strip=True)
                lived = []
                all_addr = item.find_all('span', attrs={'itemprop': 'address'})
                for addr in all_addr:
                    try:
                        adr = addr.find('a').text.split(';')[1].strip()[:-10]
                        lived.append(adr)
                    except Exception as e:
                        print(f'error in adr {e}')
                    mentions.append({'name': name, 'age': age, 'lived': lived})

            except:
                print('error in item')

        # await asyncio.sleep(1200)  # пауза на 2 минуты
        await browser.close()
        return mentions


# import json
#
# d = asyncio.run(people_search_now(first_name='sam', middle_name='', last_name='smith', state='ny', city='new york'))
# print(json.dumps(d, indent=4))
