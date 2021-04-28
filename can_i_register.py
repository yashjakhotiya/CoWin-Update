import requests as r
from playsound import playsound
from time import sleep

url='https://selfregistration.cowin.gov.in'

def get_script_path(response):
    response = str(response)
    idx = response.find('script')
    response = response[idx+7:]
    idx = response.find(' ')
    script_path = response[:idx][5:-1]
    return script_path

def is_last_modified_updated():
    script_path = get_script_path(r.get(url).content)
    js_url = url + '/' + script_path
    last_modified_time = r.get(js_url).headers['last-modified']
    if last_modified_time != 'Wed, 28 Apr 2021 05:01:24 GMT':
        return True
    return False

idx = 0
while(1):
    idx += 1
    if (is_last_modified_updated()):
        print('Register now!\n')
        while(1):
            playsound('alarm.wav')
    else:
        if idx % 60 == 0:
            print('Can not register yet. Time elapsed {} mins'.format(idx/6))
        sleep(10)