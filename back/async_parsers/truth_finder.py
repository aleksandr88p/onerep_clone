

from playwright.async_api import async_playwright
from bs4 import BeautifulSoup


async def truth_finder(*args, **kwargs):
    first_name = kwargs['first_name'].strip().replace(' ', '%20')
    middle_name = kwargs['middle_name'].strip().replace(' ', '%20')
    last_name = kwargs['last_name'].strip().replace(' ', '%20')
    state = kwargs['state'].strip().replace(' ', '%20')
    city = kwargs['city'].strip().replace(' ', '%20')

    params = {
        'firstName': f'{first_name}',
        'lastName': f'{last_name}',
        'state': f'{state}',
        'fromHome': 'true',
        'city': f'{city}',
        'previewSearchQuestion': 'true',
        'qLocation': 'false',
        'qRelatives': 'false',
        'qAgeRange': '',
        'noWait': 'false',
    }

    query_string = "&".join(f"{k}={v}" for k, v in params.items())
    url = f"https://www.truthfinder.com/results?{query_string}"
    # print(url)
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        headers = {
            'authority': 'www.truthfinder.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'cookie': 'PHPSESSID=k700a7lov8053dkdlkj9ecnpjj; device-id=8ec7de0e-fb17-4932-ab06-00ed3d6f2e9d; _gid=GA1.2.308751920.1681391888; _gcl_au=1.1.2006957507.1681391888; IR_gbd=truthfinder.com; 8a6efe92-fcd9-480e-acff-f2f45d79adc1_s=1681391888490-fed7-1bcb-3f933d661e66; 8a6efe92-fcd9-480e-acff-f2f45d79adc1_c=1681391888490-6e2e-cd61-cb67d84c06c3; 8a6efe92-fcd9-480e-acff-f2f45d79adc1_r=0.1099; IR_PI=a1f75efd-d9fd-11ed-9ef1-a1d11dcb1230%7C1681478288475; AMP_TOKEN=%24NOT_FOUND; ln_or=eyIzMjQ2NjgiOiJkIn0%3D; _pin_unauth=dWlkPU5EbGxaVEkzWmpNdFpXVmpZeTAwWm1NekxUa3hNakF0TUdKbVlqUmhPVE0xTm1Veg; __cf_bm=c36Igsv7eVwq.VDVxsntVnsQZcNFixGIu.N5e4Ta8as-1681391888-0-AYGKLMlujU3VJ0OhIwQYUhAn0AJbERjiUUOK+LkKnLBHzfVik3391zgs8Uq8Hb3v8UerLxNIUc6TDYhXChsjQOwH/AXJtzOKoQetYlND7CO9s9evU9MMxgFNdcRzROLvWHDdAdtKvmKApcvC0/5392iVVqOKpMqk3dOu1b1CBAsgVFIkXOnqZuL4H/zFq/dk4A==; outbrain_cid_fetch=true; __mmapiwsid=e421ca63-68d2-4440-8eb7-3dfb8ba9d72a:1141dce1d815ede100a046649c590ab2dbeba5fd; __ssid=eb23be0a14172e90e9c3decfdf5bb95; warningModalPopped=true; last-known-device-id=8ec7de0e-fb17-4932-ab06-00ed3d6f2e9d; IR_15694=1681391942560%7C0%7C1681391942560%7C%7C; _uetsid=a1eab470d9fd11eda118b96f89ea9ad3; _uetvid=a1eacc50d9fd11ed812d918632f163af; mouseOutModalPopped=true; _ga=GA1.2.1018641595.1681391888; _gat_UA-74882607-3=1; _ga_H5Z1GGC8S1=GS1.1.1681391888.1.1.1681391967.51.0.0',
            'dnt': '1',
            'referer': 'https://www.truthfinder.com/search?firstName=john&lastName=smith&state=NY&gender=male&fromHome=true',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        }

        await page.set_extra_http_headers(headers)
        response = await page.goto(url, timeout=1200000)

        content = await page.content()

        # f1 = open('truthFinder.html')
        # content = f1.read()
        soup = BeautifulSoup(content, 'html.parser')
        sections = soup.find('section', attrs={'id': 'people'})
        all_items = sections.find_all('div', attrs={'class': 'person'})
        mentions = []
        for item in all_items:
            try:
                name = item.find('h4', class_='link-name').text.strip()
                age = item.find('span', class_='display-age').text
                lived = []
                all_addr = item.find('li', class_="location result-item").find('ul').find_all('li', class_=lambda x: x != "include")
                for loc in all_addr:
                    lived.append(loc.text.strip())

                mentions.append({'name': name, 'age': age, 'lived': lived})
            except:
                print('error in item')




        # f1.close()

        # with open('truthFinder.html', 'a') as f:
        #     f.write(content)

        # await asyncio.sleep(300)
        await browser.close()
        return mentions








# import asyncio
# import json
# d = asyncio.run(truth_finder(first_name='john', middle_name='', last_name='jones', state='ny', city='new york'))
#
# print(json.dumps(d, indent=4))

