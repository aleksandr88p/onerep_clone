import json
import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

async def unmask(*args, **kwargs):
    first_name = kwargs["first_name"]
    middle_name = kwargs["middle_name"]
    last_name = kwargs["last_name"]
    city = kwargs["city"].strip()
    proxy = kwargs['proxy']

    if len(city.split(' ')) > 1:
        city = kwargs['city'].replace(' ', '_')
    elif len(city.split('-')) > 1:
        city = kwargs['city'].replace('-', '_')
    state = kwargs["state"]

    if state:
        if city:
            url = f'https://unmask.com/{first_name}-{last_name}/{state}-{city}'
        else:
            url = f'https://unmask.com/{first_name}-{last_name}/{state}/'
    else:
        url = f'https://unmask.com/{first_name}-{last_name}/'

    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=True)

        page = await browser.new_page()
        # Set user agent string
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
        }
        await page.set_extra_http_headers(headers)

        # Navigate to the URL
        await page.goto(url, timeout=1200000)

        # # Wait for page content to load
        # page.wait_for_selector(".person")

        # Get page content
        content = await page.content()

        # Parse HTML with BeautifulSoup
        soup = BeautifulSoup(content, "html.parser")

        all_items = soup.find_all("div", attrs={"class": "person"})
        mentions = []
        try:
            for num_, item in enumerate(all_items):
                name_age = item.find("h3", attrs={"itemprop": "name"})
                age = name_age.find("span")
                if age:
                    age = age.text
                    name = name_age.text.replace(age, "")
                    age = age.replace(",", "").strip()
                else:
                    name = name_age.text
                    age = ""

                lived = []

                try:
                    adresses = item.find_all(("a", "span"), attrs={"itemprop": "address"})
                    for address in adresses:
                        lived.append(address.text.strip())

                except Exception as ex:
                    print(f"error in address in information.com {ex}")
                mentions.append({"name": name, "age": age, "lived": lived})

        except Exception as e:
            print(f"error in item   {e}")

        await browser.close()

    # print(url)
    return mentions

#
# d = asyncio.run(unmask(first_name="billie", middle_name="", last_name="bones", state="", city=""))
# print(json.dumps(d, indent=4))
