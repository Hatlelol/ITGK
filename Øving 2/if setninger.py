tid = int(input("Hvor mange minutter har kaken stått i ovnen?"))
if(tid >= 50):
    print("Kaken kan tas ut av ovnen")
else:
    print("Vent i ", 50 - tid, " minutter")
print("tips til servering: vaniljeis")

epler = int(input("Hvor mange epler har du? "))
barn = int(input("Hvor mange barn passer du? "))
if barn > 0:
    print("Da blir det", epler // barn, "epler til hvert barn")
    print("og", epler % barn, "epler til overs til deg selv.")
print("Takk for i dag!")

alder = int(input("skriv inn din alder:"))
if alder >= 18:
    print("Du kan stemme")
elif alder >=16:
    print("Du kan stemme i lokalvalg, men ikke stortingsvalg")
else:
    print("Du kan ikke stemme")
aar = int(input("Hvor gammel er du?"))
if aar >= 67:
    print("40kr")
elif aar >= 26:
    print("80kr")
elif aar >= 12:
    print("50kr")
elif aar >= 3:
    print("30kr")
else:
    print("gratis :)")