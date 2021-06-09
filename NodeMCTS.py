import copy

class Node():

    def __init__(self, board, father=None):
        self.board = board
        self.children = []
        self.father = father
        self.moveplayed = []


    def create_child(self, chosen_move):
        newboard = copy.copy(self.board)
        newboard.move(chosen_move)
        self.children.append(newboard, self)
        self.moveplayed.append(chosen_move)

