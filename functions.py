import random;
import dict;
from dict import server

# is an answer to how your day is going?
def day_answer(input):
    global server 
    if input =='positive':
        server = random.choice(dict.day_responce_positive)
    if input == 'negative':
        server = "under construction!"
    return server

def greet():
    global server 
    server = random.choice(dict.greets)
    return server


def stop():
    global server
    server = random.choice(dict.end)
    dict.go = False
    return server

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
