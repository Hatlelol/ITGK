def oppg1():

    print("Jeg elsker ITGK")

    print("Norge")
    print()
    print("Areal (kv.km):", 385180) #Her setter jeg komma mellom tallene og teksten for å skille dem
    print("Folketall (mill.):", 5.3)
    print()
    print('"Jeg elsker itgk" ropte studentene da 1c fungerte') #Bruker '' rundt teksten for å kunne bruke ""
    print()
    #print('hei")
    print("""Noen barn sto og hang ved lekeplassen.""")
    print("""Diskusjonstemaet deres var noe uventet.""")
    print("""- Hvorfor heter'e "Python"?""")
    print("""- Var'e slanger som laget det? - Nei, Guido van Rossum.""")
    print("""- Likte slanger kanskje da? - Nei, digga "Monty Python".""")
    print("""- Hva er det? Et fjell?""")
    print("""- Nei, engelsk komigruppe. Begynte i '69.""")
    print("""- Wow! Var'e fremdeles dinosaurer da?""")
    print()
    print("Heihei, jeg vil visst ikke kompilere jeg :(")
    print("Halla, så 'bra' du ser ut i dag")
    print("Hei på deg")
    print("Er ikke dette gøy?")
    return
def oppg2():
    print("peppes Pizza:")

    pizza = float(100)
    studrabatt = float(0.2)
    tips = float(0.05)
    total = pizza * (1-studrabatt) * (1+tips)
    print("Total pris: ", total)
    #antall = int(input("Hvor mange deltok?"))
    #print("Ettersom dere var ", antall, " personer, så må dere betale ", total / antall, " kr")
    print()
    return

from turtle import *
def oppg3():
    print("geometri")
    r = 5
    print("Vi har en sirkel med radius", r)
    omkrets = format(2 * 3.14 * r, '.2f')
    print("Omkretsen er", omkrets)
    areal = 3.14 * r ** 2
    print("Arealet er", areal)
    h = 8
    volum = areal * h
    print("Sylinder med høyde", h, ": Volumet er ", volum)
    print()
    print("grafikk")


    import time
    # importerer funksjoner fra biblioteket turtle
    begin_fill()
    circle(50)      # sirkel tegnes MOT klokka med radius 50
    circle(-50) # negativ radius: tegner MED klokka
    end_fill()
    color("red")   # setter tegnefargen til rød
    pensize(8)      # setter penntykkelsen til 8
    circle(70)
    circle(-70)
    time.sleep(10)  # Gjør at vinduet med tegningen ikke lukkes med én gang, men er oppe i 10 sekunder
    return

oppg1()
oppg2()
oppg3()
