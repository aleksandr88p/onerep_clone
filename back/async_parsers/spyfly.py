import json
import time
from bs4 import BeautifulSoup
import aiohttp
import asyncio
from playwright.async_api import async_playwright
from _helpers import states_dict

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0',
    'Accept': '*/*',
    'accept-language': 'en-US,en',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.spyfly.com/people/ei',
    'Content-Type': 'application/json',
    'Origin': 'https://www.spyfly.com',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Cookie': 'AWSALB=oPBgphmbfynyW92lbv3DhBqB+U45mRXmWjShagrLaMmpkcjLObCvC39Iac8S/pKiMDlWuE2Uq7w/RYBtuYgbvp1uQseXWUUVi63N+wA52LCuKOY/Wi7mrmuGzc2H; AWSALBCORS=oPBgphmbfynyW92lbv3DhBqB+U45mRXmWjShagrLaMmpkcjLObCvC39Iac8S/pKiMDlWuE2Uq7w/RYBtuYgbvp1uQseXWUUVi63N+wA52LCuKOY/Wi7mrmuGzc2H; session.id=s%3ADX731uzfyJjhFsfpZmTsnLs_5qxNkUIV.yFlUo4wtEaeWFxHUmdA4vO3x0QIjQwzZdJZF7dpdnT8; __cf_bm=dMJ7hOFFFgTe8uANUTxCv1vhB366hWymZGojEsWimfM-1682450938-0-ARaTX6dG3AQ84Tw4eFUnBeuVLDGu2dehDzmwnPdY1tNrZGuiTfRrzTeBpNSwMa5Dr7Rj+IJSrGM8Dv+EgugludE=; _gcl_au=1.1.1419272521.1682450939; _ga_1V3X9VZS79=GS1.1.1682450939.1.0.1682451019.60.0.0; _ga=GA1.1.1690103156.1682450939',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}
async def send_post_request(*args, **kwargs):
    first_name = kwargs["first_name"]
    middle_name = kwargs["middle_name"]
    last_name = kwargs["last_name"]
    city = kwargs["city"]
    proxy = kwargs['proxy']

    # print(kwargs['state'])
    state = states_dict[kwargs["state"]]
    url = 'https://www.spyfly.com/people/api/saveSearch'
    json_data = {'dataBody': {'firstName': f'{first_name}', 'lastName': f'{last_name}', 'state': f'{state}', 'city': f'{city}', 'funnel': 'peopleSearch'}}
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.post(url, json=json_data) as response:
            data = await response.json()
            return data

async def spyfly(*args, **kwargs):
    first_name = kwargs["first_name"]
    middle_name = kwargs["middle_name"]
    last_name = kwargs["last_name"]
    city = kwargs["city"]
    state = kwargs["state"]
    response_data = await send_post_request(first_name=first_name, middle_name=middle_name,last_name=last_name, state=state, city=city)
    # print(response_data)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        url = 'https://www.spyfly.com/people/search'
        await page.set_extra_http_headers(headers)
        await page.goto(url, timeout=1200000)
        # await asyncio.sleep(6)
        html = await page.content()
        soup = BeautifulSoup(html, 'html.parser')

        all_items = soup.find_all('div', class_='result-item')
        mentions = []
        for item in all_items:
            try:
                name = item.find('h2').text
                age_raw = [p.text for p in item.find_all('p')]
                for i in age_raw:
                    if 'Age' in i:
                        age = i.replace('Age: ', '')
                        break
                    else:
                        age = ''

                location_list = []
                heads = item.find_all('p', class_='result-header')
                for head in heads:
                    if head.text.strip() == 'Location(s):':
                        location_list = [li.text.strip() for li in head.find_next_sibling('ul').find_all('li')]
                mentions.append({'name': name, 'age': age, 'lived': location_list})
            except:
                print('error in spyfly')

        return mentions


#
# d = asyncio.run(spyfly(first_name='mark', middle_name='',last_name='Smith', state='NY', city='new york'))
#
#
# print(json.dumps(d, indent=4))