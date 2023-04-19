"""https://www.fastpeoplesearch.com/name/john-doe_port-jefferson-station-ny"""
import time

import undetected_chromedriver as uc
from undetected_chromedriver.options import ChromeOptions

from bs4 import BeautifulSoup




def fast_people_search(*args, **kwargs):
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
        city = kwargs['city'].replace(' ', '-')
    state = kwargs["state"]

    if state:
        if city:
            url = f'https://www.fastpeoplesearch.com/name/{first_name}-{last_name}_{city}-{state}'
        else:
            url = f'https://www.fastpeoplesearch.com/name/{first_name}-{last_name}_{state}'
    else:
        url = f'https://www.fastpeoplesearch.com/name/{first_name}-{last_name}'

    PROXY_HOST = '45.145.58.25'
    PROXY_PORT = '8000'
    PROXY_USERNAME = '4UsLX7'
    PROXY_PASSWORD = 'tCDbq9'

    headers = {
        'authority': 'www.fastpeoplesearch.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
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


    options = ChromeOptions()
    headers_str = ""
    for key, value in headers.items():
        headers_str += f"{key}={value}; "

    headers_str = headers_str.strip()

    # options.add_argument(f'--proxy-server=http://{PROXY_USERNAME}:{PROXY_PASSWORD}@{PROXY_HOST}:{PROXY_PORT}')
    options.add_argument(f'--proxy-server={PROXY_HOST}:{PROXY_PORT}')
    # options.add_argument(f'--proxy-auth={PROXY_USERNAME}:{PROXY_PASSWORD}')
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
    # time.sleep(20)

    # with open('result.html', 'a') as f:
    #     f.write(html)

    # f1 = open('result.html', 'r')

    # html = f1.read()
    soup = BeautifulSoup(html, 'html.parser')

    all_items = soup.find_all('div', attrs={"class": "card-block"})
    mentions = []
    try:
        for item in all_items:
            age_element = item.find('h3', string='Age:')
            age = age_element.next_sibling.strip()

            full_name_element = item.find('h3', string='Full Name:')
            name = full_name_element.next_sibling.strip()

            lived = []

            try:
                first_adr = item.find("div", {'style': 'line-height:20px;margin-bottom:15px'}).text.replace('\n', ' ').strip()
                lived.append(first_adr)
                all_addr = item.find('div', {'class': 'row'}).find_all('a')
                for addr in all_addr:
                    lived.append(addr.text.replace('\n', ' ').strip())
            except Exception as ex:
                print(f'error in address in fastpeoplesearch.com {ex}')

            mentions.append({'name': name, 'age': age, 'lived': lived})
            # print(name, age)
            # print(lived)

    except Exception as e:
        print(f'error in item   {e}')
    print(url)

    # f1.close()
    driver.quit()

    return mentions

d =fast_people_search(first_name='aleks', middle_name='', last_name='brandt', state='NY', city='')
# d = fast_people_search(first_name='john', middle_name='', last_name='doe', state='NY', city='port-jefferson-station')


import json

print(json.dumps(d, indent=4))