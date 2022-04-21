import sys
import subprocess
from subprocess import PIPE
import json
import os
import braeburn

url = 'http://google.com'
cmd = f'python braeburn.py {url}'
cmd2 = f'pwd'
my_response = subprocess.check_output(['python', 'braeburn.py', f'{url}'], universal_newlines=True)
# my_response = subprocess.Popen(['python', 'braeburn.py', f'{url}'], stdout=PIPE, stderr=PIPE, universal_newlines=True)
# data = stdout, stderr = my_response.communicate()
# data2 = my_response.stdout.read()
# my_response = os.system(f'python braeburn.py {url}') 
print(my_response)
# my_response = subprocess.call('pwd')


