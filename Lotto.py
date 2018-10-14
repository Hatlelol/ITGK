import random

numbers = []
ans = []
ex = []
myGuess = [1, 2, 3, 4, 5, 6, 7]
for i in range(1, 35):
    numbers.append(i)


def skjekktall():
    tall = random.randint(1, 34)
    if tall in ans:
        skjekktall()
    else:
        ans.append(tall)


def skjekkekstra():
    tall = random.randint(1, 34)
    if tall in ex or tall in ans:
        skjekkekstra()
    else:
        ex.append(tall)


def lotto(m, n):
    for i in range(m):
        skjekktall()
    for i in range(n):
        skjekkekstra()
    arr = [ans, ex]
    return arr


def complist(guess, result):
    x = []
    y = []
    for i in result[0]:
        if i in guess:
            x.append(i)
    for i in result[1]:
        if i in guess:
            y.append(i)
    z = [len(x), len(y)]
    return z


def winning(val):
    ord = val[0]
    til = val[1]
    if ord == 7: return 2749455
    elif ord == 6 and til >= 1: return 102110
    elif ord == 6: return 3385
    elif ord == 5: return 95
    elif ord == 4 and til >= 1: return 45
    else: return 0


def main():
    return winning(complist(myGuess, lotto(7, 3)))-5


print(main())
