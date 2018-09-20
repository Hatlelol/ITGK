def a():
    i = 0
    var = int(0)
    while i < 8:
        kek = int(input("Skriv inn et heltall"))
        var += kek
        i += 1
    print("Summen av tallene blir:", var)

def b():
    x = 1
    y = 1

    while x <= 1000:
        x = x * y
        y += 1
        print(x)

def c():
    z = 0
    q = 1
    while z < 1:
        inp = input("Hva heter hovedstaden til Niue?").lower()
        if inp == "niue city":
            z = 1
            print("Korrekt, du brukte", q, "forsøk")
        else:
            z = 0
            q +=1
            print("Det var feil prøv igjen")



c()

