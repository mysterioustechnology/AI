import random
cash = ''


# start
print('Hi I am a test AI made by Johnathon!')



# is greet?
def greet():
    greeting = ['hi', 'hello', 'hey']
    intention = ""
    if_greeting = any(greeting in start for greeting in greeting)
    random = random.randint(0, 4)
    if if_greeting:
        intention = 'greating'
    if intention == 'greating':
        greets = ["hey there!", 'sup', 'Whats Up?',
                  'How are you', 'Hellow There']
        print(greets[random])
# is an answer to how your day is going?
def day_answer():
    if cash === 'greet'
    greeting = ['hi', 'hello', 'hey']
    intention = ""
    if_greeting = any(greeting in start for greeting in greeting)
    random = random.randint(0, 4)
    if if_greeting:
        intention = 'greating'
    if intention == 'greating':
        greets = ["hey there!", 'sup', 'Whats Up?',
                  'How are you', 'Hellow There']
        print(greets[random])


def input():
    user = input('User: ')
    cash = user;
    greet();
    day_answer();
