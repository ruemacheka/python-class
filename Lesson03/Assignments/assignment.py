# =============================
# Take-home Exercise: Rock-Paper-Scissors Game - OOP Version
# =============================

# Task:
# Convert your rock-paper-scissors game into a class-based implementation.
# Move the class into a separate module and import it into your main script.

# TODO: Define the Logger class and implement file logging methods
from logger import Logger
import random

class RockPaperScissorsGame:
    def __init__(self, logger):
        self.logger = logger
        self.choices = ["rock", "paper", "scissors"]

    def play_round(self, player_choice):
        computer_choice = random.choice(self.choices)
        if player_choice == computer_choice:
            result = "draw"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            result = "win"
        else:
            result = "lose"

        # Log the result
        self.logger.log_game_result(player_choice, computer_choice, result)
        return result

# Initialize the Logger and Game
logger = Logger()
game = RockPaperScissorsGame(logger)

# Example: Play a round
player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
if player_choice not in ["rock", "paper", "scissors"]:
    print("Invalid choice. Please choose rock, paper, or scissors.")
else:
    result = game.play_round(player_choice)
    print(f"You chose {player_choice}, result: {result}")
