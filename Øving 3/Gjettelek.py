import random
opp = int(input("Øvre grense for tall"))
ned = int(input("Nedre grense for tall"))

tilfeldigtall = random.randint(ned, opp)
tall = str("meme")

while tilfeldigtall != tall:
    tall = int(input("gjett!"))
    if tall == tilfeldigtall:
        print("gratulerer!", tall, tilfeldigtall)
    elif tilfeldigtall > tall:
        print("Korrekt tall er høyere!")
    elif tilfeldigtall < tall:
        print("Korrekt tall er lavere!")
    else:
        print("feil")
