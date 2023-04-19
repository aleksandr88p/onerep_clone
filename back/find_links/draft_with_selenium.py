from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import base64
s = Service(executable_path='/home/aleksandr/01_работа/index/03_23/onerep_clone/back/find_links/chromedriver_linux64/chromedriver')
options = webdriver.ChromeOptions()
"""
эти три опции и удаление cdc_cdp нужны для того что бы не было похоже что парсит робот"""
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

h1 = '45.145.58.25:8000'
h2 = '45.155.201.162:8000'

PROXY_HOST = '45.145.58.25'  # Адрес прокси-сервера
PROXY_PORT = 8000  # Порт прокси-сервера
PROXY_USER = '4UsLX7'  # Имя пользователя для аутентификации на прокси-сервере
PROXY_PASS = 'tCDbq9'  # Пароль для аутентификации на прокси-сервере



# options.add_argument(f'--proxy-server=http://{PROXY_USER}:{PROXY_PASS}@{PROXY_HOST}:{PROXY_PORT}')
options.add_argument(f"--proxy-server=http://{h1}")
# options.add_argument()
# if PROXY_USER and PROXY_PASS:
#     credentials = f"{PROXY_USER}:{PROXY_PASS}"
#     # encoded_credentials = base64.b64encode(credentials.encode('ascii')).decode('utf-8')
#     options.add_argument(f'--proxy-auth={credentials}')


driver = webdriver.Chrome(service=s, options=options)

"""
увидел в консоли разработчика
это нужно удалить что бы браузер не думал, что я робот
window.cdc_adoQpoasnfa76pfcZLmcfl_Array
window.cdc_adoQpoasnfa76pfcZLmcfl_Promise
window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol
"""
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',{
    'source': '''
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
    '''
})


try:
    driver.maximize_window()
    driver.get('https://www.fastpeoplesearch.com/name/john-doe_NY')
    time.sleep(999999)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

