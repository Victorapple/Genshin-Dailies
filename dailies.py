import requests, json

import browser_cookie3
import time
import sys


act_id = "e202102251931481" #This is the action ID for login dailies. 

headers = {
        'Accept': 'application/json', 
        'Origin': 'https://webstatic-sea.mihoyo.com',
        'Referer': f'https://webstatic-sea.mihoyo.com/ys/event/signin-sea-v3/index.html?act_id={act_id}&mhy_auth_required=true&mhy_presentation_style=fullscreen&utm_source=tools&lang=en-us',
    }

params = (
        ('lang', 'en-us'),
        ('act_id', act_id),
)

try:
    cookies = browser_cookie3.load(domain_name = ".mihoyo.com")
   
except Exception as e:
    print("No login information found. Login first to Hoyolab to generate cookies.")
    time.sleep(5)
    sys.exit(1)    

try:
    response = requests.get('https://hk4e-api-os.mihoyo.com/event/sol/info', headers= headers, params=params, cookies = cookies).json()
    if response['retcode'] == 0:
        if response['data']['is_sign']:
            print("You have already claimed rewards today. Try again tommorow.")
            sys.exit(1)
        else:
            print("Attempting to claim daily rewards.")
            try:
                response = requests.post('https://hk4e-api-os.mihoyo.com/event/sol/sign', headers=headers, params=params, cookies=cookies, json= {'act_id': act_id}).json()
                num = response['data']['total_sign_day']
                print(f"Daily rewards claimed! You have claimed Day {num} rewards.")
            
            except requests.exceptions.ConnectionError as e:
                print("Connection error. Cannot claim daily reward.")

    else:
        print("You are not logged in onto Hoyolab. Login first to Hoyolab.")
        sys.exit(1)

except Exception as e:
    print("No login information found. Login first to Hoyolab to generate cookies.")
    print(e)
    sys.exit(1)


