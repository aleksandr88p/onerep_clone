import requests

cookies = {
    'PHPSESSID': 'nl6bgedr99v8010neg0fnjl9fs',
    'device-id': 'f261d09a-e4df-418c-9d76-bb120b649394',
    '_gid': 'GA1.2.22179741.1681403952',
    '_gcl_au': '1.1.82409429.1681403952',
    'IR_gbd': 'instantcheckmate.com',
    'AMP_TOKEN': '%24NOT_FOUND',
    '_pin_unauth': 'dWlkPVpEazVZakZqT0dZdE5ERmtOUzAwTkdGaExUaGlaRGt0WlRVMVl6ZGxZamN4T1RnMw',
    '_fbp': 'fb.1.1681403952231.1467720534',
    '__cf_bm': 'QY4JRoGECT4umflUFMXPXJR94g1FOL3JzUUnOS49xBE-1681403952-0-AUjJKsscQXQdUoJ69npYRYAEh34lcFt+BReK6RJwbNfTmcfx8BuD1H0Y8Uvz0ekaY5OUQwfyQ631zz+GJ0fZMM1eKsYO5yR0dyIcDVUbBEFeNqd1RC9gpg73i/5TDJpa9vAiUklk4Uawf53WlnhxqzWDPgoZDU/JHuGOAqRZyrZIxC9WAGjkh4347Rh6sobL0w==',
    'outbrain_cid_fetch': 'true',
    '__ssid': '2ffe95f98496edf1f97ee49cc4b1da7',
    '__mmapiwsid': 'bd85c08f-e49e-4593-a106-8591620d5230:075e7d8544840fbea2a3d2e8ef9169ae41654fd3',
    'last-known-device-id': 'f261d09a-e4df-418c-9d76-bb120b649394',
    'IR_PI': 'b8694ea6-da19-11ed-9ef1-a1d11dcb1230%7C1681490355771',
    'warningModalPopped': 'true',
    '_uetsid': 'b83d2240da1911eda637478c8ea6c400',
    '_uetvid': 'b83d53e0da1911ed9eb26536ce079ca4',
    'IR_15721': '1681404012736%7C0%7C1681404012736%7C%7C',
    '_ga': 'GA1.2.1710419069.1681403952',
    '_ga_HTDKQCCYPC': 'GS1.1.1681403951.1.1.1681404047.25.0.0',
}





# response = requests.get('https://www.instantcheckmate.com/results/', params=params, cookies=cookies, headers=headers)
# print(response.text)


from playwright.async_api import async_playwright
from bs4 import BeautifulSoup


async def instant_checkmate(*args, **kwargs):
    first_name = kwargs['first_name'].strip().replace(' ', '%20')
    middle_name = kwargs['middle_name'].strip().replace(' ', '%20')
    last_name = kwargs['last_name'].strip().replace(' ', '%20')
    state = kwargs['state'].strip().replace(' ', '%20')
    city = kwargs['city'].strip().replace(' ', '%20')
    proxy = kwargs['proxy']


    params = {
        'firstName': f'{first_name}',
        'lastName': f'{last_name}',
        'state': f'{state}',
        'city': f'{city}',
    }
    query_string = "&".join(f"{k}={v}" for k, v in params.items())

    url = f'https://www.instantcheckmate.com/results/?{query_string}'

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        headers = {
            'authority': 'www.instantcheckmate.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en',
            'cookie': 'PHPSESSID=nl6bgedr99v8010neg0fnjl9fs; device-id=f261d09a-e4df-418c-9d76-bb120b649394; _gid=GA1.2.22179741.1681403952; _gcl_au=1.1.82409429.1681403952; IR_gbd=instantcheckmate.com; AMP_TOKEN=%24NOT_FOUND; _pin_unauth=dWlkPVpEazVZakZqT0dZdE5ERmtOUzAwTkdGaExUaGlaRGt0WlRVMVl6ZGxZamN4T1RnMw; _fbp=fb.1.1681403952231.1467720534; __cf_bm=QY4JRoGECT4umflUFMXPXJR94g1FOL3JzUUnOS49xBE-1681403952-0-AUjJKsscQXQdUoJ69npYRYAEh34lcFt+BReK6RJwbNfTmcfx8BuD1H0Y8Uvz0ekaY5OUQwfyQ631zz+GJ0fZMM1eKsYO5yR0dyIcDVUbBEFeNqd1RC9gpg73i/5TDJpa9vAiUklk4Uawf53WlnhxqzWDPgoZDU/JHuGOAqRZyrZIxC9WAGjkh4347Rh6sobL0w==; outbrain_cid_fetch=true; __ssid=2ffe95f98496edf1f97ee49cc4b1da7; __mmapiwsid=bd85c08f-e49e-4593-a106-8591620d5230:075e7d8544840fbea2a3d2e8ef9169ae41654fd3; last-known-device-id=f261d09a-e4df-418c-9d76-bb120b649394; IR_PI=b8694ea6-da19-11ed-9ef1-a1d11dcb1230%7C1681490355771; warningModalPopped=true; _uetsid=b83d2240da1911eda637478c8ea6c400; _uetvid=b83d53e0da1911ed9eb26536ce079ca4; IR_15721=1681404012736%7C0%7C1681404012736%7C%7C; _ga=GA1.2.1710419069.1681403952; _ga_HTDKQCCYPC=GS1.1.1681403951.1.1.1681404047.25.0.0',
            'dnt': '1',
            'referer': 'https://www.instantcheckmate.com/search/?firstName=john&lastName=jones&state=NY',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        }

        await page.set_extra_http_headers(headers)
        response = await page.goto(url, timeout=1200000)

        content = await page.content()
        soup = BeautifulSoup(content, 'html.parser')
        sections = soup.find('section', attrs={'id': 'people'})
        all_items = sections.find_all('div', attrs={'class': 'person'})
        mentions = []
        for item in all_items:
            try:
                name = item.find('li', class_='category name').find('h4').text.strip()
                age = item.find('span', class_='display-age').text
                lived = []
                all_addr = item.find('li', class_="category location").find('ul', class_='desktop').find_all('li')
                for loc in all_addr:
                    lived.append(loc.text.strip())

                mentions.append({'name': name, 'age': age, 'lived': lived})
            except Exception as e:
                print(f'error in item instant checkmate\n{e}')

        await browser.close()
        return mentions


# import asyncio
#
# d = asyncio.run(instant_checkmate(first_name='William', middle_name='', last_name='jones', state='ny', city='new york'))
# import json
# print(json.dumps(d, indent=4))