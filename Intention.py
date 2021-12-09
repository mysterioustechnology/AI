import dict
import functions
def user_input(intention):
    user = input('User: ')
    cash = intention;
    get_int(user,cash)

def get_int(input,recent):
    for items in dict.ending:
        if items == input:
            dict.output=functions.stop()
    for items in dict.greeting:
        if items == input:
            dict.intention = 'greeting'
            dict.output = functions.greet()


        print('Server: '+dict.output)

