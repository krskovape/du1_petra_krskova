from turtle import *
from math import sqrt

speed(0)

p_sloupcu=3
p_radku=3
strana=60

#posunutí počátku sítě
penup()
a = -((strana)*p_sloupcu)
b = -((strana)*p_radku)
setpos(a,b)
pendown()

#vykreslení sítě
for _ in range(p_radku):
    for _ in range(p_sloupcu):
        for _ in range(8):
            forward(strana)
            left(60)
        right(120)
    right(120)
    for _ in range(p_sloupcu):
        forward(strana)
        right(60)
        forward(strana)
        left(60)
    right(120)
    forward(strana)
    right(60)
    forward(strana)
    right(60)
penup()
setpos(a,b)
pendown()

rad=2
sloup=2
x= a + ((strana/2) + 1.5*strana*(sloup-1))
y= b + ((strana) + 2*strana*(rad-1))
setpos(x, y)

exitonclick()