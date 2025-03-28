# =============================
# Take-home Exercise: Rock-Paper-Scissors Game
# =============================

# Task:
# 1. Using the pseudo-code created in your in-class exercise 3, create a Rock-Paper-Scissors game using Python.
# 2. Implement the game logic to allow the user to play against the computer.
# 3. Display the result of each round and the final outcome (win, lose, or tie).
# 4. Allow the user to play multiple rounds and keep track of the score.

import random

def get_user_choice():
    user_input = input("Enter rock, paper, or scissors: ").lower()
    while user_input not in ["rock", "paper", "scissors"]:
        user_input = input("Invalid choice. Enter rock, paper, or scissors: ").lower()
    return user_input

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "win"
    else:
        return "lose"

def play_round():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    if result == "win":
        print("You win this round!")
    elif result == "lose":
        print("You lose this round!")
    else:
        print("This round is a tie!")
    return result

def play_game():
    user_score = 0
    computer_score = 0
    rounds = int(input("Enter the number of rounds you want to play: "))
    for _ in range(rounds):
        result = play_round()
        if result == "win":
            user_score += 1
        elif result == "lose":
            computer_score += 1
        print(f"Score: You {user_score} - {computer_score} Computer")
    if user_score > computer_score:
        print("You win the game!")
    elif user_score < computer_score:
        print("You lose the game!")
    else:
        print("The game is a tie!")

if __name__ == "__main__":
    play_game()
