"""
https://unmask.com/John-Doe/NY-New_York/
https://unmask.com/Matt-Jones/NY-New_York/
"""

import undetected_chromedriver as uc
from undetected_chromedriver.options import ChromeOptions
from bs4 import BeautifulSoup


def unmask(*args, **kwargs):
    '''

    :param args:
    :param kwargs:
    :return:
    '''
    first_name = kwargs["first_name"]
    middle_name = kwargs["middle_name"]
    last_name = kwargs["last_name"]
    city = kwargs["city"].strip()
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

    headers = {
        'authority': 'unmask.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'cache-control': 'max-age=0',
        # 'cookie': '__cf_bm=m27fQvDxdOF5GlMRP9VFh_xJpVPoLiZjHYSUvdttEdo-1680211249-0-Abkv7reVLWOdgL9cBk2IDy3HPyDcSR3ZuVZmquynOco0hOkpKBPKvV5cz9kmYUpm7ZzOP/GyFGVn7GIrmNPvS90=',
        'dnt': '1',
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

    options = ChromeOptions()
    headers_str = ""
    for key, value in headers.items():
        headers_str += "{}={}; ".format(key, value)
    headers_str = headers_str.strip()

    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    # options.add_argument(f"user-data-dir={chrome_data}")
    options.add_argument(f"--user-agent={headers_str}")


    driver = uc.Chrome(options=options)
    driver.get(url)
    # Получаем HTML-код страницы
    html = driver.page_source


    content = html
    soup = BeautifulSoup(content, 'html.parser')
    all_items = soup.find_all('div', attrs={"class": "person"})
    mentions = []
    try:
        for num_, item in enumerate(all_items):
            name_age = item.find('h3',attrs={'itemprop':"name"})
            age = name_age.find('span')
            if age:
                age = age.text
                name = name_age.text.replace(age, '')
                age = age.replace(',','').strip()
            else:
                name = name_age.text
                age = ''

            lived = []

            try:
                adresses = item.find_all(('a', 'span'), attrs={"itemprop": 'address'})
                for address in adresses:
                    # print(address.text)
                    lived.append(address.text.strip())

            except Exception as ex:
                print('error in address in information.com')
            mentions.append({'name': name, 'age': age, 'lived': lived})

    except Exception as e:
        print(f'error in item   {e}')

    print(url)
    driver.quit()
    return mentions




d = unmask(first_name='billie',middle_name='', last_name='bones', state='', city='')

import json

print(json.dumps(d, indent=4))