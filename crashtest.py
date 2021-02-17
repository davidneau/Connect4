L=['X', 'X', 'X','X','0','0',' ']
pt=[6,0]
pat='X'
vert = False


def relu(x):
    if x < 0:
        return 0
    else:
        return x

def threeinarow(L, pt, pat, vert):
    # return the position of the gap if there a 3 pieces in a row
    if vert:
        p = pt[0]
    else:
        p = pt[1]
    maxAlign = 0
    numberOfWindows = 4 - abs(p - 3)
    for wind in range(numberOfWindows):
        w = L[relu(p - 3) + wind: relu(p - 3) + wind + 4]
        if w.count(pat) == 3 and w.count(' ') == 1:
            if maxAlign < 3:
                maxAlign = 3
            a = wind
            b = w
        elif w.count(pat) == 4:
            maxAlign = 4
            break
    if maxAlign == 3:
        return relu(p - 3) + a + b.index(' ') + 1
    elif maxAlign == 4:
        return "win"

print(threeinarow(L, pt, pat, vert))