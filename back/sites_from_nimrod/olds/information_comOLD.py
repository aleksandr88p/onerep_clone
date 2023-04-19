import requests
from requests_html import HTMLSession
import undetected_chromedriver as uc
from undetected_chromedriver.options import ChromeOptions
from bs4 import BeautifulSoup


def information_com(*args, **kwargs):
    first_name = kwargs["first_name"]
    middle_name = kwargs["middle_name"]
    last_name = kwargs["last_name"]
    city = kwargs["city"].strip()
    if len(city.split(' ')) > 1:
        city = kwargs['city'].replace(' ', '-')
    state = kwargs["state"]

    cookies = {
        '__cf_bm': 'L_Y3lZEB.C16PtqBtObMFJmYgUeClXNL7ih972VyJog-1680076586-0-AQ7VVUYHOTJPpQkYvEv8j+iBkG/rmQqwkz8YBytRwjYMwSLaqhb6pwDuVw3D/HWlKXFikNTWQ5e5aueKfjqGHTQ=',
    }

    headers = {
        'authority': 'information.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        "Accept-Language": "en-US,en;q=0.9",
        # 'cookie': '__cf_bm=L_Y3lZEB.C16PtqBtObMFJmYgUeClXNL7ih972VyJog-1680076586-0-AQ7VVUYHOTJPpQkYvEv8j+iBkG/rmQqwkz8YBytRwjYMwSLaqhb6pwDuVw3D/HWlKXFikNTWQ5e5aueKfjqGHTQ=',
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
        headers_str += "{}={}; ".format(key, value)
    headers_str = headers_str.strip()

    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    # options.add_argument(f"user-data-dir={chrome_data}")
    options.add_argument(f"--user-agent={headers_str}")

    # chrome_version = '111.0.5563.110'
    # options.add_argument(f'--version={chrome_version}')

    if state:
        if city:
            url = f'https://information.com/people/{first_name}-{last_name}/{state}/{city}'
        else:
            url = f'https://information.com/people/{first_name}-{last_name}/{state}/'
    else:
        url = f'https://information.com/people/{first_name}-{last_name}/'
    driver = uc.Chrome(options=options)

    driver.get(url)

    # Получаем HTML-код страницы
    html = driver.page_source

    # with open('result.html', 'a') as f:
    #     f.write(html)

    # f1 = open("result.html", 'r')

    content = html

    soup = BeautifulSoup(content, 'html.parser')

    all_items = soup.find_all('div', attrs={"class": "person"})
    mentions = []
    try:
        for num_, item in enumerate(all_items):
            name_age = item.find('h3', attrs={'itemprop': "name"})
            age = name_age.find('span')
            if age:
                age = age.text
                name = name_age.text.replace(age, '')
                age = age.replace(',', '').strip()
            else:
                name = name_age.text
                age = ''

            lived = []

            try:
                adresses = item.find_all('span', attrs={"itemprop": 'address'})
                for address in adresses:
                    lived.append(address.text.strip())

            except Exception as ex:
                print(f'error in address in information.com {ex}')
            mentions.append({'name': name, 'age': age, 'lived': lived})

    except Exception as e:
        print(f'error in item   {e}')

    # f1.close()
    driver.quit()
    print(url)
    return mentions


d = information_com(first_name='billie', middle_name='', last_name='bones', state='', city='')
import json

print(json.dumps(d, indent=4))

