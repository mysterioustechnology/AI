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

# is greet?
def greet(input):

    intention = ""
    if_greeting = any(greeting in input for greeting in greeting)
    random_num = random.randint(0, 4)
    if if_greeting:
        intention = 'greating'
    if intention == 'greating':
        greets = ["hey there!", 'sup', 'Whats Up?','How are you', 'Hellow There']
        print(greets[random_num])

day_answer('hey');