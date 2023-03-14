import requests

cookies = {
    'XSRF-TOKEN': '1L4yCe3vR2zbDr80XA91D0aMnPtiENr8JXeLURw1v_-dyl05qKsyOop77GcrehxFft3-jCNK75dVMNIFSXDTmg%3D%3D',
    '_csrf': 'a83c116f391379b783f9ca3f12c34e863b564d710ffd8aa9663b63cf312e5015a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22Ito0EDuVQuSSwuiJ8QbwAZ5kpGYTUEle%22%3B%7D',
    '_gcl_au': '1.1.1435399673.1678467073',
    '_rdt_uuid': '1678467073451.07d84e10-b9de-41c8-9452-db5e58a965ca',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_first_add': 'fd%3D2023-03-10%2016%3A51%3A13%7C%7C%7Cep%3Dhttps%3A%2F%2Fonerep.com%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current_custom': 'campaign_id%3D%28none%29%7C%7C%7Cadgroup_id%3D%28none%29%7C%7C%7Cutm_type%3D%28none%29',
    'sbjs_first_custom': 'campaign_id%3D%28none%29%7C%7C%7Cadgroup_id%3D%28none%29%7C%7C%7Cutm_type%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29',
    '_ga': 'GA1.2.1891695047.1678467074',
    'FPAU': '1.1.1435399673.1678467073',
    'hubspotutk': '848ff9b0ab79d445223ccc34e03b5383',
    '__hssrc': '1',
    '__zlcmid': '1Eolf2CDMdphHDd',
    '_hjSessionUser_666932': 'eyJpZCI6IjE3NDRjMzIyLTM1ZmUtNTJlYi04NmI1LTRiNmU5NzJmYTBjYSIsImNyZWF0ZWQiOjE2Nzg0NjcwNzU4MzAsImV4aXN0aW5nIjp0cnVlfQ==',
    '_auth': '%7B%22access_token%22%3A%22e1a755fb41ce3717c66dbfcaf4547a14f3956f00%22%2C%22expires_in%22%3A315360000%2C%22token_type%22%3A%22bearer%22%2C%22scope%22%3Anull%2C%22refresh_token%22%3A%226bdde671d354e1337d1f7dd0c4fac4958d97fabe%22%7D',
    '_identity': 'b475c9a469e8d8db4c6b942318e3bd6c9ba4a50e469442c3dc17b56718aa3f9ba%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A52%3A%22%5B595787%2C%22aBmh7uawIMCiHsvaWgxuOd5bP4PSo7rQ%22%2C31536000%5D%22%3B%7D',
    '_hjDonePolls': '873048',
    'sbjs_current_add': 'fd%3D2023-03-13%2016%3A41%3A03%7C%7C%7Cep%3Dhttps%3A%2F%2Fonerep.com%2Fdashboard%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
    'sbjs_current': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29',
    '_gid': 'GA1.2.253608904.1678725664',
    'PHPSESSID': 'ec7e114d51ec68e1592fd4304022659d',
    'sbjs_udata': 'vst%3D7%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F111.0.0.0%20Safari%2F537.36',
    '__hstc': '71170255.848ff9b0ab79d445223ccc34e03b5383.1678467074420.1678725664384.1678730028010.6',
    '_hjIncludedInSessionSample_666932': '0',
    '_hjSession_666932': 'eyJpZCI6IjEzZDEzZTkwLTNiYWMtNDczNy04NTllLTU4ZWY0NjVjYmU0YiIsImNyZWF0ZWQiOjE2Nzg3MzAwMjkyNzcsImluU2FtcGxlIjpmYWxzZX0=',
    'sbjs_session': 'pgs%3D3%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fonerep.com%2Fdashboard',
    '_uetsid': 'd830adc0c1bd11ed97cf3d548d9c90d6',
    '_uetvid': 'c45593f0bf6311ed9ec5d3708b90f953',
    '_gat_UA-62975156-8': '1',
    '_gat_UA-62975156-1': '1',
    '__hssc': '71170255.3.1678730028010',
}

headers = {
    'authority': 'customer-api.onerep.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6',
    'authorization': 'Bearer e1a755fb41ce3717c66dbfcaf4547a14f3956f00',
    # 'cookie': 'XSRF-TOKEN=1L4yCe3vR2zbDr80XA91D0aMnPtiENr8JXeLURw1v_-dyl05qKsyOop77GcrehxFft3-jCNK75dVMNIFSXDTmg%3D%3D; _csrf=a83c116f391379b783f9ca3f12c34e863b564d710ffd8aa9663b63cf312e5015a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22Ito0EDuVQuSSwuiJ8QbwAZ5kpGYTUEle%22%3B%7D; _gcl_au=1.1.1435399673.1678467073; _rdt_uuid=1678467073451.07d84e10-b9de-41c8-9452-db5e58a965ca; sbjs_migrations=1418474375998%3D1; sbjs_first_add=fd%3D2023-03-10%2016%3A51%3A13%7C%7C%7Cep%3Dhttps%3A%2F%2Fonerep.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current_custom=campaign_id%3D%28none%29%7C%7C%7Cadgroup_id%3D%28none%29%7C%7C%7Cutm_type%3D%28none%29; sbjs_first_custom=campaign_id%3D%28none%29%7C%7C%7Cadgroup_id%3D%28none%29%7C%7C%7Cutm_type%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29; _ga=GA1.2.1891695047.1678467074; FPAU=1.1.1435399673.1678467073; hubspotutk=848ff9b0ab79d445223ccc34e03b5383; __hssrc=1; __zlcmid=1Eolf2CDMdphHDd; _hjSessionUser_666932=eyJpZCI6IjE3NDRjMzIyLTM1ZmUtNTJlYi04NmI1LTRiNmU5NzJmYTBjYSIsImNyZWF0ZWQiOjE2Nzg0NjcwNzU4MzAsImV4aXN0aW5nIjp0cnVlfQ==; _auth=%7B%22access_token%22%3A%22e1a755fb41ce3717c66dbfcaf4547a14f3956f00%22%2C%22expires_in%22%3A315360000%2C%22token_type%22%3A%22bearer%22%2C%22scope%22%3Anull%2C%22refresh_token%22%3A%226bdde671d354e1337d1f7dd0c4fac4958d97fabe%22%7D; _identity=b475c9a469e8d8db4c6b942318e3bd6c9ba4a50e469442c3dc17b56718aa3f9ba%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A52%3A%22%5B595787%2C%22aBmh7uawIMCiHsvaWgxuOd5bP4PSo7rQ%22%2C31536000%5D%22%3B%7D; _hjDonePolls=873048; sbjs_current_add=fd%3D2023-03-13%2016%3A41%3A03%7C%7C%7Cep%3Dhttps%3A%2F%2Fonerep.com%2Fdashboard%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_current=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29; _gid=GA1.2.253608904.1678725664; PHPSESSID=ec7e114d51ec68e1592fd4304022659d; sbjs_udata=vst%3D7%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F111.0.0.0%20Safari%2F537.36; __hstc=71170255.848ff9b0ab79d445223ccc34e03b5383.1678467074420.1678725664384.1678730028010.6; _hjIncludedInSessionSample_666932=0; _hjSession_666932=eyJpZCI6IjEzZDEzZTkwLTNiYWMtNDczNy04NTllLTU4ZWY0NjVjYmU0YiIsImNyZWF0ZWQiOjE2Nzg3MzAwMjkyNzcsImluU2FtcGxlIjpmYWxzZX0=; sbjs_session=pgs%3D3%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fonerep.com%2Fdashboard; _uetsid=d830adc0c1bd11ed97cf3d548d9c90d6; _uetvid=c45593f0bf6311ed9ec5d3708b90f953; _gat_UA-62975156-8=1; _gat_UA-62975156-1=1; __hssc=71170255.3.1678730028010',
    'dnt': '1',
    'origin': 'https://onerep.com',
    'referer': 'https://onerep.com/',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

params = {
    'user_id': '595787',
    'status[]': 'frozen',
    'page': '1',
    'profile_id': '910422',
    'per_page': '50',
}

response = requests.get('https://customer-api.onerep.com/scan-results', params=params, cookies=cookies, headers=headers)

with open('onerepcopy_frozen.html', 'a') as f:
    f.write(response.text)