import random;
import dict;
from dict import server

# is an answer to how your day is going?
def day_answer(input):
    random_num = random.randint(0, 4)
    if dict.intention == 'day_answer':
        
        greets[random_num]


def greet():
    global server 
    if dict.intention == 'greating':
        server = random.choise(dict.greets)
        return server


def stop():
    global server
    if dict.intention == 'stop':
        server = random.choice(dict.end)
        dict.go = False

def play(game):
    if game == 'tic tac toe':
        print('Loading...')
        print('/n'*50)
        execfile(tic_tac_toe.py)