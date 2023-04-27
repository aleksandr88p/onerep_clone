import asyncio
import json
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

async def people_finders(*args, **kwargs):
    first_name = kwargs["first_name"]
    middle_name = kwargs["middle_name"]
    last_name = kwargs["last_name"]
    city = kwargs["city"].strip().replace(' ', '-')
    state = kwargs["state"]
    proxy = kwargs['proxy']

    if state:
        if city:
            url = f'https://www.peoplefinders.com/people/{first_name}-{last_name}/{state}/{city}'
        else:
            url = f'https://www.peoplefinders.com/people/{first_name}-{last_name}/{state}'
    else:
        url = f'https://www.peoplefinders.com/people/{first_name}-{last_name}'
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, proxy=proxy)
        context = await browser.new_context()
        page = await context.new_page()
        headers = {
            'authority': 'www.peoplefinders.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en',
            'cache-control': 'max-age=0',
            'cookie': '__cf_bm=gz7_zMgxOjvjaYKRBRvETMDSwUT_4a4b4pVZn8BBYWE-1681421612-0-AaZGvA14b57NHwjYnVSIrhThu0S5gbP89rWKrpQkhxg4GrkMD1+ga4Sn5JlLdYtup+00fGLEIF+oXxauaav77Pc=; _gcl_au=1.1.1713748018.1681421613; _conv_r=s%3Awww.google.com*m%3Aorganic*t%3A*c%3A; pf.browserid=04d0ba07-e018-4db4-8a0a-91529b9e2c18; pf.sessionid=CfDJ8M4fcUh5edFEqSHZs11%2B5TkgRh9I839Wg%2FHkWAQ9RLK%2FpvCfqWuDQx6SZstlp9NUlTPPjCBrhC1DUvSAWPXAejA9ayJmIlSwZisMxldVtCHmA85BgiK1ErWjiJlFYrz9NYP1g%2BktW5WHDhY4JcPtkQHjEEcEu3BbPY0snH8yQ2dR; _gid=GA1.2.868735270.1681421614; _hjFirstSeen=1; _hjIncludedInSessionSample_2798290=0; _hjSession_2798290=eyJpZCI6ImJiOGZmOTc0LTgzZjItNDBmOC04NTMxLTEzOGFjZjA5YTY5YyIsImNyZWF0ZWQiOjE2ODE0MjE2MTQ0NTYsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; rbuid=rbos-bd9878a3-523e-424f-a75e-4fc2f76be9d4; _uetsid=d7a7c110da4211eda9f883ac058d46f7; _uetvid=d7a7e500da4211edb72363cbc204efda; _hjSessionUser_2798290=eyJpZCI6IjZiYWE5M2VjLTBmNTctNWE0NC1iMWRkLTM3ZjAxMDQ3MTZlMCIsImNyZWF0ZWQiOjE2ODE0MjE2MTQ0NDksImV4aXN0aW5nIjp0cnVlfQ==; _conv_v=vi%3A1*sc%3A1*cs%3A1681421613*fs%3A1681421613*pv%3A2*exp%3A%7B100034396.%7Bv.1-g.%7B%7D%7D%7D; _conv_s=si%3A1*sh%3A1681421613389-0.5516426577442344*pv%3A2; __kla_id=eyIkcmVmZXJyZXIiOnsidHMiOjE2ODE0MjE2MTUsInZhbHVlIjoiaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8iLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cucGVvcGxlZmluZGVycy5jb20vIn0sIiRsYXN0X3JlZmVycmVyIjp7InRzIjoxNjgxNDIxNjM0LCJ2YWx1ZSI6Imh0dHBzOi8vd3d3Lmdvb2dsZS5jb20vIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LnBlb3BsZWZpbmRlcnMuY29tLyJ9fQ==; _ga=GA1.2.162153171.1681421614; _gat_UA-466999-1=1; _ga_EFQJT8231M=GS1.1.1681421613.1.1.1681421747.42.0.0',
            'referer': 'https://www.peoplefinders.com/',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        }

        await page.set_extra_http_headers(headers)
        await page.goto(url, timeout=1200000)
        html = await page.content()
        soup = BeautifulSoup(html, 'html.parser')
        all_items = soup.find_all('div', {"class": "record__data d-none d-lg-block pb-0"})
        mentions = []
        for item in all_items:
            try:
                name = item.find('h4', {"class": "record__title"}).text.strip()
                age = item.find('span', {"class": ['text-dark', 'text-secondary']}).text.strip()
                all_locations = item.find('div', {"class": 'col-lg-2 col-xl-3'}).find_all('li', {'class': 'text-dark'})
                lived = []
                for loc in all_locations:
                    lived.append(loc.text)
                mentions.append({'name': name, 'age': age, 'lived': lived})
            except:
                print('error in item')
        # await asyncio.sleep(300)
        await browser.close()
        return mentions




# d = asyncio.run(people_finders(first_name='billie', middle_name='', last_name='bones', state='ny', city='new york'))
# print(json.dumps(d, indent=4))