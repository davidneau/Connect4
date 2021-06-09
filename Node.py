import copy

class node():

    def __init__(self, father, p, profondeurMax, i=0, board=None):
        self.board = board
        self.children = []
        self.father = father
        self.numberOfChildren = len(self.children)
        self.heuristic = 0
        self.coup = i
        self.stateBoard = False
        self.profondeur = p
        self.profondeurMax = profondeurMax
        if father == None:
            self.nom = "Root"
            self.movePlayed = None
        elif father.nom == "Root":
            self.movePlayed = [i+1]
            self.nom = "Root, " + str(i+1)
        else:
            MP = copy.copy(father.movePlayed)
            MP.append(i+1)
            self.movePlayed = MP
            self.nom = self.father.nom + "," + str(i+1)
        if self.nom != "Root":
            if self.profondeur % 2 == 1:
                p = "ordi"
            else:
                p = "Player"
            pos = (-self.board.colonne[i+1], i)
            score = self.board.score(p, pos)
            self.heuristicBase = score
            self.heuristic = self.father.heuristic + score

    def is_terminal(self):
        if self.profondeur == self.profondeurMax:
            return True
        else:
            return False

    def createChild(self, i):
        boardChild = copy.deepcopy(self.board)
        p = ""
        if self.profondeur % 2 == 0:
            p = "ordi"
        else:
            p = "Player"
        try:
            boardChild.move(p, i+1)
            newnode = node(self, self.profondeur+1, self.profondeurMax, i, boardChild)
            self.children.append(newnode)
        except:
            pass

    def __str__(self):
        return self.nom