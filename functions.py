import random;
import dict;

# is an answer to how your day is going?
def day_answer(input):
    intention = ""
    if_day_answer = any(day_answer in input for day_answer in day_answer)
    if if_day_answer:
        random_num = random.randint(0, 4)
        if if_day_answer:
            intention = 'greating'
        if intention == 'greating':
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
        return x
        dict.go = false