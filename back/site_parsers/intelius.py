"""
https://www.intelius.com/results/?affid=1117&campid=3120&mdm=&mdm=&src=DIME&sid=www.peoplefinder.com&utm_source=DIME&utm_campaign=www.peoplefinder.com&utm_medium=&utm_content=&utm_term=&page=h&origin=icm&traffic%5Bsource%5D=DIME&traffic%5Bmedium%5D=&traffic%5Bcampaign%5D=%3Awww.peoplefinder.com&traffic%5Bterm%5D=&traffic%5Bcontent%5D=&s1=www.peoplefinder.com&s2=&s3=&s4=&s5=&traffic%5Bfunnel%5D=bg&traffic%5Bplacement%5D=&firstName=will&lastName=smitt&city=&state=ID&qLocation=false&qRelatives=false&qOver30=false"""


"""
ЭТОТ САЙТ НЕ ДОДЕЛАН
"""

import requests
from bs4 import BeautifulSoup


def intelius(*args, **kwargs):
    first_name = kwargs["first_name"]
    middle_name = kwargs["middle_name"]
    last_name = kwargs["last_name"]
    city = kwargs["city"]
    state = kwargs["state"]
    url = 'https://www.intelius.com/results/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/58.0.3029.110 Safari/537.3',
               }

    params = {
        'affid': '1117',
        'campid': '3120',
        'mdm': [
            '',
            '',
        ],
        'src': 'DIME',
        'sid': 'www.peoplefinder.com',
        'utm_source': 'DIME',
        'utm_campaign': 'www.peoplefinder.com',
        'utm_medium': '',
        'utm_content': '',
        'utm_term': '',
        'page': 'h',
        'origin': 'icm',
        'traffic[source]': 'DIME',
        'traffic[medium]': '',
        'traffic[campaign]': ':www.peoplefinder.com',
        'traffic[term]': '',
        'traffic[content]': '',
        's1': 'www.peoplefinder.com',
        's2': '',
        's3': '',
        's4': '',
        's5': '',
        'traffic[funnel]': 'bg',
        'traffic[placement]': '',
        'firstName': f'{first_name}',
        'lastName': f'{last_name}',
        'city': f'{city}',
        'state': f'{state}',
        'qLocation': 'false',
        'qRelatives': 'false',
        'qOver30': 'false',
    }
    cookies = {
        'PHPSESSID': 'akkshrbasgu50fk4mnuld9biqg',
        'device-id': '43ad0902-7261-4079-95d6-84117687ab2b',
        '_gcl_au': '1.1.1931433858.1679505960',
        '__cf_bm': 'OVpbQKoWRGqJIe33KY1TX4zC0pM3rJGpyv8wrXm7Y4g-1679505960-0-AUZ+mMSo4gufbsTVNxbbX+qSZNuesHaSlksbCSd3/g5b+YFjEJrKf4xTJ+ikrNF53rixQ/6YpOlHgGroEZ5bvHGfocx/hCbyYQ2njFo+jeeZkWGZYo7nHtXb2vu0Gb+F49n9BkAiYzfyiFGz6oaQoGHDOW3ppOflKD3g7zannJDW',
        'IR_gbd': 'intelius.com',
        'AMP_TOKEN': '%24NOT_FOUND',
        '_gid': 'GA1.2.10621052.1679505960',
        '_tt_enable_cookie': '1',
        '_ttp': '4kRh3a5Emox_HzmGIQs1EGOy_tl',
        'outbrain_cid_fetch': 'true',
        '__ssid': '73977a8f8c07b4626ba390c3fefc050',
        'last-known-device-id': '43ad0902-7261-4079-95d6-84117687ab2b',
        '_uetsid': '9cf6fcc0c8d611ed88495f09900581bf',
        '_uetvid': '9cf71ff0c8d611eda7a98dfd6768ae55',
        'IR_15720': '1679506050600%7C3642511%7C1679506050600%7C%7C',
        'IR_PI': '9d2271be-c8d6-11ed-b374-636268c2c298%7C1679592450600',
        '_ga_1N4R2NC6S0': 'GS1.1.1679505959.1.1.1679506050.60.0.0',
        '_ga': 'GA1.1.1740432874.1679505960',
        '__mmapiwsid': 'b3ddf424-41e7-47f7-8184-730f3ceeeef7:f8844f52603eb5d3115b6682fd2d5178d6f54880',
    }
    session = requests.Session()
    session.headers.update(headers)
    session.params.update(params)
    # Включаем поддержку cookies
    # session.cookies.update({'cookies_are': 'working'})
    session.cookies.update(cookies)
    # Включаем поддержку JavaScript
    response = session.get(url, headers=headers, verify=False, timeout=5, allow_redirects=True, stream=True)

    # with open('result.html', 'a') as f:
    #     f.write(response.text)

    # f1 = open('result.html', 'r')
    # content = f1.read()
    content = response.text

    soup = BeautifulSoup(content, 'html.parser')
    all_persons = soup.find_all('div', attrs={'class': 'person'})

    mentions = {}
    for num, person in enumerate(all_persons):
        try:
            name = person.find('h4', attrs={'class': 'link-name'}).text.strip()
            try:
                age = person.find('span', attrs={'class': 'display-age'}).text.strip()
            except:
                age = ''

            lived = []
            locs = person.find('li', class_='location').find('ul').find_all('li')
            for loc in locs:
                location = loc.text.strip()
                if 'Locations Include:' not in location:
                    lived.append(location)

            mentions[num + 1] = {'name': name, 'age': age, 'lived': lived}

        except Exception as ex:
            print(f'error in intelius {ex}')
            continue


    # f1.close()

    return mentions

import time

start_time = time.time()
d = intelius(first_name='billie', last_name='bones', middle_name='', city='', state='')

import json

print(json.dumps(d, indent=4))

end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")