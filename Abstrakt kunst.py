from turtle import *

# setter opp tegnevinduet
setup(330, 330, 0, 0)
screensize(315, 315)
goto(-60, 150)

bakgrunn = input("Bakgrunnsfarge?")
firkant = input("Firkantfarge?")

# velger farger
bgcolor(bakgrunn)
color(firkant)

# tegner den indre firkanten
begin_fill()
right(10)  # tilter den 10 grader nedover
forward(200)
right(90)
forward(200)
right(90)
forward(200)
right(90)
forward(200)
end_fill()
