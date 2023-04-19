import requests
import tldextract

# Отправка запроса на сайт
response = requests.get('https://www.fastpeoplesearch.com/')

# Получение куков из ответа сервера
cookies = response.cookies.get_dict()

# Создание списка куков с доменом и путем
cookies_with_domain = []
for cookie_name, cookie_value in cookies.items():
    cookie_domain = tldextract.extract(response.url).registered_domain
    cookie_path = '/'
    cookies_with_domain.append({'name': cookie_name, 'value': cookie_value, 'domain': cookie_domain, 'path': cookie_path})
