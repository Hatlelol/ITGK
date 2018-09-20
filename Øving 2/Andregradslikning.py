import math
print("En andregregradslikning på formen ax^2 + bx + c skriv inn for:")
a = int(input("a"))
b = int(input("b"))
c = int(input("c"))

d = ((b**2) - 4*a*c)

def los():
    x_1 = (-b+math.sqrt(d))/(2*a)
    x_2 = (-b-math.sqrt(d))/(2*a)
    if x_1 == x_2:
        print(x_1)
    else:
        print(x_1, "og", x_2)



if d == 0:
    print("En reell dobbeltrot")
    los()
elif d < 0:
    print("To imaginære løsninger")
else:
    print("To reelle løsninger")
    los()
print(d)
