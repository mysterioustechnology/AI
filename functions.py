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
        x = random.choise(dict.greets)
        return x


def stop():
    if dict.intention == 'stop':
        x = random.choice(dict.end)
        dict.go = false
        return x
