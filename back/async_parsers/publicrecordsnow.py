"""
https://www.publicrecordsnow.com/name/Billie+Bones/eagle/ID/
https://www.publicrecordsnow.com/name/billie+bones/-none-/-none-/
"""
import json

import aiohttp
from bs4 import BeautifulSoup


async def publicrecordsnow(*args, **kwargs):
    first_name = kwargs["first_name"]
    middle_name = kwargs["middle_name"]
    last_name = kwargs["last_name"]
    city = kwargs["city"]
    state = kwargs["state"]
    cookies = {
        '_gcl_au': '1.1.1114480529.1678919287',
        '_gid': 'GA1.2.2058094499.1678919287',
        'session': 'eyJkZXZpY2UiOm51bGwsIm5ldHdvcmsiOm51bGwsInB1Ymxpc2hlciI6IlVOS05PV04ifQ.ZBRN2g.EbXVHxRVmOj_XDCcZf7h2R4Q9hA',
        '_uetsid': 'a8f18bf0c38011edafe069b492fb43e6',
        '_uetvid': 'a8f1e640c38011edaa2daba43c656837',
        '_ga': 'GA1.1.1972518481.1678919287',
        '_ga_M4X6ZNH0MB': 'GS1.1.1679051947.5.1.1679052256.0.0.0',
    }

    headers = {
        'authority': 'www.publicrecordsnow.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en',
        'cache-control': 'max-age=0',
        # 'cookie': '_gcl_au=1.1.1114480529.1678919287; _gid=GA1.2.2058094499.1678919287; session=eyJkZXZpY2UiOm51bGwsIm5ldHdvcmsiOm51bGwsInB1Ymxpc2hlciI6IlVOS05PV04ifQ.ZBRN2g.EbXVHxRVmOj_XDCcZf7h2R4Q9hA; _uetsid=a8f18bf0c38011edafe069b492fb43e6; _uetvid=a8f1e640c38011edaa2daba43c656837; _ga=GA1.1.1972518481.1678919287; _ga_M4X6ZNH0MB=GS1.1.1679051947.5.1.1679052256.0.0.0',
        'dnt': '1',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    }


    if state:
        if city:
            url = f'https://www.publicrecordsnow.com/name/{first_name}+{last_name}/{city}/{state}/'
        else:
            url = f'https://www.publicrecordsnow.com/name/{first_name}+{last_name}/-none-/{state}/'
    else:
        url = f'https://www.publicrecordsnow.com/name/{first_name}+{last_name}/-none-/-none-/'

    async with aiohttp.ClientSession(cookies=cookies, headers=headers) as session:
        async with session.get(url) as response:
            content = await response.text()
            soup = BeautifulSoup(content, 'html.parser')
            result_container = soup.find('div', attrs={'class': 'search-results-container'})
            all_div_res = result_container.find_all('div', attrs={'class': 'result'})
            mentions = []
            for num_, div_res in enumerate(all_div_res):
                num = num_ + 1
                name_age = div_res.find(attrs={'class': 'result-name'})
                name = name_age.find(attrs={"itemprop": "name"}).text.strip()
                age = name_age.text.replace(name, '').strip().replace('(', '').replace(')', '')

                lived = []
                try:
                    cur_address = div_res.find(attrs={'class': 'result-current-address'}).text
                    lived.append(cur_address)
                    all_address = div_res.find_all(attrs={'class': 'address'})
                    for address in all_address:
                        lived.append(address.text.strip())
                except:
                    continue
                mentions.append({'name': name, 'age': age, 'lived': lived})
            return mentions



import asyncio
# async def main():
#     mentions = await publicrecordsnow(first_name='billie', last_name='bones', middle_name='', state='', city='')
#     return mentions
#
# d = asyncio.run(main())
# print(json.dumps(d, indent=4))
# d = publicrecordsnow(first_name='billie', last_name='bones', middle_name='', state='', city='')
# # d = publicrecordsnow(first_name='billie', last_name='bones', middle_name='j', state='ID', city='eagle')
#
#
# print(json.dumps(d, indent=4))