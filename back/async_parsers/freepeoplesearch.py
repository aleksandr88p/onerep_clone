
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

async def free_people_search(*args, **kwargs):
    first_name = kwargs["first_name"]
    middle_name = kwargs["middle_name"]
    last_name = kwargs["last_name"]
    city = kwargs["city"].replace(' ', '_').replace('-', '_')
    state = kwargs['state']
    proxy = kwargs['proxy']

    if state:
        if city:
            url = f'https://freepeoplesearch.com/{last_name}/{first_name}/{state}/{city}/'
        else:
            url = f'https://freepeoplesearch.com/{last_name}/{first_name}/{state}/'
    else:
        url = f'https://freepeoplesearch.com/{last_name}/{first_name}/'


    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, proxy=proxy)
        page = await browser.new_page()
        response = await page.goto(url, timeout=1200000)
        if response.status != 200:
            print('Page did not load in time')
        else:
            content = await page.content()
            soup = BeautifulSoup(content, 'html.parser')
            if soup.find('div', attrs={'class': 'tz-spinner'}):
                return None

            result_list = soup.find('div', attrs={'class': 'fp-seo-results__list'})
            all_items = result_list.find_all('div', attrs={'class': 'person'})

            mentions = []
            for item in all_items:
                try:
                    # contents[0] для извлечения первого элемента из списка дочерних элементов тега h2
                    name = item.find('h3', {'class': 'person__header-title'}).contents[0].strip()
                    info_str = item.find('span', attrs={'class': 'person__header-subtext'}).text.split('|')
                    lived = []
                    age = ''
                    if len(info_str) >= 2:
                        lived.append(info_str[0].strip())
                        age = info_str[1].replace('Age:', '').strip()
                    elif len(info_str) == 1:
                        lived.append(info_str[0].strip())
                    all_addreses = item.find_all('span', attrs={"itemprop": 'address'})
                    for adr in all_addreses:
                        lived.append(adr.text)
                    mentions.append({'name': name, 'age': age, 'lived': lived})
                except Exception as e:
                    print(f'error in item freepeoplesearch\n {e}')

            return mentions
        await browser.close()


# import asyncio
# #
# #
# import json
# #
# d = asyncio.run(free_people_search(first_name="john", middle_name="", last_name="doe", state="", city=""))
# print(json.dumps(d, indent=4))