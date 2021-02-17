import numpy as np
from Board import board
from TreeSearchMinMax import TSMinMax

class Minimax():
    def __init__(self):
        self.player = "j1"
        self.winner = ""
        self.profMM = 5
        print("ok")
        self.board = board(np.tile(' ', (7,7)))
        self.partie()


    def partie(self):
        pos = [10, 10]
        joueur = ["Player", "ordi"]
        ind = 1
        self.player = joueur[ind]
        CW = 0
        i = 0
        while CW != 1:
            print("Au tour de : ", self.player)
            if self.player == "Player":
                print(self.board.plateau)
                coup = int(input())
                self.board.move("Player", coup)
                pos = (-self.board.colonne[coup], coup-1)
            if self.player == "ordi":
                coup = self.MinMax()+1
                self.board.move("ordi", coup)
                pos = (-self.board.colonne[coup], coup-1)
            i+=1
            ind += 1
            print(self.board.plateau)
            self.player = joueur[ind%2]
            CW = self.board.condWin(pos)


    def MinMax(self):
        ts = TSMinMax(self.profMM, 7, self.board)
        print(ts.root.heuristic)

Minimax()


