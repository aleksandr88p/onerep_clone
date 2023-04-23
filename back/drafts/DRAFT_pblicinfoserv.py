import requests

cookies = {
    'AWSALB': 'j9Eg3+oMAKBNX8qcC3e2F/ARWFn/Ma9O6htdPd1VyV39/ozuLRk2ikxLi/zi2QyxEBlsKaEJ1dVzqqPHPZTM7lwMPmXJK8Utc035jmlPTpcPclkmR6NA6UcGKmsX',
    'AWSALBCORS': 'j9Eg3+oMAKBNX8qcC3e2F/ARWFn/Ma9O6htdPd1VyV39/ozuLRk2ikxLi/zi2QyxEBlsKaEJ1dVzqqPHPZTM7lwMPmXJK8Utc035jmlPTpcPclkmR6NA6UcGKmsX',
    'koa.sid': 'OS6aidp6zHxPITdOe0OYIGJ8HHmscTlU',
    'koa.sid.sig': 'DZ0LX4lqXxr_LG-1OkAIP3qIlR4',
    '_gcl_au': '1.1.1171074368.1681930903',
    '_ga_PHKGYZNTBE': 'GS1.1.1681930903.1.1.1681931068.0.0.0',
    '_ga': 'GA1.1.1297084430.1681930904',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0',
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.publicinfoservices.com/r/search',
    'X-NewRelic-ID': 'VgQOWVNbGwcJUldbBQMF',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://www.publicinfoservices.com',
    'DNT': '1',
    'Connection': 'keep-alive',
    # 'Cookie': 'AWSALB=j9Eg3+oMAKBNX8qcC3e2F/ARWFn/Ma9O6htdPd1VyV39/ozuLRk2ikxLi/zi2QyxEBlsKaEJ1dVzqqPHPZTM7lwMPmXJK8Utc035jmlPTpcPclkmR6NA6UcGKmsX; AWSALBCORS=j9Eg3+oMAKBNX8qcC3e2F/ARWFn/Ma9O6htdPd1VyV39/ozuLRk2ikxLi/zi2QyxEBlsKaEJ1dVzqqPHPZTM7lwMPmXJK8Utc035jmlPTpcPclkmR6NA6UcGKmsX; koa.sid=OS6aidp6zHxPITdOe0OYIGJ8HHmscTlU; koa.sid.sig=DZ0LX4lqXxr_LG-1OkAIP3qIlR4; _gcl_au=1.1.1171074368.1681930903; _ga_PHKGYZNTBE=GS1.1.1681930903.1.1.1681931068.0.0.0; _ga=GA1.1.1297084430.1681930904',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

data = {
    'state[long]': 'New York',
    'state[short]': 'NY',
    'city': 'New York',
    'minAge': '18',
    'maxAge': '100',
    'firstName': 'John',
    'lastName': 'Smith',
}

response = requests.post('https://www.publicinfoservices.com/api/updateSearch', cookies=cookies, headers=headers, data=data)

cookies2 = response.cookies

res2 = requests.get('https://www.publicinfoservices.com/r/search#', cookies=cookies2)
print(res2.text)