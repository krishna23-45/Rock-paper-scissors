import random


def main():
    choices = ['rock','papper','scissors']
    computer_guess = random.choice(choices)
    while True:
        guess = str(input("Make a guess \n>>> "))
        guess = guess.lower()
        print("you gussed"+ ' ' + guess)
        print("computer gussed"+ ' ' + computer_guess)
        if guess != "q":
            if guess in choices:
                if guess == computer_guess:
                    print("This is tie . Try again")
                elif guess == 'rock':
                    if computer_guess == "scissors":
                        print('You win!!!')
                    elif computer_guess == ' papper':
                        print("Sorry, You lose : (' ")
                elif guess == "papper":
                    if computer_guess == "rock":
                        print("You win!!!")
                    elif computer_guess == "scissors":
                        print("Sorry, You lose : (' ")
                elif guess == "scissors":
                    if computer_guess == "papper":
                        print("Sorry, You lose : (' ")
                    elif computer_guess == "rock":
                        print("You win!!!")
            else:
                print("invalid choices")
            print("______________________________")
            print("\nEnter q to exit\n")
        elif guess == "q":
            break

main()