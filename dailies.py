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


#for cookie in cookies:
    #if cookie.name == "cookie_token":
        #cookies.clear('.mihoyo.com', '.mihoyo.com', cookie.name)

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


    


"""
url = "https://hk4e-api-os.mihoyo.com/event/sol/sign?lang=en-us"

payload = '{"act_id": "e202102251931481"}'

header = {  "Cookie": "_MHYUUID=f69417b6-2754-4a85-aeae-1db60213c965; cookie_token=bfi4i3sbTlCBPPf3ORQKtKMWKYnVMKzuSqUQx4qS; account_id=5618917; _ga_88EC1VG6YY=GS1.1.1630268406.4.1.1630269445.0; _ga=GA1.1.56206098.1624722635; _ga_9TTX3TE5YL=GS1.1.1632919949.34.0.1632919949.0; ltoken=JD6n5XduauumTiEBtGGrR8P8IIjE4XbYCmYGpJE7; ltuid=5618917; _ga_54PBK3QDF4=GS1.1.1641227451.19.0.1641227451.0; _ga_JSHPQ7G1W8=GS1.1.1628183611.1.1.1628183765.0; _ga_KD6RN0HSGZ=GS1.1.1633405548.2.1.1633405570.0; _ga_LH4KMBBZ4L=GS1.1.1634016216.5.0.1634016522.0; _ga_9CLQG3L12Z=GS1.1.1634275249.1.1.1634275376.0; _ga_6ZT27XS0C9=GS1.1.1636247692.5.0.1636247692.0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0",
            "Origin": "https://webstatic-sea.mihoyo.com",
            "Referer": "https://webstatic-sea.mihoyo.com/"
}



response_decoded_json = requests.post(url, data = payload, headers = header)
response_json = response_decoded_json.json()

print(response_json)
"""