import dict
import functions


def user_input(intention):
    user = input('User: ')
    cash = intention;
    get_int(user,cash)
    output = get_int(user,cash)
    return output

def get_int(user,recent):
    from dict import pass_through
    user = user.lower()
    user = user.split()
    for items in dict.ending:
        if items == user:
            pass_through =functions.stop()
    for items in dict.greeting:
        if items == user:
            dict.intention = 'greeting'
            pass_through = functions.greet()
    if 'play' in user:
        x = user.index('play')
        rem = user[:x]
        for items in rem:
            user = user.remove(items)
        if 'tic' or 'tac' or 'toe' in user:
            functions.play('tic tac toe')
            pass_through = 'game'
        else:
            functions.play('null')
    if not user:
        pass_through = 'Say Something'
    return pass_through


