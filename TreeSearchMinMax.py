from Node import node
from graphviz import Digraph
from Board import board
import numpy as np
import time
import random

class TSMinMax():

    def __init__(self, profondeurMax, nbChildMax, board):
        self.profondeurMax = profondeurMax
        self.nbChildMax = nbChildMax
        self.root = node(None, 0, self.profondeurMax, 0, board)
        self.propagate(self.root)

        self.root.heuristic = self.MinMax(self.root)
        self.info()
        #self.showGraph()

    def propagate(self, node):
        L = [node]
        while L != []:
            if node.numberOfChildren == 0 and node.profondeur != self.profondeurMax:
                L.pop(0)
                for i in range(self.nbChildMax):
                    #self.showGraph()
                    pos = (-node.board.colonne[node.coup + 1], node.coup)
                    if node.board.condWin(pos) == 0:
                        node.createChild(i)
                    else:
                        node.stateBoard = True
                    if node.children != []:
                        L.append(node.children[-1])
                node = L[0]
            else:
                L.pop(0)
                try:
                    node = L[0]
                except:
                    pass

    def MinMax(self, node):
        if node.is_terminal() or node.stateBoard == True:
            return node.heuristic
        else:
            if node.profondeur % 2 == 1:
                node.heuristic = min([self.MinMax(i) for i in node.children])
                return min([self.MinMax(i) for i in node.children])
            if node.profondeur == 0:
                maxi = [-100000000]
                mm_val = [(self.MinMax(i), i.coup) for i in node.children]
                maximum = max([i[0] for i in mm_val])
                choix = [i[1] for i in mm_val if i[0] == maximum]
                p = choix[0]
                #p = random.choice(choix)
                return (p, maxi)
            elif node.profondeur % 2 == 0:
                node.heuristic = max([self.MinMax(i) for i in node.children])
                return max([self.MinMax(i) for i in node.children])


    def showGraph(self):
        dot = Digraph(comment='Tree Search')
        node = self.root
        L = [node]
        while L != []:
            if node.nom in ["Root, " + str(i) for i in range(1, 8)]:
                print("board at node : ", node.nom)
                print(node.board.plateau)
            node = L.pop(0)
            if node.nom == "Root":
                dot.node(node.nom, node.nom[-1] + " " + str(node.heuristic))
            else:
                dot.node(node.nom, node.nom[-1] + " " + str(node.heuristic))
                dot.edge(node.father.nom, node.nom, constraint='True')
            try:
                [L.append(n) for n in node.children]
            except:
                pass
        dot.render('TreeSearch.dot', view=True)

    def info(self):
        print("heuristic de root : ", self.root.heuristic)
