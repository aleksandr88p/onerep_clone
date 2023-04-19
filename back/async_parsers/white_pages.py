import asyncio

from playwright.async_api import async_playwright
from bs4 import BeautifulSoup


async def white_pages(*args, **kwargs):
    first_name = kwargs["first_name"]
    middle_name = kwargs["middle_name"]
    last_name = kwargs["last_name"]
    city = kwargs["city"].strip().replace(' ', '-')
    state = kwargs["state"]
    if state:
        if city:
            url = f'https://www.whitepages.com/name/{first_name}-{last_name}/{city}-{state}'
        else:
            url = f'https://www.whitepages.com/name/{first_name}-{last_name}/{state}'
    else:
        url = f'https://www.whitepages.com/name/{first_name}-{last_name}'
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        headers = {
            'authority': 'www.whitepages.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en',
            'cache-control': 'max-age=0',
            'cookie': '_ga=GA1.2.723349806.1678918913; initial_referrer=https://www.google.com/; initial_referring_domain=www.google.com; shown_cookie_banner=true; accepted_tos_via_serp=true; _gid=GA1.2.1570949844.1681306649; com_whitepages_wp_app_test=0; wp_pid=f107f88c155f4968b7ffda2a652f003b; amp_4452f9=-qgrRG7LHJhQA9H2ffvfXs...1gtrl66fl.1gtrl66g3.1k.1k.38; __cf_bm=Pae6zUha2vSWUssebAO06Oh6CLzMcbpbV1ISfWN7zk8-1681336009-0-Ae1jlwg7uQhNKvDYTnGISt3+VoHPSzVfGWFJWHIXcyWecmnyQ3PzjJc36IrxvRR5OgVJH5oQar21M4XBlQBQewk=',
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

        response = await page.goto(url, timeout=1200000)

        content = await page.content()

        # f1 = open('white_page.html')
        # content = f1.read()
        soup = BeautifulSoup(content, 'html.parser')
        all_items = soup.find_all('div', attrs={'class': 'serp-card'})
        mentions = []
        for item in all_items:
            try:
                name_wrap = item.find('div', class_='name-wrap')
                name = name_wrap.contents[0].strip() # Берем первый дочерний элемент, убираем пробельные символы в начале и конце строки
                age = item.find('span', {'class': 'person-age'}).text
                lived = []
                all_addr = item.find_all('div', attrs={'class': "address-item"})
                for addr in all_addr:
                    lived.append(addr.text.strip())
                mentions.append({'name': name, 'age': age, 'lived': lived})
            except Exception:
                print('error in item')
        # await asyncio.sleep(300)


        await browser.close()
        return mentions

# import json
# d = asyncio.run(white_pages(first_name='john', middle_name='', last_name='smith', state='ny', city='new york'))
#
# print(json.dumps(d, indent=4))