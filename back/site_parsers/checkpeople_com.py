import requests

cookies = {
    '__cf_bm': 'UDdPKp5KB63gkUvISf8Y4Yw.Jy5YoP0mupvmIlJ1Pm0-1680080452-0-AfAfSCb0OMSTC2YQlmyiWYxfUGVa+cksM67EOcudUH50QS7FvYRi+TBVjUpuqj5xYQLY3j8zOWQFIARNrrdB7InE/c68RR8sI9WYdj7wJjVA',
    '_vwo_uuid_v2': 'D5992CC38E0E8D9E6454C518700A08DB2|f45b6e3901d3fb31010fb1c82e26c67a',
    '_gcl_au': '1.1.1119363499.1680080452',
    '_clck': '1dv5mwt|1|fab|0',
    '_vis_opt_s': '1%7C',
    '_vis_opt_test_cookie': '1',
    '_vwo_uuid': 'D5992CC38E0E8D9E6454C518700A08DB2',
    '_vwo_ds': '3%241680080451%3A37.72361526%3A%3A',
    '_ga': 'GA1.1.1183632586.1680080453',
    '_wingify_pc_uuid': 'e128b21f883647b69dd78eb3077004ff',
    'wingify_donot_track_actions': '0',
    'trustedsite_visit': '1',
    'trustedsite_tm_float_seen': '1',
    '__ssid': 'ad90b6e7b630a6a21531fe52d860691',
    '_vis_opt_exp_714_split': '4',
    'XSRF-TOKEN': 'eyJpdiI6ImlvVE51YmdCVHFocGM1amVDRldrQnc9PSIsInZhbHVlIjoiczl2SFFxcGd3Ukw3SEsyWm5vam5KRUk3dXNHM1grXC9JS0J6XC90dTA5TjZ3WjFpb09zQ0tjd0dkTzZveENmRHNQRXlxXC9qdEdkU1BHcE53eDMrRWlQNmc9PSIsIm1hYyI6IjhmOGVlM2JkNTQ2Y2Q1YTQ4NjhmMzc1ZGNhM2Q5OThkYzYyNTNiNGZiOWMzM2Y4OWE1OTZhODVkNTVmMmYxYmQifQ%3D%3D',
    'laravel_session': 'eyJpdiI6ImZaVzdKZGttZUIzditIM3BMVk56TFE9PSIsInZhbHVlIjoiK29TQlhIWm1waDFOMnlrOTZzWGwyRTR1T1BUNU9FMUNPM2NKa3pudnVydnJ6WjFQOVRSamZGa2FlQWcxN0JrUGp1Qjk5T2RcL2FMWk1tZUF4OVBrXC9odz09IiwibWFjIjoiMDk1YmRiZWQ4MGE3M2ZlYTFmMDVjN2UzMTFjYzA0Zjc2OGU2YzViN2RkNGJiZDY5ZDAyZGM4NTc2YjNhY2ZhYiJ9',
    '_ga_SWL0YK5V5H': 'GS1.1.1680080452.1.1.1680080465.47.0.0',
    '_vwo_sn': '0%3A2%3A%3A%3A1',
    '_vis_opt_exp_714_combi': '4',
    '_clsk': 'b2i4yg|1680080465670|3|1|s.clarity.ms/collect',
    '_vis_opt_exp_714_goal_1': '1',
}

headers = {
    'authority': 'checkpeople.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': '__cf_bm=UDdPKp5KB63gkUvISf8Y4Yw.Jy5YoP0mupvmIlJ1Pm0-1680080452-0-AfAfSCb0OMSTC2YQlmyiWYxfUGVa+cksM67EOcudUH50QS7FvYRi+TBVjUpuqj5xYQLY3j8zOWQFIARNrrdB7InE/c68RR8sI9WYdj7wJjVA; _vwo_uuid_v2=D5992CC38E0E8D9E6454C518700A08DB2|f45b6e3901d3fb31010fb1c82e26c67a; _gcl_au=1.1.1119363499.1680080452; _clck=1dv5mwt|1|fab|0; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vwo_uuid=D5992CC38E0E8D9E6454C518700A08DB2; _vwo_ds=3%241680080451%3A37.72361526%3A%3A; _ga=GA1.1.1183632586.1680080453; _wingify_pc_uuid=e128b21f883647b69dd78eb3077004ff; wingify_donot_track_actions=0; trustedsite_visit=1; trustedsite_tm_float_seen=1; __ssid=ad90b6e7b630a6a21531fe52d860691; _vis_opt_exp_714_split=4; XSRF-TOKEN=eyJpdiI6ImlvVE51YmdCVHFocGM1amVDRldrQnc9PSIsInZhbHVlIjoiczl2SFFxcGd3Ukw3SEsyWm5vam5KRUk3dXNHM1grXC9JS0J6XC90dTA5TjZ3WjFpb09zQ0tjd0dkTzZveENmRHNQRXlxXC9qdEdkU1BHcE53eDMrRWlQNmc9PSIsIm1hYyI6IjhmOGVlM2JkNTQ2Y2Q1YTQ4NjhmMzc1ZGNhM2Q5OThkYzYyNTNiNGZiOWMzM2Y4OWE1OTZhODVkNTVmMmYxYmQifQ%3D%3D; laravel_session=eyJpdiI6ImZaVzdKZGttZUIzditIM3BMVk56TFE9PSIsInZhbHVlIjoiK29TQlhIWm1waDFOMnlrOTZzWGwyRTR1T1BUNU9FMUNPM2NKa3pudnVydnJ6WjFQOVRSamZGa2FlQWcxN0JrUGp1Qjk5T2RcL2FMWk1tZUF4OVBrXC9odz09IiwibWFjIjoiMDk1YmRiZWQ4MGE3M2ZlYTFmMDVjN2UzMTFjYzA0Zjc2OGU2YzViN2RkNGJiZDY5ZDAyZGM4NTc2YjNhY2ZhYiJ9; _ga_SWL0YK5V5H=GS1.1.1680080452.1.1.1680080465.47.0.0; _vwo_sn=0%3A2%3A%3A%3A1; _vis_opt_exp_714_combi=4; _clsk=b2i4yg|1680080465670|3|1|s.clarity.ms/collect; _vis_opt_exp_714_goal_1=1',
    'referer': 'https://checkpeople.com/landing/people/gc1r/searching?firstName=john&lastName=doe&state=wa&city=&aid=11&sid=&tid=&hitid=&iv=&obcid=',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

params = {
    'firstName': 'john',
    'lastName': 'doe',
    'state': 'wa',
    'city': '',
    'aid': '11',
    'sid': '',
    'tid': '',
    'hitid': '',
    'iv': '',
    'obcid': '',
}

response = requests.get('https://checkpeople.com/landing/people/gc1r/results', params=params, cookies=cookies, headers=headers)

print(response.text)