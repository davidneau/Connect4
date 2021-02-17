import copy
import random

def MinMax(self):
    print("Minmax")
    self.board2 = copy.deepcopy(self.board)
    self.colonne2 = copy.deepcopy(self.colonne)
    L = []
    for i in range(1, 8):
        for j in range(1, 8):
            for k in range(1, 8):
                try:
                    sum = 0

                    self.move("ordi", i)
                    pos = (-self.colonne[i], i - 1)
                    sum += self.score("ordi", "0", pos)

                    self.move("Player", j)
                    pos = (-self.colonne[j], j - 1)
                    sum += self.score("Player", "X", pos)

                    self.move("ordi", k)
                    pos = (-self.colonne[k], k - 1)
                    sum += self.score("ordi", "0", pos)

                    L.append(sum)

                    self.board = copy.deepcopy(self.board2)
                    self.colonne = copy.deepcopy(self.colonne2)
                except:
                    L.append(-1000000)
                    self.board = copy.deepcopy(self.board2)
                    self.colonne = copy.deepcopy(self.colonne2)
    maxx = [max(i) for i in self.paquet(L)[0]]
    minn = [min(i) for i in self.paquet(maxx)[0]]
    print(self.paquet(maxx)[1])
    print(minn)
    if len(indexMax(minn, np.max(minn))) > 1:
        maxx = random.choice(indexMax(minn, np.max(minn)))
    else:
        maxx = np.argmax(minn)
    self.board = copy.deepcopy(self.board2)
    self.colonne = copy.deepcopy(self.colonne2)
    print("fin minmax")
    return maxx