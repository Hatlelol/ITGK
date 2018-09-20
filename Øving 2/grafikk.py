import time
from turtle import *

# importerer funksjoner fra turtle
print("Hei, jeg kan tegne en trekant")
pen = input("Velg pennfarge, NTNU-rosa(R) eller NTNU-oransje (O)")
fill = input("Velg fyllfarge, lilla (L), turkis(T) eller gul(G)")
var = input("Ønsker du spissen på trekanten opp eller ned? (O/N)").lower()
pensize(7)  # sett pennen 7 piksler tykk

if pen == "R":
    pencolor("#ad207e")  # sett pennefargen til rosa
elif pen == "O":
    pencolor("#f58025")
else:
    print("Feil input")

bgcolor("grey")  # sett bakgrunnsfargen grå

if fill == "L":
    fillcolor("#552988")
elif fill == "T":
    fillcolor("#5cbec9")
elif fill == "G":
    fillcolor("#d5d10e")
else:
    print("Feil input fill")
# Tegner en fylt trekant
begin_fill()
forward(200)  # gå 100 piksler framover
if var == "o":
    left(120)  # drei 120 grader venstre
    forward(200)
    left(120)
    forward(200)
elif var == "n":
    right(120)
    forward(200)
    right(120)
    forward(200)
else:
    print("Du svarte feil")
end_fill()

# Holder vinduet med tegningen åpent i 10 sekunder. Ha dette som siste linje i koden din
time.sleep(10)