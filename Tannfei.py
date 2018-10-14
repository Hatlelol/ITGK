teeth = [95,103,71,99,114,64,95,53,97,114,109,11,2,21,45,2,26,81,54,14,118,108,117,27,115,43,70,58,107]
ut = []

def regnut(x):
    temp = []
    temp.append(int((x - x % 20)/20))
    x = x % 20
    temp.append(int((x - x % 10)/10))
    x = x % 10
    temp.append(int((x - x % 5)/5))
    x = x % 5
    temp.append(x)
    ut.append(temp)


for i in teeth:
    regnut(i)


for i in range(len(ut)):
    print("20:", ut[i][0], ", 10:", ut[i][1], ", 5:", ut[i][2], ", 1:", ut[i][3])