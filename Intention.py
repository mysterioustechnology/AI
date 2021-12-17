import dict
import functions

passthrough = ''
def user_input(intention):
    user = input('User: ')
    cash = intention;
    get_int(user,cash)
    output = Intention.get_int()
    return output

def get_int(input,recent):
    global pass_through
    input = input.split()
    for items in dict.ending:
        if items == input:
            pass_through =functions.stop()
    for items in dict.greeting:
        if items == input:
            dict.intention = 'greeting'
            pass_through = functions.greet()
    if 'play' in input:
        if 'tic' or 'tac' or 'toe' in input:
            functions.play('tic tac toe')
            pass_through = 'game'
    return pass_through


