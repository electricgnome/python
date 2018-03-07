import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def yes_no(answer):
    yes=(['yes','y','ye',''])
    no=(['no','n'])
    while True:
        choice= input(answer).lower()
        if choice in yes:
            return True
        elif choice in no:
            return False
        else:
            print ("Please respond with 'yes' or 'no'")

def guess_game():
    secret = random.randint(1,10)
    tries=5
    correct=False
    print(bcolors.ENDC +"I'm thinking of a number between 1 and 10")
    while (correct==False and tries>0):
        print (bcolors.WARNING +"You have " + str(tries) + " guesses left")
        try:
            guess = int(input(bcolors.ENDC+"What's the number:"))
        except ValueError:
            print(bcolors.WARNING + "please use a number between 1 and 10.")
            continue
        else:
            if 1 <= guess <= 10:
                if guess==secret:
                    correct=True
                    print (bcolors.OKGREEN + "You win!")

                elif guess<secret:
                    tries -=1
                    print(bcolors.FAIL + "Higher! ")
                elif guess>secret:
                    tries -=1
                    print(bcolors.FAIL + "Lower!")
            else:
                print(bcolors.WARNING + "please use a number between 1 and 10.")
    if tries ==0:
        print(bcolors.FAIL + "You didn't guess!")


    again=yes_no(bcolors.OKBLUE + "Do you want to play again?")
    if again:
        guess_game()


guess_game()
