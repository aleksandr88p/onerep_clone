import asyncio
import json
import time

from bs4 import BeautifulSoup
from playwright.async_api import async_playwright


async def usphonebook(*args, **kwargs):
    first_name = kwargs["first_name"]
    middle_name = kwargs["middle_name"]
    last_name = kwargs["last_name"]
    city = kwargs["city"].strip().replace(' ', '-')
    state = kwargs["state"]
    url = 'https://www.usphonebook.com/abraham-james/NY/new-york'
    if state:
        if city:
            url = f'https://www.usphonebook.com/{first_name}-{last_name}/{state}/{city}'
        else:
            url = f'https://www.usphonebook.com/{first_name}-{last_name}/{state}'
    else:
        url = f'https://www.usphonebook.com/{first_name}-{last_name}'
    # print(url)
    headers = {
        'authority': 'www.usphonebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en',
        'cache-control': 'max-age=0',
        # 'cookie': 'laravel_session=eyJpdiI6InJuV1hEN3U2bnkrc0hVWUlJcVh2eXc9PSIsInZhbHVlIjoiNDNlTXRjQ0hDV0lwditxcXc4RkwxWXozMDJIM1wvNDZPVDdSMHdmOG5YQWl0VXJPRFVlN2Q2aE15NUsxV0orOXoiLCJtYWMiOiIzZDM4OGY3NTVmMzIxZTU4YjJkZDk4M2NmYzhhOGFmYmVlYjMxODU0MDQ2YjQwZmRhNmMxOTBhOGEzZjBiNjI1In0%3D; AWSELB=4BFD87B90808B3DAE295A8DC419496EC6D4C647156ED203333B9B673C46A4C8A5B2C6B851F870AF168E34455A3B9ECF6520E09275189865A67700C3B85480870552B1A50D8; AWSELBCORS=4BFD87B90808B3DAE295A8DC419496EC6D4C647156ED203333B9B673C46A4C8A5B2C6B851F870AF168E34455A3B9ECF6520E09275189865A67700C3B85480870552B1A50D8; _uc_referrer=direct; _pbjs_userid_consent_data=3524755945110770; _gcl_au=1.1.1252226451.1682545895; _ga_PQPRV3Z7Y4=GS1.1.1682545895.1.0.1682545895.0.0.0; __gads=ID=e05beb4e2ed708e0-22b722c5addd003d:T=1682545895:RT=1682545895:S=ALNI_MYMuQvV47whsEYp0d_yvEOY3ogMeg; __gpi=UID=00000bf16421f8bf:T=1682545895:RT=1682545895:S=ALNI_MYWE-M-M4d6r1AV88gdVilBn-Q6Sg; _ga=GA1.2.1167812046.1682545895; _gid=GA1.2.964567644.1682545896; __cf_bm=waBOvvFYyDgDZ9VTLaFf2FUvE69GuENxug1S4xcYNfo-1682545895-0-Aa9a0Tsa2sDoMqck5/0i8QbnH3o75woIsPuKSfsS1X6O689vh4fUa3q1Kq3QTOfYyuyD6K96sEdV7G3Bh40YQX10L7y6MziepSGAu8463qNvbp9+r1fu9xoblui2dPETmpdG1WVw95Oo9psMkkl0NlI=; __qca=P0-92181284-1682545895307; _lr_retry_request=true; _lr_env_src_ats=false; pbjs_li_nonid=%7B%7D; cto_bundle=I0XL4F9XJTJCMTQ5ZGhUZURPZW4lMkYza3hhREd1TTlCaFFWVEslMkI4MXhHU1FuaG9tOGYlMkI4Qlg2YlJqY2xyU1dzeFBFNVh6UmZseFN2d1B6NiUyRlE5WU9OOFloZXNGeVZ2Q3l2Qmpaa3NZJTJCcktlSzVWRXlpSW43aGxONzVRRmNaVEVsV2ExNzZrMURoZ0ZUTGNiRGxiMDZhQW44Q1RLQmclM0QlM0Q',
        'pragma': 'no-cache',
        'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    }
    async with async_playwright() as p:
        try:
            browser = await p.chromium.launch(headless=True, proxy={
                "server": "http://45.155.201.162:8000",
                "username": "4UsLX7",
                "password": "tCDbq9"})
            context = await browser.new_context()
            page = await context.new_page()
            await page.set_extra_http_headers(headers)
            await page.goto(url, timeout=120000)
            html = await page.content()
            soup = BeautifulSoup(html, 'html.parser')
            all_items = soup.find_all('div', attrs={'class': 'success-wrapper-padding'})
            mentions = []
            for item in all_items:
                try:
                    name = item.find('span', attrs={'itemprop': 'name'}).text.strip()
                    age_raw = item.find('h3', attrs={'class': 'ls_number-text'})
                    try:
                        age = age_raw.text.replace(name, '').replace(', Age ', '').strip()
                    except:
                        age = ''

                    lived = []
                    try:
                        all_locs = item.find_all('span', attrs={'itemprop': 'address'})
                        for loc in all_locs:
                            lived.append(loc.text.strip())
                    except:
                        print()

                    mentions.append({'name': name, 'age': age, 'lived': lived})
                except Exception as e:
                    print(f'error in item usphonebook\n{e}')

            await context.close()
            return mentions
        except Exception as e:
            print(f'error in func usphonebook\n{e}')

#
# d = asyncio.run(usphonebook(first_name='abraham', middle_name='', last_name='james', state='NY', city='new york'))
#
# print(json.dumps(d, indent=4))
