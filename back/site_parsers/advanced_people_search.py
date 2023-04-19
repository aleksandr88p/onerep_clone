import requests
from bs4 import BeautifulSoup


def advanced_people_search(*args, **kwargs):
    first_name = kwargs["first_name"]
    middle_name = kwargs["middle_name"]
    last_name = kwargs["last_name"]
    city = kwargs["city"]
    state = kwargs["state"]

    cookies = {
        'session': 'eyJkZXZpY2UiOm51bGwsIm5ldHdvcmsiOm51bGwsInB1Ymxpc2hlciI6IlVOS05PV04ifQ.ZBmrCQ.mCocEG23DKqjX8RozLf47kwIt-c',
        '_gcl_au': '1.1.642809030.1679403788',
        '_gid': 'GA1.2.79258065.1679403788',
        '_ga_XCR2KJWG9L': 'GS1.1.1679403788.1.0.1679403788.0.0.0',
        '_ga': 'GA1.1.371054973.1679403788',
        '_uetsid': 'ba06c3d0c7e811ed940483c0192aee4e',
        '_uetvid': 'ba06c200c7e811edbfde31025bced421',
        '__gads': 'ID=7dfb59f1caabb61b-22ba4fab5fdd000a:T=1679403788:RT=1679403788:S=ALNI_MZiwSZLqpx1zem13ktdaDVf2xBxhg',
        '__gpi': 'UID=00000bc9a6cc394d:T=1679403788:RT=1679403788:S=ALNI_MZ67htlG1SuWjQZ6HmdxIvGcLs6zQ',
    }

    headers = {
        'authority': 'www.advanced-people-search.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'session=eyJkZXZpY2UiOm51bGwsIm5ldHdvcmsiOm51bGwsInB1Ymxpc2hlciI6IlVOS05PV04ifQ.ZBmrCQ.mCocEG23DKqjX8RozLf47kwIt-c; _gcl_au=1.1.642809030.1679403788; _gid=GA1.2.79258065.1679403788; _ga_XCR2KJWG9L=GS1.1.1679403788.1.0.1679403788.0.0.0; _ga=GA1.1.371054973.1679403788; _uetsid=ba06c3d0c7e811ed940483c0192aee4e; _uetvid=ba06c200c7e811edbfde31025bced421; __gads=ID=7dfb59f1caabb61b-22ba4fab5fdd000a:T=1679403788:RT=1679403788:S=ALNI_MZiwSZLqpx1zem13ktdaDVf2xBxhg; __gpi=UID=00000bc9a6cc394d:T=1679403788:RT=1679403788:S=ALNI_MZ67htlG1SuWjQZ6HmdxIvGcLs6zQ',
        'dnt': '1',
        'origin': 'https://www.advanced-people-search.com',
        'referer': 'https://www.advanced-people-search.com/',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    }

    data = {
        'fn': f'{first_name}',
        'ln': f'{last_name}',
        'city': f'{city}',
        'state': f'{state}',
    }

    response = requests.post('https://www.advanced-people-search.com/people/name', cookies=cookies, headers=headers, data=data)

    # with open('result.html', 'a') as f:
    #     f.write(response.text)

    # f1 = open('result.html', 'r')
    # content = f1.read()

    content = response.text
    soup = BeautifulSoup(content, 'html.parser')

    all_items = soup.find_all('div', attrs={'class': 'result-content'})
    # mentions = {}
    mentions = []

    try:
        for num_, item in enumerate(all_items):
            name_age = item.find(attrs={'class': 'result-name'})
            name = name_age.find(attrs={"itemprop": "name"}).text.strip()
            age = name_age.text.replace(name, '').strip().replace('(', '').replace(')', '')

            lived = []
            try:
                cur_address = item.find(attrs={'class': 'result-current-address'}).text.strip()
                lived.append(cur_address)
                all_address = item.find_all(attrs={'class': 'address'})
                for address in all_address:
                    lived.append(address.text.strip())
            except:
                continue
            # mentions[num_ + 1] = {'name': name, 'age': age, 'lived': lived}
            mentions.append({'name': name, 'age': age, 'lived': lived})
    except Exception as e:
        print(f'error in item   {e}')

    # f1.close()

    return mentions


d = advanced_people_search(first_name='john', last_name='fisher', middle_name='', state='', city='')


import json

print(json.dumps(d, indent=4))