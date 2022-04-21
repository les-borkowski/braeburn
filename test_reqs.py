# quick script for api testing
import requests
from datetime import datetime

# SCRIPT SETTINGS
REQUEST_URL = "http://www.bbc.co.uk"
REQUEST_COUNT = 100
AUTH_USER = 'demo'
AUTH_PASS = 'grannysmith'
SERVER_URL = 'http://127.0.0.1:1337/queries/'

req_counter = REQUEST_COUNT
success_counter = 1
f = open("test_responses.txt", "w")
start = datetime.now()

payload = {"url":f"{REQUEST_URL}"}

while(req_counter > 0):
    print(f'test: {success_counter}')
    response = requests.post(f'{SERVER_URL}', auth=(f'{AUTH_USER}', f'{AUTH_PASS}'), data=payload)
    f.write(f'{str(success_counter)}: {str(response.status_code)}\n')
    success_counter += 1
    req_counter -= 1

end = datetime.now()
elapsedtime = end - start
f.write(f'Elapsed time: {elapsedtime}\n')
f.close()