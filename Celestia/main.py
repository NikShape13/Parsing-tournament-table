import requests
import json
from fake_useragent import UserAgent as US


user_agent = US().random


headers = {
    'authority': '7nkwv3z5t1.execute-api.us-east-1.amazonaws.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru,en;q=0.9',
    'origin': 'https://analytics.smartstake.io',
    'referer': 'https://analytics.smartstake.io/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "YaBrowser";v="24.1", "Yowser";v="2.5"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': user_agent,
}

params = {
    'pageSize': '500',
    'page': '1',
    'type': 'address',
    'key': '2mwTEDr9zXJH323M',
    'token': '1712840836',
    'app': 'TIA',
}


with open('adress.txt') as f:
    adress_list = f.read().splitlines()


for i in range(1, 1033):
    r = requests.get(
        'https://7nkwv3z5t1.execute-api.us-east-1.amazonaws.com/prod/richlist', params=params, headers=headers)
    r.encoding = 'utf-8'

    dicts = r.json()['data']

    for i in dicts:
        if i['address'] in adress_list:
            with open('fin.json', 'a')as f:
                json.dump(i, f, indent=4)

            if i['address'] == adress_list[-1]:
                print('Done')

    params['page'] = str(int(params['page']) + 1)
