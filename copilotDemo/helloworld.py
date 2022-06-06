#make a game of rock paper scissors
import random
import time
import sys

def main():
    print("Welcome to Rock, Paper, Scissors!")
    print("Please enter your name:")
    name = input()
    print("Hello " + name + "!")
    print("Please enter your choice:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = input()
    if choice == "1":
        choice = "Rock"
    elif choice == "2":
        choice = "Paper"
    elif choice == "3":
        choice = "Scissors"
    print("You chose " + choice)
    print("Please wait...")
    time.sleep(2)
    print("Computer is choosing...")
    time.sleep(2)
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice = "Rock"
    elif comp_choice == 2:
        comp_choice = "Paper"
    else:
        comp_choice = "Scissors"
    print("Computer chose " + comp_choice)
    if choice == "Rock" and comp_choice == "Rock":
        print("It's a tie!")
    elif choice == "Rock" and comp_choice == "Paper":
        print("You lose!")
    elif choice == "Rock" and comp_choice == "Scissors":
        print("You win!")
    elif choice == "Paper" and comp_choice == "Rock":
        print("You win!")
    elif choice == "Paper" and comp_choice == "Paper":
        print("It's a tie!")
    elif choice == "Paper" and comp_choice == "Scissors":
        print("You lose!")
    elif choice == "Scissors" and comp_choice == "Rock":
        print("You lose!")
    elif choice == "Scissors" and comp_choice == "Paper":
        print("You win!")
    elif choice == "Scissors" and comp_choice == "Scissors":
        print("It's a tie!")
    else:
        print("Please enter a valid choice!")
        sys.exit()
    print("Would you like to play again?")
    print("1. Yes")
    print("2. No")
    play_again = input()
    if play_again == "1":
        main()
    elif play_again == "2":
        print("Goodbye!")

main()