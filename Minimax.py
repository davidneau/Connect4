import numpy as np
from TreeSearchMinMax import TSMinMax
import time

class Minimax():
    def __init__(self):
        self.player = "j1"
        self.profMM = 5
        self.nbCoupMax = 7
        self.MinMax()

    def MinMax(self):
        a0 = time.time()
        ts = TSMinMax(self.profMM, self.nbCoupMax, self.board)
        print(ts.root.heuristic)
        print(time.time() - a0)
        return ts.root.heuristic[0]

#Minimax()


