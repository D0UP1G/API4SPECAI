import requests
from urllib.parse import urlencode
while True:
    a = input('[1]Получить Токен\n[2]Получить о товаре\nПолучить: ')
    try:
        if int(a) == 1:
            print(requests.post('https://d5dhfr3ddkpc5v7acc8h.apigw.yandexcloud.net/token').text)
        if int(a) == 2:
            data = {
                'token':input('token: '),
                'model':input('Model: '),
                'brand':input('Brand: ')
            }

            print(requests.get(f'https://d5dhfr3ddkpc5v7acc8h.apigw.yandexcloud.net/get_sign?{urlencode(data)}').text)
            
    except:
        print('Ты видимо Биттер')