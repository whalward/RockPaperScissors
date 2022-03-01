'''
Waseem Alward
cis-125-72
rockpaperscissors.py
'''

import random

win = 0
lose = 0
tie = 0

while True:
    user_input = input("Choose rock, paper or scissors: ")

    possible_choices = ["rock", "paper", "scissors"]

    computer_choices = random.choice(possible_choices)

    print(f"\nYou chose {user_input} and the computer chose {computer_choices}.\n")


    if user_input == computer_choices:
        print(f"Both players selected {user_input}. It's a tie!")
        tie += 1
    elif user_input == "rock":
        if computer_choices == "scissors":
            print("Rock smashes scissors! You win!")
            win += 1
        else:
            print("Paper covers rock! You lose.")
            lose += 1
    elif user_input == "paper":
        if computer_choices == "rock":
            print("Paper covers rock! You win!")
            win += 1
        else:
            print("Scissors cuts paper! You lose.")
            lose += 1
    elif user_input == "scissors":
        if computer_choices == "paper":
            print("Scissors cuts paper! You win!")
            win += 1
        else:
            print("Rock smashes scissors! You lose.")
            lose += 1
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break

print("You've won: ", win, "\nLost: ", lose, "\nTied: ", tie)
