from Node import node

class TSMinMax():

    def __init__(self, profondeurMax, nbChildMax, board):
        self.profondeurMax = profondeurMax
        self.nbChildMax = nbChildMax
        self.root = node(None, 0, self.profondeurMax, 0, board)
        self.propagate(self.root)

        self.root.heuristic = self.MinMax(self.root)
        self.info()

    def propagate(self, node):
        L = [node]
        while L != []:
            if node.numberOfChildren == 0 and node.profondeur != self.profondeurMax:
                L.pop(0)
                for i in range(self.nbChildMax):
                    node.createChild(i)
                    L.append(node.children[-1])
                node = L[0]
            else:
                L.pop(0)
                try:
                    node = L[0]
                except:
                    pass

    def MinMax(self, node):
        if node.is_terminal():
            return node.heuristic
        else:
            if node.profondeur % 2 == 1:
                return min(self.MinMax(node.children[0]), self.MinMax(node.children[1]))
            if node.profondeur % 2 == 0:
                return max(self.MinMax(node.children[0]), self.MinMax(node.children[1]))


    def info(self):
        print("heuristic de root : ", self.root.heuristic)