

from player import Player 
import random

class AIPlayer(Player):
    def __init__(self, p):
        self.playerN = p
    def taketurn(self, board):
        def predictScore(playerNum, board):
            maxMove = -1
            maxScore = -1
            for option in board.actions():
                # Corner preference
                if option[0] == option[1] == 0 or option[0] == option[1] == 7 or option[0] == option[1] == 0 or (option[0] == 0 and option[1] == 7) or (option[0] == 7 and option[1] == 0):
                    return option
                tempBoard = board.result(option)
                tempScore = tempBoard.countpieces(playerNum)
                print(f"Playing {option} gives me a score of {tempScore}")
                if tempScore > maxScore:
                    maxScore = tempScore
                    maxMove = option
            print(f"Playing {maxMove} gives me a score of {maxScore}, which is the best move.")
            return maxMove
        # board.print()
        # TODO: update this function to use some effective combination of techniques discussed in class
        # Aim to take <5sec/move on reasonably modern hardware.
        # You should *always* beat the random player, and will score points for beating weak AIs as well.
        # To launch a game using this AI, run $ python3 play.py
        # print(board.actions())
        return predictScore(self.playerN, board)
        # return random.sample(sorted(board.actions()),1)[0]
        # return random.sample(sorted(board.actions()),1)[0]
    def player(self):
        return self.playerN
    
