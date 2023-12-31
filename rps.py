"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random

MOVES = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.score = 0
        self.index = 0
        self.last_opponent_move = None
        self.my_move = None

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    winning_combinations = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }
    return winning_combinations[one] == two


class RockPlayer(Player):
    def move(self):
        return "rock"


class RandomPlayer(Player):
    def move(self):
        return random.choice(MOVES)


class HumanPlayer(Player):
    def move(self):
        while True:
            self_move = input("Rock, Paper, Scissors > ").lower()
            if self_move in MOVES:
                return self_move
            else:
                print("Invalid input. Please enter 'rock', 'paper', or 'scissors'.")


class ReflectPlayer(Player):
    """This allows opponent to play your previous move as their next move
    (If you play rock in your last move, the opponent would play rock in their next move)"""

    def __init__(self):
        super().__init__()
        self.their_move = None

    def move(self):
        if self.last_opponent_move is not None:
            return self.last_opponent_move
        else:
            return random.choice(MOVES)

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
    """This allows opponent to remember what move it played last round,
    and cycles through the different moves. (If it played 'rock' this round,
    it should play 'paper' in the next round.)"""

    def move(self):
        new_move = MOVES[self.index]
        if self.index == 2:
            self.index = 0
        else:
            self.index += 1
        return new_move

    def learn(self, my_move, their_move):
        self.my_move = my_move


class Game:
    def __init__(self, player1, player2, rounds=4):  # Change value of rounds to determine number of game rounds
        self.p1 = player1
        self.p2 = player2
        self.rounds = rounds

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You played {move1}. \nOpponent Played {move2}.")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if move1 == move2:
            print("** TIE **")
        elif beats(move1, move2):
            self.p1.score += 1
            print("** PLAYER ONE WINS **")
        else:
            self.p2.score += 1
            print("** PLAYER TWO WINS **")
        print(f"Score: Player One: {self.p1.score}, Player Two: {self.p2.score}\n")

    def play_game(self):
        print("Game start!")
        for game_round in range(self.rounds):
            print(f"Round {game_round + 1}:")
            self.play_round()
        if self.p1.score > self.p2.score:
            print("THE WINNER IS PLAYER ONE")
        elif self.p2.score > self.p1.score:
            print("THE WINNER IS PLAYER TWO")
        else:
            print("IT'S A TIE!")
        print(f"Final Score:\nPlayer One: {self.p1.score}, Player Two: {self.p2.score}")
        print("Game over!")


if __name__ == '__main__':
    opponents = [
        RockPlayer(),
        RandomPlayer(),
        ReflectPlayer(),
        CyclePlayer()
    ]
    p1 = HumanPlayer()
    p2 = random.choice(opponents)
    game = Game(p1, p2)
    game.play_game()
