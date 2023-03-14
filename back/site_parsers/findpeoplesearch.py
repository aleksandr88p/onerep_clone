import json

import requests

def findpeoplesearch(name, state=None, age=None):
    cookies = {
        'X-Mapping-fjhppofk': '5F3B4AF9EBCDEF03FC48835BCC613FF5',
        'PHPSESSID': 'g9d8uem67g1lgicksl9nsurlt5',
        '__utma': '37810740.1905991786.1678750670.1678750670.1678750670.1',
        '__utmc': '37810740',
        '__utmz': '37810740.1678750670.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
        '__utmt': '1',
        '__stripe_mid': 'c317a7e9-8fdf-43b4-88f2-1d373095890710daa9',
        '__stripe_sid': '173054a7-c2da-419b-9888-e9f9af0f907234d96d',
        '__utmb': '37810740.14.10.1678750670',
    }

    headers = {
        'authority': 'www.findpeoplesearch.com',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'X-Mapping-fjhppofk=5F3B4AF9EBCDEF03FC48835BCC613FF5; PHPSESSID=g9d8uem67g1lgicksl9nsurlt5; __utma=37810740.1905991786.1678750670.1678750670.1678750670.1; __utmc=37810740; __utmz=37810740.1678750670.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; __stripe_mid=c317a7e9-8fdf-43b4-88f2-1d373095890710daa9; __stripe_sid=173054a7-c2da-419b-9888-e9f9af0f907234d96d; __utmb=37810740.14.10.1678750670',
        'origin': 'https://www.findpeoplesearch.com',
        'referer': 'https://www.findpeoplesearch.com/Billie+Bones/null/null/null/null/null/null/null/null/null/null/null/1/null/16787510919391',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    """
    data = {
        'formData': '&full_name=billie bones&age=30&state=NY&email=null&address=null&city=null&zip=null&akas=null&phone=null&month=null&day=null&year=null&url_timestamp=16788113483412',
    }
    """

    # name = 'Billie Bones'
    data = {
        'formData': f'&full_name={name}&age=null&state=null&email=null&address=null&city=null&zip=null&akas=null&phone=null&month=null&day=null&year=null&url_timestamp=16787510919391',
    }

    response = requests.post('https://www.findpeoplesearch.com/search_ajax.php', cookies=cookies, headers=headers, data=data)


    from bs4 import BeautifulSoup


    """
    здесь я тестил и поэтому записывал в файл
    """
    # with open('result.html', 'a') as f:
    #     f.write(response.text)
    # f1 = open('result.html', 'r')
    # content = f1.read()
    content = response.text

    soup = BeautifulSoup(content, 'lxml')

    all_items = soup.find_all(class_='panel panel-default')

    mentions = {}
    """
    есть несколько людей с одинаковыми именами и фамилиями здесь сохраяняется только один и ключи у словарей это имена
    """

    # for item in all_items:
    #     try:
    #         head_name = item.find(class_='head_name').text.split('- ')[0].replace('\xa0', '')
    #     except:
    #         head_name = item.find(class_='head_name').text
    #         head_name = head_name.replace('\xa0', '').replace('\n', '').replace('\t', '')
    #     age = item.find(class_='head_dob').text
    #     lived_raw = item.find('h6').text.split()
    #     lived = f"{lived_raw[0]} {lived_raw[1]}"
    #     mentions[head_name] = {'age': age, 'lived': lived}


    """
    здесь сохраяняются все и ключи у словарей это имена и возраст    
    """

    for item in all_items:
        try:
            head_name = item.find(class_='head_name').text.replace('\n', '').replace('\t', '').split(' - ')
            name = head_name[0]
            age = head_name[1]
            lived_raw = item.find('h6').text.split()
            lived = f"{lived_raw[0]} {lived_raw[1]}"
            mentions[f"{name} {age}"] = {'name': name, 'age': age, 'lived': lived}
        except Exception as ex:
            print(f'error in findpeoplesearch {ex}')
            continue



    # f1.close()

    return mentions



# print(json.dumps(findpeoplesearch('Billie Bones'), indent=4))
print(json.dumps(findpeoplesearch('John Doe'), indent=4))