pos = input("skriv posisjon")  # byttes ut med en input()-setning

bokstav = pos[0].lower()  # gir variabelen bokstav verdi 'a'

tall = int(pos[1])

odd = ["a", "c", "e", "g"]
parr = ["b", "d", "f", "h"]
var = 0

for x in odd:
    if bokstav == x:
       var = 0

for x in parr:
    if bokstav == x:
        var = 1

if (tall % 2 == 0 and var == 0) or (tall % 2 == 1 and var == 1):
    print("hvit")
elif (tall % 2 == 0 and var == 1) or (tall % 2 == 1 and var == 0):
    print("Sort")
else:
    print("feil")

