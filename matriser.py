import random


def random_matrise(bredde, hoyde):
    temp = []
    for i in range(hoyde):
        width = []
        for x in range(bredde):
            width.append(random.randint(1, 9))
        temp.append(width)
    return temp


def print_matrise(val, inp):
    print(inp, "=[")
    for i in range(len(val)):
        print(val[i])
    print("]")


def matrise_addisjon(nr1, nr2):
    if len(nr1) != len(nr2) or len(nr1[0]) != len(nr2[0]):
        print("Matrisene er ikke av samme dimensjon")
    else:
        sum = []
        for i in range(len(nr1)):
            unit = []
            for x in range(len(nr1[0])):
                unit.append(nr1[i][x] + nr2[i][x])
            sum.append(unit)
        return sum


def main():
    A = random_matrise(4, 3)
    print_matrise(A, 'A')
    B = random_matrise(3, 4)
    print_matrise(B, 'B')
    C = random_matrise(3, 4)
    print_matrise(C, 'C')
    D = matrise_addisjon(A, B)
    E = matrise_addisjon(B, C)
    print_matrise(E, 'B+C')


main()
