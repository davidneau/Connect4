from NodeMCTS import Node
import random
import copy

class MCTS():

    def __init__(self, expl, board, N, maxmove):
        self.exploration = expl
        self.nbCycle = N
        self.root = Node(board)
        self.maxmove = maxmove
        self.main()

    def main(self):
        for i in range(self.nbCycle):
            nodeSelected = self.selection(self.root)
            nodeSelected.create_child(random.choice([i for i in range(self.maxmove) if i not in nodeSelected.moveplayed]))
            self.simulation(nodeSelected.children[-1])

    def selection(self, node):
        while len(node.children) == self.maxmove:
            node = self.ucb(node)
        return node

    def simulation(self, node):
        board = copy.copy(node.board)
        while board.condWin() == 0:
            board.move(random.choice(range(self.maxmove)))
