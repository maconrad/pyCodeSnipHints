import random
import time

import requests

from snips.funcs_testing import roll_dice

def guess_number(num):
    res = roll_dice()
    if res == num:
        return 'You won!'
    else:
        return 'You lost!'

def get_ip():
    response = requests.get("https://httpbin.org/ip")
    if response.status_code == 200:
        return response.json()['origin']

def randum_sum():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    print(time.time())
    return a + b
