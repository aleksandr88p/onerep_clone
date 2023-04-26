import json
import time
from bs4 import BeautifulSoup
import asyncio
from playwright.async_api import async_playwright


async def spytox(*args, **kwargs):
    first_name = kwargs["first_name"]
    middle_name = kwargs["middle_name"]
    last_name = kwargs["last_name"]
    city = kwargs["city"].strip().replace(' ', '-')
    state = kwargs["state"]
    url = f'https://www.spytox.com/{first_name}-{last_name}'
    # print(state)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'accept-language': 'en-US,en',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            # 'Cookie': '_gcl_au=1.1.155407561.1682370117; spy_session=a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%229de5b52ab3011ef886d16d140dcabd19%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A11%3A%2262.4.55.242%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A78%3A%22Mozilla%2F5.0+%28X11%3B+Ubuntu%3B+Linux+x86_64%3B+rv%3A109.0%29+Gecko%2F20100101+Firefox%2F112.0%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1682370131%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7Dcfbbba0ed6a5fea2c0301a53df71ac033fca204d',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
        }

        page = await context.new_page()
        await page.set_extra_http_headers(headers)
        await page.goto(url)
        try:
            element_handle = await page.wait_for_selector(f'a[data-filter="{state}"]')
            await element_handle.click()
            print("state found")
        except:
            print("state not found")

        content = await page.content()
        soup = BeautifulSoup(content, 'html.parser')

        all_items = soup.find_all('div', class_='row single-person')
        mentions = []
        for item in all_items:
            try:
                if not item.get('style') or 'display: none;' not in item.get('style'):
                    name = item.find('div', attrs={'class': 'person'}).text.strip()
                    locations = item.find('div', attrs={'class': 'addresses'}).find_all('p')
                    age = ''
                    lived = []
                    for loc in locations:
                        loc = loc.text
                        if loc:
                            loc = loc.strip()
                            lived.append(loc)

                    mentions.append({'name': name, 'age': age, 'lived': lived})
            except:
                print('error in item')

        await context.close()
        return mentions







#
#
# d = asyncio.run(spytox(first_name='mark', middle_name='', last_name='smith', state='IL', city='new york'))
#
# print(json.dumps(d, indent=4))

