import json
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
import asyncio

async def information_com(*args, **kwargs):
    first_name = kwargs["first_name"]
    middle_name = kwargs["middle_name"]
    last_name = kwargs["last_name"]
    city = kwargs["city"].strip()
    if len(city.split(' ')) > 1:
        city = kwargs['city'].replace(' ', '-')
    state = kwargs["state"]
    proxy = kwargs['proxy']


    if state:
        if city:
            url = f'https://information.com/people/{first_name}-{last_name}/{state}/{city}'
        else:
            url = f'https://information.com/people/{first_name}-{last_name}/{state}/'
    else:
        url = f'https://information.com/people/{first_name}-{last_name}/'

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Emulate a desktop browser to avoid mobile site rendering
        context = await browser.new_context(
            **{"viewport": {"width": 1920, "height": 1080}}
        )
        page = await context.new_page()

        # Set the user agent
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        }
        await page.set_extra_http_headers(headers)

        # Navigate to the URL
        await page.goto(url, timeout=1200000)

        # Wait for page content to load
        await page.wait_for_selector(".person")

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
                    adresses = item.find_all("span", attrs={"itemprop": "address"})
                    for address in adresses:
                        lived.append(address.text.strip())

                except Exception as ex:
                    print(f"error in address in information.com {ex}")
                mentions.append({"name": name, "age": age, "lived": lived})

        except Exception as e:
            print(f"error in item information.com\n{e}")

        await browser.close()
    return mentions


# async def run_async():
#     d = await information_com(first_name="nora", middle_name="", last_name="amezcua", state="", city="")
#     print(json.dumps(d, indent=4))
#
# asyncio.run(run_async())
