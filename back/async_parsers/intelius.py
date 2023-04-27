

from playwright.async_api import async_playwright
from bs4 import BeautifulSoup


async def intelius(*args, **kwargs):
    first_name = kwargs["first_name"]
    middle_name = kwargs.get("middle_name", "")
    last_name = kwargs["last_name"]
    city = kwargs.get("city", "").strip().replace(" ", "-")
    state = kwargs.get("state", "")
    proxy = kwargs['proxy']

    if city == "":
        url = f"https://www.intelius.com/results/?firstName={first_name}&middleInitial={middle_name}&lastName={last_name}&state={state}"
    else:
        url = f"https://www.intelius.com/results/?firstName={first_name}&middleInitial={middle_name}&lastName={last_name}&city={city}&state={state}"

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(ignore_https_errors=True)

        page = await context.new_page()
        headers = {
            'authority': 'www.intelius.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en',
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
            "Referer": url,

        }

        await page.set_extra_http_headers(headers)

        await page.goto(url, timeout=1200000)

        html = await page.content()

        soup = BeautifulSoup(html, 'html.parser')
        section = soup.find('section', {'id': 'people'})
        all_items = section.find_all('div', {'class': 'person'})
        mentions = []
        for item in all_items:
            try:
                name = item.find('h4', class_='link-name').text.strip()
                try:
                    age = item.find('span', class_='display-age').text.strip()
                except:
                    age = ''
                lived = []
                try:
                    all_addr = item.find('li', attrs={'class': 'location'}).find_all('li')
                    for addr in all_addr:
                        if 'include' in addr.get('class', []):
                            pass
                        else:
                            lived.append(addr.text)
                except:
                    pass
                mentions.append({'name': name, 'age': age, 'lived': lived})
            except Exception as e:
                print(f'error in item intelius {e}')
        await browser.close()
        return mentions


# import asyncio
# import json
#
# d = asyncio.run(intelius(first_name="john", middle_name="", last_name="doe", city="new york", state="NY"))
#
# print(json.dumps(d, indent=4))
