dager = int(input("Dager til du skal reise?"))


def milla():
    x = input("Er du i militæret / student? (J/N)")
    if x == "J":
        print("Kult prisen din blir da: ", 330)
    else:
        print("Prisen på din billett blir da: ", 440)
def alder():
    aar = int(input("Skriv din alder"))
    if aar <= 16:
        print("Prisen på din billett blir da: ", 220)
    elif aar >= 60:
        print("Prisen på din billett blir da: ", 330)
    else:
        milla()


def minipris():
    var = input("ønskes dette? (J/N)")
    if var == "J":
        print("Ønsker deg en god reise")
    else:
        alder()


if dager >= 14:
    print("Du kan får minipris:", 199, ",- Dette kan ikke refunderes")
    minipris()
else:
    alder()
