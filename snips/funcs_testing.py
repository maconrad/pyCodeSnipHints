import random
from functools import reduce

def hello():
    return 'hello'

def format_data_for_display(people):
    ret = []
    for person in people:
        val = '{} {}: {}'.format(person['given_name'], person['family_name'], person['title'])
        ret.append(val)
    return ret

def hello_raises():
    raise ValueError('Just testing with some error')

def below2(integer_list, below_value):
    summ = reduce(lambda x, y: x + y, integer_list)
    print(summ)
    if summ <= below_value:
        return True
    return False

def roll_dice():
    print('rolling...')
    return random.randint(1, 6)
