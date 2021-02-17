import copy

class node():

    def __init__(self, father, p, profondeurMax, i=0, board=None):
        self.board = board
        self.children = []
        self.father = father
        self.numberOfChildren = len(self.children)
        self.heuristic = 0
        self.profondeur = p
        if father == None:
            self.nom = "Root"
            self.movePlayed = None
        elif father.nom == "Root":
            self.movePlayed = [i+1]
            self.nom = str(self.profondeur) + "," + str(i+1)
        else:
            MP = father.movePlayed
            MP.append(i+1)
            self.movePlayed = MP
            self.nom = str(self.profondeur) + "," + str(i+1)
        self.profondeurMax = profondeurMax
        if self.is_terminal() == True:
            self.heuristic = self.evaluate()

    def is_terminal(self):
        if self.profondeur == self.profondeurMax:
            return True
        else:
            return False

    def evaluate(self):
        node = self
        while node.father != None:
            node = node.father
        print(node.board)
        board = copy.copy(node.board)
        print(board)
        j = 0
        somme = 0
        for i in self.movePlayed:
            pos = (-board.colonne[i], i - 1)
            if j%2 == 0:
                p = "ordi"
                board.move(p, i+1)
                somme += board.score(p, pos)
            if j%2 == 1:
                p = "Player"
                board.move(p, i+1)
                somme += board.score(p, pos)
            j+=1
        return somme

    def createChild(self, i):
        newnode = node(self, self.profondeur+1, self.profondeurMax, i)
        self.children.append(newnode)

    def __str__(self):
        return self.nom