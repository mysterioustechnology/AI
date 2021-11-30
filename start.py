import random

# start
print('Hi I am a test AI made by Johnathon!')
start = input('')


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


greet()
