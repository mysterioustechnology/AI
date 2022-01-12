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
    for i in range(len(dict.greeting)):
        dict.greeting[i]
        if dict.greeting[i] == user:
            dict.intention = 'greeting'
            pass_through = functions.greet()
    if 'play' in user:
        x = user.index('play')
        rem = user[:x]
        for z in range(len(rem)):
            if rem[z] in user:
                index = user.index(rem[z])
                user = user.remove(user[index])
        if 'tic tac toe' in user:
            functions.play('tic tac toe')
            pass_through = 'game over'
            user = ""
        elif 'hangman' in user:
            functions.play('hangman')
            pass_through = 'game over'
            user = ""
        else:
            functions.play('null')
    if not user:
        pass_through = 'Say Something'
    return pass_through


