import random;
import dict;
from dict import server

# is an answer to how your day is going?
# def day_answer(input):
#     random_num = random.randint(0, 4)
#     if dict.intention == 'day_answer':
        
#         greets[random_num]


def greet():
    global server 
    if dict.intention == 'greating':
        server = random.choice(dict.greets)
        return server


def stop():
    global server
    if dict.intention == 'stop':
        server = random.choice(dict.end)
        dict.go = False

def play(game):
    if game == 'null':
        game = input('What game would you like to play?  ')
        if not game:
            game = 'null'
        play(game)
    if game == 'tic tac toe':
        print('Loading...')
        print('\n'*200)
        from tic_tac_toe import tic_tac_toe
        tic_tac_toe()
    if game == 'hangman':
        print('Loading...')
        print('\n'*200)
        from hangman import hangman
        hangman()
