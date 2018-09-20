# a)
val1 = str("druer")
val2 = str("DrUer")

if val1.lower() == val2.lower():
    print("verdiene er like!")
else:
    print(val1, " og ", val2, " er ikke samme")

#b)

navn1 = "Karl Bjarne"
navn2 = "Karl Bernt"

print("Første navn er ", navn1, "og andre navn er", navn2)

if navn1 > navn2:
    print(navn2, "\n", navn1)
else:
    print(navn1, "\n", navn2)
#1: skjekker hva som kommer først av k og b i alfabetet, 2: skjekker hva som kommer først av la og ny i alfabetet, mens 3 skjekker d1 og d2 er alfabetisk eller like

