dato = int(input("Skriv en dato"))
month = input("Skriv inn måned")
month = month.lower()
aar = ["januar", "februar", "mars", "april", "mai", "juni", "juli", "august", "september", "oktober", "november",
       "desember"]

for x in range(0, len(aar)): #lager en for løkke for å bestemme måneden med et tall
    if month == aar[x]:
        month = int(x)

val = month*100 + dato #gir datoen en verdi med tre eller fire siffer for å representere dato og måned i samme variabel

vaar = 220
sommer = 521
host = 822
vinter = 1121

if vaar <= val < sommer:
    print("Vår")
elif sommer <= val < host:
    print("Sommer")
elif host <= val < vinter:
    print("host")
elif 0 < val > 1131:
    print("skriv inn noe gyldig")
else:
    print("vinter")
