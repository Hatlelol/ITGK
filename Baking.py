cookies = 48
sukker = 400
smoer = 320
sjokolade = 500
egg = 2
hvetemel = 460

antall = int(input("Hvor mange cookies ønsker du å bake?"))


def oppskrift(x):
    tall = float(x/ cookies)
    print("Antall cookies: ", int(x),
          "\nsukker(g)", sukker * tall,
          "\nsmoer(g)",smoer * tall,
          "\nsjokolade(g)",sjokolade * tall,
          "\negg",egg * tall,
          "\nhvetemel(g)",hvetemel * tall,)
    return


oppskrift(antall)

antall1 = int(input("Hvor mange1?"))
antall2 = int(input("Hvor mange2?"))
antall3 = int(input("Hvor mange3?"))

def oppskrifter(x, y, z):
    tall1 = float(x/cookies)
    tall2 = float(y/cookies)
    tall3 = float(z/cookies)
    print("Antall cookies:", "sukker(g)".rjust(15), "sjokolade(g)".rjust(20),
          "\n", x, str(round(sukker*tall1)).rjust(25), str(round(sjokolade * tall1)).rjust(20),
          "\n", y, str(round(sukker*tall2)).rjust(25), str(round(sjokolade * tall2)).rjust(20),
          "\n", z, str(round(sukker*tall3)).rjust(25), str(round(sjokolade * tall3)).rjust(20),
          )
    return

oppskrifter(antall1, antall2, antall3)


