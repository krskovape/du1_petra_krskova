from turtle import *

speed(0)

#vykreslí hrací pole
p_radku = 3
p_sloupcu = 3
strana = 90
for _ in range(p_sloupcu):
    for _ in range(p_radku):
        for _ in range(4):
            forward(strana)
            left(90)
        forward(strana)
    left(180)
    forward(strana*p_radku)
    right(90)
    forward(strana)
    right(90)
setpos(0,0)

print("Hráči 1, zadej souřadnice pro svůj tah:")
rad = int(input("řádek: "))
sloup = int(input("sloupec: "))
while (rad<1) or (rad>p_radku) or (sloup<1) or (sloup>p_sloupcu):
    print("Souřadnice jsou mimo hrací pole, zadej nové:")
    rad = int(input("řádek: "))
    sloup = int(input("sloupec: "))
       
    

exitonclick()