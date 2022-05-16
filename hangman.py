new = True
def diffult():
    global my_file
    diffulty = input("choose your diffulty \n hard \n medium \n easy \n : ")
    if diffulty == 'hard':
        my_file = open("/home/mysterious/Documents/Local_Git/AI/hard.txt", "r")
    elif diffulty == 'medum':
        my_file = open("hangman_medum.txt")
    else:
        diffult()
    new = False

def hangman():
    # sets the difficulty of the game only if the user hasent played before
    if new:
        diffult()    
    else:
        yn = input("Do you want to change the difficulty? ")
        if yn == 'yes':
            diffult()
    import random
    # var init
    guesses=0
    word_bank = my_file.readlines()
    chosen_word = random.choice(word_bank)
    shown = []
    global chosen_bank
    chosen_bank = ["Already Picked: "]

    #sets up the hangman game
    for i in range(len(chosen_word)):
        shown.append("-")

    # error handler
    def error(letter,done):
        if len(letter) > 1:
            print("Your guess must have exactly one character!")
            return True
        if not letter.islower():
            print("Letter must be a lower case!")
            return True
        if letter in done:
            print("You have allready picked that letter!")
            return True
    #letter checker
    def letter_check(letter,word):
        if letter in word:
            for z in range(len(word)):
                if chosen_word[z] == letter:
                    shown[z] = chosen_word[z]
            chosen_bank.append(letter)
            chosen_bank.append(",")
            return False
        chosen_bank.append(letter)
        chosen_bank.append(",")
        return True


    # game over checker
    def game_over(i):
        if i >= 10:
            print("The Word Was: " + chosen_word)
            print("You Lose!")
            return True
        if not "-" in shown:
            print("You Win!")
            print("The Word Was: " + chosen_word)
            return True
        

    # ask for the letter 
    while not game_over(guesses):
        print("You have " + str(10-guesses) + " guesses remaining!")
        print(*chosen_bank)
        print(*shown)
        guess = input("Guess: ")
        print('\n'*150)
        if error(guess,chosen_bank):
            continue
        else:
            if letter_check(guess,chosen_word):
                guesses = guesses + 1
                continue
    def ask(): 
        a = input("Play agine?  ")
        if a == 'yes':
            print("\n" * 150)
            hangman()
        elif a == 'no':
            return done
        else:
            ask()
    ask()