"""
https://www.privateeye.com/people/Billie+Bones/eagle/ID/
https://www.privateeye.com/people/billie+bones/-none-/
https://www.privateeye.com/people/billie+bones/-none/NY/
"""
import aiohttp
from bs4 import BeautifulSoup
import json
async def privateeye(*args, **kwargs):
    first_name = kwargs["first_name"]
    middle_name = kwargs["middle_name"]
    last_name = kwargs["last_name"]
    city = kwargs["city"].replace(' ', '%20')
    state = kwargs["state"]
    cookies = {
        'session': 'eyJkZXZpY2UiOm51bGwsIm5ldHdvcmsiOm51bGwsInB1Ymxpc2hlciI6IlVOS05PV04ifQ.ZBWNpg.wcMekd7dg7SjsRSi7jBI0g_o8sY',
        '_gcl_au': '1.1.1253534278.1679134119',
        '_ga_0EV8KB0TJ4': 'GS1.1.1679134119.1.0.1679134119.0.0.0',
        '_ga': 'GA1.2.1870299248.1679134119',
        '_gid': 'GA1.2.824756526.1679134120',
        '_gat_UA-37474269-1': '1',
        '_gat_gtag_UA_37474269_1': '1',
        '_uetsid': 'dac11d50c57411ed975083dd0ccdc079',
        '_uetvid': 'dac12ce0c57411ed8aa32d0a6a4beb13',
        '__gads': 'ID=ccfb983258bbb502-22fd8390d8de008b:T=1679134119:RT=1679134119:S=ALNI_MYSyBDkH6DRNmhLHCRP828R3Ve8jA',
        '__gpi': 'UID=00000a2d646dfe14:T=1679134119:RT=1679134119:S=ALNI_MbIvFG0Ln_U2a2TqVSIh8z0xLh_Mw',
    }

    headers = {
        'authority': 'www.privateeye.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en',
        'cache-control': 'max-age=0',
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

    url = f'https://www.privateeye.com/people/{first_name}+{last_name}/'
    if not city:
        if not state:
            url = f'{url}-none-/'
        else:
            url = f'{url}-none-/{state}/'
    else:
        url = f"{url}{city}/{state}/"

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
            cur_address = div_res.find(attrs={'class': 'result-current-address'}).text.strip()
            lived.append(cur_address)
            all_address = div_res.find_all(attrs={'class': 'address'})
            for address in all_address:
                lived.append(address.text.strip())
        except:
            continue
        mentions.append({'name': name, 'age': age, 'lived': lived})

    return mentions

#
import asyncio

# async def main():
#     mentions = await privateeye(first_name='billie', last_name='bones', middle_name='j', state='NY', city='new york')
#     print(json.dumps(mentions, indent=4))
#
# asyncio.run(main())