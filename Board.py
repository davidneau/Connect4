import numpy as np

class board():

    def __init__(self, np_obj):
        self.plateau = np_obj
        self.colonne = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}

    def move(self, player, col):
        if player == "Player":
            self.plateau[-self.colonne[col]-1, col-1] = "X"
        if player == "ordi":
            self.plateau[-self.colonne[col]-1, col-1] = "0"
        self.colonne[col] += 1

    def consecutif(self, arr, x):
        i = 0
        j = 0
        rec = 0
        while j < len(arr):
            if arr[j] == x:
                i += 1
            else:
                if i > rec:
                    rec = i
                i = 0
            j += 1
        if arr[-1] == x:
            return i
        else:
            return rec

    def indexMax(self, L, m):
        Loutput = []
        for i in range(len(L)):
            if L[i] == m:
                Loutput.append(i)
        return Loutput

    def condWin(self, pos):
        if pos[0] != 0:
            pos = [pos[0]+7, pos[1]]
        if pos == [10, 10]:
            return 0
        val = self.plateau[pos[0], pos[1]]
        if val == " ":
            return 0
        if list(self.colonne.values()) == [7, 7, 7, 7, 7, 7, 7]:
            #print("Tie!")
            self.winner = "Tie"
            return 1
        else:
            hor = list(self.plateau[pos[0], :])
            ver = list(self.plateau[:, pos[1]])
            diag1, diag2 = self.makeDiagonale(pos)
            if self.consecutif(hor, val) >= 4 or self.consecutif(ver, val) >= 4 or self.consecutif(diag1, val) >= 4 or self.consecutif(diag2, val) >= 4:
                #print("Win!!!")
                return 1
        return 0


    def makeDiagonale(self, pos):
        if pos[1]>=pos[0]:
            ptref = [0,pos[1]-pos[0]]
            diag1 = [self.plateau[ptref[0]+i, ptref[1]+i] for i in range(pos[0]+7-pos[1])]
            extra = list(np.repeat(' ', ptref[1]))
            diag1 = extra + diag1
        else:
            ptref = [pos[0]-pos[1],0]
            diag1 = [self.plateau[ptref[0]+i,ptref[1]+i] for i in range(pos[1]+7-pos[0])]
            extra = list(np.repeat(' ', ptref[0]))
            diag1 = diag1 + extra
        if pos[1]+pos[0]<=6:
            ptref = [pos[1]+pos[0],0]
            diag2 = [self.plateau[ptref[0]-i,ptref[1]+i] for i in range(pos[0]+pos[1]+1)]
            extra = list(np.repeat(' ', 6-ptref[0]))
            diag2 = diag2 + extra
        else:
            ptref = [6,pos[1]-(6-pos[0])]
            diag2 = [self.plateau[ptref[0]-i,ptref[1]+i] for i in range(7-(pos[1]-(6-pos[0])))]
            extra = list(np.repeat(' ', ptref[1]))
            diag2 = extra + diag2
        return diag1, diag2

    def relu(self,x):
        if x<0:
            return 0
        else:
            return x

    def threeinarow(self, L, pt, pat, vert):
        #return the position of the gap if there a 3 pieces in a row
        if vert:
            p = pt[0]
        else:
            p = pt[1]
        maxAlign = 0
        numberOfWindows = 4-abs(p-3)
        for wind in range(numberOfWindows):
            w = L[self.relu(p-3)+wind : self.relu(p-3)+wind+4]
            if w.count(pat) == 3 and w.count(' ') == 1:
                if maxAlign < 3:
                    maxAlign = 3
                a = wind
                b = w
            elif w.count(pat) == 4:
                maxAlign = 4
                break
        if maxAlign == 3:
            return self.relu(p - 3) + a + b.index(' ') + 1
        elif maxAlign == 4:
            return "win"

    def get_heuristic(self, player, line, pat,  pos, vert):
        score = self.threeinarow(line, pos, pat, vert)
        if score == "win" and player == "Player": return -100000
        if score == "win" and player == "ordi": return 10000000
        if score != None:
            newpos=[6-self.colonne[score], score-1]
            self.move(player, score)
            CW2 = self.condWin([newpos[0]-7, newpos[1]])
            if CW2 == 1:
                if player == "Player":
                    self.plateau[newpos[0], newpos[1]] = ' '
                    self.colonne[score] -= 1
                    return -100
                if player == "ordi":
                    self.plateau[newpos[0], newpos[1]] = ' '
                    self.colonne[score] -= 1
                    return 1
            self.plateau[newpos[0], newpos[1]] = ' '
            self.colonne[score] -= 1
        return 0

    def score(self, player, pos):
        if pos[0] != 0:
            pos = [pos[0]+7, pos[1]]
        score = 0
        if player == "Player":
            val = "X"
        else:
            val = "0"
        score += self.get_heuristic(player, list(self.plateau[pos[0], :]), val, pos, False)
        score += self.get_heuristic(player, list(self.plateau[:, pos[1]]), val, pos, True)
        score += self.get_heuristic(player, self.makeDiagonale(pos)[0], val, pos, False)
        score += self.get_heuristic(player, self.makeDiagonale(pos)[1], val, pos, False)
        return score