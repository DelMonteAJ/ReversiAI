

from player import Player 
import random
MAX_DEPTH = 5

class AIPlayer(Player):
    def __init__(self, p):
        self.playerN = p
    def taketurn(self, board):
        def seeNearCorner(action):
            nearCornerCoords = [(0,1),(1,1),(1,0), (0,6),(1,6),(1,7), (6,0),(6,1),(7,1), (6,6), (7,6), (6,7)]
            tup = (action[0],action[1])
            return tup in nearCornerCoords
        # Add a way to return the score with the move that made it
        # Terminate when a score with None is attached
        def predictScore(playerNum, board, depth=1):
            moveList=[]
            maxMove = list(board.actions())[0]
            maxScore = -1
            tempScore = -1
            for option in board.actions():
                # Corner preference
                if option[0] == option[1] == 0 or option[0] == option[1] == 7 or option[0] == option[1] == 0 or (option[0] == 0 and option[1] == 7) or (option[0] == 7 and option[1] == 0):
                    return option
                if seeNearCorner(option): continue
                tempBoard = board.result(option)
                try:
                    opponentMaxMove = -1
                    opponentMaxScore = -1
                    opponentMaxBoard = tempBoard.result(list(tempBoard.actions())[0])
                    for opponentMove in tempBoard.actions():
                        opponentTempBoard = tempBoard.result(opponentMove)
                        opponentTempScore = opponentTempBoard.countpieces(1 if playerNum == 2 else 2)
                        print(f"Opp Score: {opponentTempScore} - {opponentMaxScore}")
                        if type(opponentMaxBoard) == None: opponentMaxBoard = opponentTempBoard
                        if opponentTempScore > opponentMaxScore:
                            opponentMaxScore = opponentTempScore
                            opponentMaxMove = opponentMove
                            opponentMaxBoard = opponentTempBoard 
                    # predictScore(playerNum, opponentMaxBoard,depth+1)
                    tempScore = opponentMaxBoard.countpieces(playerNum)
                    moveList.append(())
                except:
                    tempBoard.countpieces(playerNum)
                print(f"Playing {option} gives me a score of {tempScore}")
                if tempScore > maxScore:
                    maxScore = tempScore
                    maxMove = option
            print(f"Playing {maxMove} gives me a score of {maxScore}, which is the best move.")
            # return maxMove if maxMove != -1 else random.sample(sorted(board.actions()),1)[0]
                # if depth >= MAX_DEPTH:
                #     return ()
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
    
