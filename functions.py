import random;
import dict;

# is an answer to how your day is going?
def day_answer(input):
    random_num = random.randint(0, 4)
    if dict.intention == 'day_answer':
        
        greets[random_num]


def greet():
    random_num = random.randint(0, 4)
    if dict.intention == 'greating':
        x = dict.greets[random_num]
        return x


def stop():
    random_num = random.randint(0, 3)
    if dict.intention == 'stop':
        x = dict.end[random_num]
        dict.go = false
        if type(x) == 'NoneType':
            x = 'error'
        return x
