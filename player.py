
import re
import random

class Player:
    def taketurn(self, board):
        print("This is the base class!")
        raise NotImplementedError()
    def player(self):
        print("This is the base class!")
        raise NotImplementedError()


class RandomPlayer(Player):
    def __init__(self, p):
        self.playerN = p
    def taketurn(self, board):
        board.print()
        return random.sample(sorted(board.actions()),1)[0]
    def player(self):
        return self.playerN


class HumanPlayer(Player):
    def __init__(self, p):
        self.playerN = p
    def taketurn(self, board):
        board.print()
        print("")
        coord = None
        while coord == None or coord not in board.actions():
            if coord != None:
                print("Oops, please enter a valid move.")
            coord = input("Give a row,col coordinate for your move: ")
            coord = coord.replace('(','').replace(')','').strip()
            coord = re.match(r'(\d),(\d)',coord)
            if coord:
                coord = (int(coord.group(1)), int(coord.group(2)))
            else:
                print("Sorry, please enter n,m where n and m are in [0--7].")
        return coord
    def player(self):
        return self.playerN
        
