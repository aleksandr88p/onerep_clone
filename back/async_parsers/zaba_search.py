import aiohttp
import asyncio
from bs4 import BeautifulSoup
import json

async def zaba_search(*args, **kwargs):
    first_name = kwargs["first_name"]
    middle_name = kwargs["middle_name"]
    last_name = kwargs["last_name"]
    city = kwargs["city"].replace(' ', '+').replace('-', "+")
    state = kwargs["state"]
    proxy = kwargs['proxy']

    if state:
        if city:
            url = f'https://www.zabasearch.com/people/{first_name}+{last_name}/{city}+{state}/'
        else:
            url = f'https://www.zabasearch.com/people/{first_name}+{last_name}/{state}/'
    else:
        url = f'https://www.zabasearch.com/people/{first_name}+{last_name}/'


    cookies = {
        'PHPSESSID': 'j8mkri3kk8arsq9tsst2tkb30l',
        'device-id': 'e8e617ee-102f-42fc-99ae-94aa5b97131e',
        '_ga': 'GA1.2.1213594622.1681475669',
        '_gid': 'GA1.2.1621328356.1681475669',
        '__gpi': 'UID=00000bd55947bc6e:T=1681475670:RT=1681475670:S=ALNI_MZqoRUrud2yCv33OFgYc3ZhiBAbYw',
        '__gads': 'ID=082fd689b7400995-22390c5291dd0079:T=1681475670:S=ALNI_MYZS_UX62ugor7wp3UWmJtKpUt_lw',
    }

    headers = {
        'authority': 'www.zabasearch.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en',
        'cache-control': 'max-age=0',
        # 'cookie': 'PHPSESSID=j8mkri3kk8arsq9tsst2tkb30l; device-id=e8e617ee-102f-42fc-99ae-94aa5b97131e; _ga=GA1.2.1213594622.1681475669; _gid=GA1.2.1621328356.1681475669; __gpi=UID=00000bd55947bc6e:T=1681475670:RT=1681475670:S=ALNI_MZqoRUrud2yCv33OFgYc3ZhiBAbYw; __gads=ID=082fd689b7400995-22390c5291dd0079:T=1681475670:S=ALNI_MYZS_UX62ugor7wp3UWmJtKpUt_lw',
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

    async with aiohttp.ClientSession(cookies=cookies, headers=headers) as session:
        async with session.get(url) as response:
            content = await response.text()

            soup = BeautifulSoup(content, 'html.parser')
            mentions = []
            all_items = soup.find_all('section', {'class': 'person people-results resultsbox'})
            for item in all_items:
                try:
                    name = item.find('h2').text.strip()
                    age = 'no'
                    all_p = item.find_all('p')
                    for p in all_p:
                        if 'Age' in p.text:
                            age = p.text.split(":")[1].strip()
                    addres = item.find('script')
                    json_data = json.loads(addres.text)
                    try:
                        loc_str = f"{json_data['address']['addressLocality']}, {json_data['address']['addressRegion']}, {json_data['address']['streetAddress']}, {json_data['address']['postalCode']}"
                    except:
                        loc_str = 'no'

                    mentions.append({'name': name, 'age': age, 'lived': [loc_str]})
                except Exception as e:
                    print(f'error in item {e}')

            return mentions



# d = asyncio.run(zaba_search(first_name='John', middle_name='', last_name='smith', city='chicago', state='il'))
#
# print(json.dumps(d, indent=4))