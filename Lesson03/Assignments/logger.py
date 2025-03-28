import datetime

class Logger:
    def __init__(self, log_file="game_log.txt"):
        """
        Initializes the Logger with a specified log file.
        :param log_file: The name of the log file to write to.
        """
        self.log_file = log_file

    def log(self, message):
        """
        Logs a message to the log file with a timestamp.
        :param message: The message to log.
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, "a") as file:
            file.write(f"[{timestamp}] {message}\n")

    def log_game_result(self, player_choice, computer_choice, result):
        """
        Logs the result of a game round.
        :param player_choice: The player's choice (rock, paper, or scissors).
        :param computer_choice: The computer's choice.
        :param result: The result of the game (win, lose, or draw).
        """
        self.log(f"Player chose: {player_choice}, Computer chose: {computer_choice}, Result: {result}")