import random

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


    print("I'm thinking of a number between 1 and 10")
    while (correct==False and tries>0):
        print ("You have " + str(tries) + " guesses left")

        try:
            guess = int(input("What's the number:"))
        except ValueError:
            print("please use a number between 1 and 10.")
            continue
        else:
            if 1 <= guess < 10:
                if guess==secret:
                    correct=True
                    print ("You win!")

                elif guess<secret:
                    tries -=1
                    print("Too low, go higher! ")
                elif guess>secret:
                    tries -=1
                    print("Too high, go lower!")
            else:
                print("please use a number between 1 and 10.")
    if tries ==0:
        print("You didn't guess!")


    again=yes_no("Do you want to play again?")
    # if again =="no":
    #     return
    # elif again=="yes":
    if again:
        guess_game()


guess_game()
