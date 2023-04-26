

import asyncio
import random
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright


async def thath_them(*args, **kwargs):
    first_name = kwargs["first_name"]
    middle_name = kwargs["middle_name"]
    last_name = kwargs["last_name"]
    city = kwargs["city"]
    state = kwargs["state"]
    if state:
        url = f'https://thatsthem.com/name/{first_name}-{last_name}/{state}'
    else:
        url = f"https://thatsthem.com/name/{first_name}-{last_name}/"

    headers = {
            'authority': 'thatsthem.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en',
            'cookie': 'PHPSESSID=Y8QBOdhl9DbRLeaB3Qntuv%2C7vud-5xvpniyGZsqcw3cosVfm; _ga=GA1.2.1658888537.1681424304; _gid=GA1.2.1925596816.1681424304',
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

    proxy_list = [
        'http://196.17.66.143:8000', 'http://45.145.58.25:8000', 'http://45.155.201.162:8000'
    ]

    # choose random proxy
    proxy_url = random.choice(proxy_list)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        # browser = await p.chromium.launch(headless=False, proxy={
        #     "server": f"{proxy_url}",
        #     "username": "",
        #     "password": ""
        # })
        context = await browser.new_context()
        page = await context.new_page()
        await page.set_extra_http_headers(headers)
        await page.goto(url)
        content = await page.content()
        # with open('ththsThem.html', 'a') as f:
        #     f.write(content)


        await asyncio.sleep(1200000000)

        await browser.close()


asyncio.run(thath_them(first_name='Kwabena', middle_name='', last_name='Dwomoh', city='', state='NY'))