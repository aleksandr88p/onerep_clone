import requests
from bs4 import BeautifulSoup

def a411locate(name, surename):


    cookies = {
        '_pbjs_userid_consent_data': '3524755945110770',
        '_ga': 'GA1.1.2048302641.1679331960',
        '__gads': 'ID=222dc16cdb5144a2:T=1679331959:S=ALNI_MZSFPZxwxjtwTAi7viTBX3eTTcO_Q',
        '__gpi': 'UID=00000bf11b977bbd:T=1679331959:RT=1679331959:S=ALNI_Ma52cfCbZlUeeBOlLU14fmkgMrz5Q',
        '_ga_MDWVDXGLSM': 'GS1.1.1679331959.1.1.1679331992.0.0.0',
    }

    headers = {
        'authority': 'www.411locate.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru',
        # 'cookie': '_pbjs_userid_consent_data=3524755945110770; _ga=GA1.1.2048302641.1679331960; __gads=ID=222dc16cdb5144a2:T=1679331959:S=ALNI_MZSFPZxwxjtwTAi7viTBX3eTTcO_Q; __gpi=UID=00000bf11b977bbd:T=1679331959:RT=1679331959:S=ALNI_Ma52cfCbZlUeeBOlLU14fmkgMrz5Q; _ga_MDWVDXGLSM=GS1.1.1679331959.1.1.1679331992.0.0.0',
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

    response = requests.get(f'https://www.411locate.com/people-search/full/{name}-{surename}', cookies=cookies, headers=headers)

    # with open('result.html', 'a') as f:
    #     f.write(response.text)
    # f1 = open('result.html', 'r')
    # content = f1.read()

    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    all_items = soup.find_all('div',
                                 attrs={'class': 'bg-blue text-backgroundColor rounded-[20px] drop-shadow-normal'})
    # print(len(all_items))

    mentions = {}
    for num_, item in enumerate(all_items):
        try:

            name = item.find('div', attrs={'class': 'flex justify-between px-2 sm:px-4 py-3 md:px-10 md:py-6'}).find('span').text
            items_needed = item.find_all('div', attrs={"class": 'flex flex-col items-start sm:flex-row gap-x-3 gap-y-1'})
            age = items_needed[1].text
            lived = [items_needed[0].text]

            try:
                all_places = [place.text.replace('/', '') for place in items_needed[2].find_all('p')]

            except:
                continue

            mentions[num_+1] = {'name': name, 'age': age, 'lived': all_places}



        except Exception as e:
            print(f'error in item {e}')
    # f1.close()
    return mentions




import json


d = a411locate('john', 'doe')
print(json.dumps(d, indent=4))