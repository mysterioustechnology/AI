import random;
import dict;

# is an answer to how your day is going?
def day_answer(input):
    random_num = random.randint(0, 4)
    if dict.intention == 'greating':
        greets = ["hey there!", 'sup', 'Whats Up?','How are you', 'Hellow There']
        print('Server: '+ greets[random_num])


def greet():
    random_num = random.randint(0, 4)
    if dict.intention == 'greating':
        x = dict.greets[random_num]
        return x

def stop():
    random_num = random.randint(0, 4)
    if dict.intention == 'stop':
        x = dict.end[random_num]
        return str(x)
        dict.go = false