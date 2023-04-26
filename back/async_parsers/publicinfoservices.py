import time


import asyncio
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

async def publicinfoservices(*args, **kwargs):
    first_name = kwargs["first_name"]
    middle_name = kwargs["middle_name"]
    last_name = kwargs["last_name"]
    city = kwargs["city"].strip().replace(' ', '-')
    state = kwargs["state"]

    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context()
            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0',
                'Accept': '*/*',
                'accept-language': 'en-US,en',
                'Referer': 'https://www.publicinfoservices.com/r/search',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Origin': 'https://www.publicinfoservices.com',
            }

            page = await context.new_page()
            await page.set_extra_http_headers(headers)
            await page.goto(url='https://www.publicinfoservices.com/r/search#', timeout=120000)

            # Заполнение поля First Name
            await page.fill('#no-first-name-search', first_name)

            # Заполнение поля Last Name
            await page.fill('#no-last-name-search', last_name)

            # Выбор значения в выпадающем списке Select State
            await page.select_option('#no-results-states', value=state)

            # Ожидание 1 секунд, чтобы увидеть результаты заполнения
            await asyncio.sleep(1)

            await page.click('a.update-results')

            try:
                # await page.waitForSelector('#congrats-button', timeout=5000)
                await page.click('#congrats-button')
            except Exception as e:
                print(f'Кнопка "Continue" не найдена на странице\n{e}')
                await browser.close()
                return

            content = await page.content()

            soup = BeautifulSoup(content, 'html.parser')
            all_item = soup.find('tbody', attrs={'id': 'table-body'}).find_all('tr')
            mentions = []

            for item in all_item:
                try:
                    all_info = item.find_all('td')
                    name = item.find('h5', attrs={'class': 'text-sm blue bold mb-0'}).text
                    age_row = all_info[1].text
                    if age_row.isdigit():
                        age = age_row
                    else:
                        age = ''
                    lived = []
                    try:
                        places = all_info[2]
                        for loc in places.find_all('br'):
                            location_text = loc.previous_sibling.strip()
                            lived.append(location_text)
                    except:
                        continue

                    mentions.append({'name': name, 'age': age, 'lived': lived})

                except Exception as e:
                    print(f'error in item publicinfoservices\n{e}')
            # time.sleep(60000)
            await context.close()
            return mentions
    except Exception as e:
        print(f'error in publicinfoservices\n{e}')
#
# d = asyncio.run(publicinfoservices(first_name='billie', middle_name='', last_name='bones', state='NY', city='new york'))
#
# import json
# print(json.dumps(d, indent=4))