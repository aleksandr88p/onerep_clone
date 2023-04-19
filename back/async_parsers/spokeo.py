"""
имя-фамилия/штат/город
https://www.spokeo.com/Will-Smitt/Alabama/Calera

https://www.spokeo.com/Will-Smitt
"""
import aiohttp
import asyncio
import json
from bs4 import BeautifulSoup


async def spokeo(*args, **kwargs):
    first_name = kwargs["first_name"]
    middle_name = kwargs["middle_name"]
    last_name = kwargs["last_name"]
    city = kwargs["city"]
    state = kwargs["state"]
    if state:
        if city:
            url = f"https://www.spokeo.com/{first_name}-{last_name}/{state}/{city}"
        else:
            url = f"https://www.spokeo.com/{first_name}-{last_name}/{state}"
    else:
        url = f"https://www.spokeo.com/{first_name}-{last_name}"
    # print(url)

    cookies = {
        '_sp_ses.6a20': '*',
        '_sp_id_temp': '089134e0-637e-4fa6-a4f4-a53eaa7616ee',
        '_sp_ses_temp': 'd5ab5ad2-6fff-4a6f-9208-240ce99b3827',
        'full_story_gtm': 'false',
        'sem': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJnIjoibmFtZV9kaXJlY3RfY2l0eV9jb250cm9sX2Vtb2ppIiwic2VtRmxvdyI6IkgxMDAwUzEwMDBQMTAyMyJ9.vGOK2MvEbzxZkKBnNslrnoCkjc9u_8CxdHgRO84wgUg',
        'campaigns_list': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ2YWx1ZSI6Im5hbWVfZGlyZWN0X2NpdHlfY29udHJvbF9lbW9qaSJ9.KGiH4bw7JggqDWCHNt9K5pdo9rT3m6WatnV_2HH4wz0',
        'campaign_regex': '.*name_direct.*',
        'first_visit_date': '2023-03-18+00%3A00%3A00+%2B0000',
        'a': '%5E%5E%5E%5E%5E%5Ename_direct_city_control_emoji%5E%5E1679155555',
        'spokeo_sessions_rails4': 'fe4dcb7ce664264a01b539359a056969',
        '_ga': 'GA1.2.1836784831.1679155556',
        '_gid': 'GA1.2.617100643.1679155556',
        '_gcl_au': '1.1.670419546.1679155557',
        '_fbp': 'fb.1.1679155557404.632301235',
        'last_campaign_tstamp': '1679155917',
        'insights': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJnYV9jYW1wYWlnbl92aXNpdCI6Im5hbWVfZGlyZWN0X2NpdHlfY29udHJvbF9lbW9qaSIsImdhX3NlbV9mbG93X3Zpc2l0IjoiSDEwMDBTMTAwMFAxMDIzIiwiZ2FfY2FtcGFpZ25fc2Vzc2lvbl9hdHRyIjoibmFtZV9kaXJlY3RfY2l0eV9jb250cm9sX2Vtb2ppIiwiZ2FfdXNlcnR5cGVfcGFnZSI6IkZyZWUiLCJwYWdlX3ZpZXdfaWQiOiJlMGQxZDk2NC0xYWI0LTQzZDgtYWJiNS00MGZjYjdmNzAyMzkiLCJyZXFfaG9zdCI6Ind3dy5zcG9rZW8uY29tIiwiZ2Ffc2ltcGxlX3Rlc3RfZ3JvdXAiOiIifQ.O3XSt1KmFosyAabH963ZfrDkDFHYIBTWpWxFszzqRAE',
        'page_view_id_refresh': 'true',
        'current_url': f'{url}',
        'current_page_url': f'{url}',
        '_gat_Insights': '1',
        '_gat_UA-46050535-2': '1',
        'previous_page_url': f'{url}',
        'referrer_url': f'{url}',
        '_sp_id.6a20': '38f236a9-0e94-49c8-a1a3-ff4b422203af.1679155555.1.1679156227.1679155555.feb1c966-75b2-49f7-bab2-849f733c99de',
    }

    headers = {
        'authority': 'www.spokeo.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en',
        # 'cookie': '_sp_ses.6a20=*; _sp_id_temp=089134e0-637e-4fa6-a4f4-a53eaa7616ee; _sp_ses_temp=d5ab5ad2-6fff-4a6f-9208-240ce99b3827; full_story_gtm=false; sem=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJnIjoibmFtZV9kaXJlY3RfY2l0eV9jb250cm9sX2Vtb2ppIiwic2VtRmxvdyI6IkgxMDAwUzEwMDBQMTAyMyJ9.vGOK2MvEbzxZkKBnNslrnoCkjc9u_8CxdHgRO84wgUg; campaigns_list=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ2YWx1ZSI6Im5hbWVfZGlyZWN0X2NpdHlfY29udHJvbF9lbW9qaSJ9.KGiH4bw7JggqDWCHNt9K5pdo9rT3m6WatnV_2HH4wz0; campaign_regex=.*name_direct.*; first_visit_date=2023-03-18+00%3A00%3A00+%2B0000; a=%5E%5E%5E%5E%5E%5Ename_direct_city_control_emoji%5E%5E1679155555; spokeo_sessions_rails4=fe4dcb7ce664264a01b539359a056969; _ga=GA1.2.1836784831.1679155556; _gid=GA1.2.617100643.1679155556; _gcl_au=1.1.670419546.1679155557; _fbp=fb.1.1679155557404.632301235; last_campaign_tstamp=1679155917; insights=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJnYV9jYW1wYWlnbl92aXNpdCI6Im5hbWVfZGlyZWN0X2NpdHlfY29udHJvbF9lbW9qaSIsImdhX3NlbV9mbG93X3Zpc2l0IjoiSDEwMDBTMTAwMFAxMDIzIiwiZ2FfY2FtcGFpZ25fc2Vzc2lvbl9hdHRyIjoibmFtZV9kaXJlY3RfY2l0eV9jb250cm9sX2Vtb2ppIiwiZ2FfdXNlcnR5cGVfcGFnZSI6IkZyZWUiLCJwYWdlX3ZpZXdfaWQiOiJlMGQxZDk2NC0xYWI0LTQzZDgtYWJiNS00MGZjYjdmNzAyMzkiLCJyZXFfaG9zdCI6Ind3dy5zcG9rZW8uY29tIiwiZ2Ffc2ltcGxlX3Rlc3RfZ3JvdXAiOiIifQ.O3XSt1KmFosyAabH963ZfrDkDFHYIBTWpWxFszzqRAE; page_view_id_refresh=true; current_url=https://www.spokeo.com/Will-Smitt/-none-/-none-; current_page_url=https://www.spokeo.com/Will-Smitt/-none-/-none-; _gat_Insights=1; _gat_UA-46050535-2=1; previous_page_url=https://www.spokeo.com/Will-Smitt/-none-/-none-; referrer_url=https://www.spokeo.com/Will-Smitt/-none-/-none-; _sp_id.6a20=38f236a9-0e94-49c8-a1a3-ff4b422203af.1679155555.1.1679156227.1679155555.feb1c966-75b2-49f7-bab2-849f733c99de',
        'dnt': '1',
        'if-none-match': 'W/"a05d1a352cadecee1571eeeb7fa18728"',
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

    async with aiohttp.ClientSession(headers=headers, cookies=cookies) as session:
        async with session.get(url) as response:
            content = await response.text()
            soup = BeautifulSoup(content, 'html.parser')
            all_item = soup.find_all('div', attrs={"class": 'single-column-list-item'})
            mentions = []
            for num_, item in enumerate(all_item):
                num = num_ + 1
                all_divs = item.find_all('div')
                name_age = all_divs[0].find('a').text.split(',')
                name = name_age[0]
                try:
                    age = name_age[1].strip()
                except IndexError:
                    age = None
                lived = [all_divs[1].text.replace('Resides in', '').strip()]
                other_places = all_divs[2].text
                try:
                    if 'Lived In' in other_places:
                        other_places = other_places.replace('Lived In', '').split(',')
                        for place in other_places:
                            lived.append(place.strip())
                except:
                    continue
                mentions.append({'name': name, 'age': age, 'lived': lived})
            return mentions



# import asyncio
# async def main():
#     mentions = await spokeo(first_name='billie', last_name='bones', middle_name='', state='', city='')
#     return mentions
#
# d = asyncio.run(main())
# print(json.dumps(d, indent=4))