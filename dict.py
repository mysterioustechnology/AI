# is greet?
def greet():
    greeting = ['hi', 'hello', 'hey']
    intention = ""
    if_greeting = any(greeting in user for greeting in greeting)
    random_num = random.randint(0, 4)
    if if_greeting:
        intention = 'greating'
    if intention == 'greating':
        greets = ["hey there!", 'sup', 'Whats Up?','How are you', 'Hellow There']
        print(greets[random])
# is an answer to how your day is going?
def day_answer():
    if_day_answer = False;
    day_answer = ['hi', 'hello', 'hey']
    intention = ""
    if_day_answer = any(day_answer in user for day_answer in day_answer)
    if if_day_answer:
        random = random.randint(0, 4)
        if if_day_answer:
            intention = 'greating'
        if intention == 'greating':
            greets = ["hey there!", 'sup', 'Whats Up?','How are you', 'Hellow There']
            print('Server: '+ greets[random])
def user_input():
    user = input('User: ')
    cash = intention;
    greet();
    day_answer();
