import requests
import aiohttp
import asyncio
from helpers import states_dict



# response = requests.get('https://www.peekyou.com/usa/california/john_smith', cookies=cookies, headers=headers)
#
# print(response.text)



# async def fetch(session, url):
#     async with session.get(url) as response:
#         return await response.text()
#
# async def parse_page(page_num):
#     async with aiohttp.ClientSession() as session:
#         url = f'https://www.peekyou.com/usa/new_york/john_bloom/page={page_num}'
#         html = await fetch(session, url)
#         # здесь парсим страницу и извлекаем нужную информацию
#
# async def main():
#     tasks = []
#     async with aiohttp.ClientSession() as session:
#         # можно задать количество страниц, которые нужно спарсить
#         for page_num in range(1, 11):
#             task = asyncio.create_task(parse_page(page_num))
#             tasks.append(task)
#
#         await asyncio.gather(*tasks)
#
# if __name__ == '__main__':
#     asyncio.run(main())


async def peek_you(*args, **kwargs):
    first_name = kwargs["first_name"]
    middle_name = kwargs["middle_name"]
    last_name = kwargs["last_name"]
    city = kwargs["city"]
    state = kwargs["state"]

    if state:
        url = f"https://www.peekyou.com/usa/{states_dict[state].replace(' ','_')}/{first_name}_{last_name}/"
    else:
        url = f"https://www.peekyou.com/usa/{first_name}_{last_name}/"

    cookies = {
        'PHPSESSID': '73a65a4dc9c29657446d084515ebbea6',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'accept-language': 'en-US,en',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://www.peekyou.com/',
        # 'Cookie': 'PHPSESSID=73a65a4dc9c29657446d084515ebbea6',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    async with aiohttp.ClientSession(cookies=cookies, headers=headers) as session:

        async with session.get(url=url, ssl=False) as response:
            content = await response.text()
            with open('first_page.html', 'a') as f:
                f.write(content)



# asyncio.run(peek_you(first_name='john', last_name='smith', middle_name='', state='DC', city=''))