from turtle import speed, penup, pendown, setpos, forward, left, right, write, pensize, circle, exitonclick
from math import sqrt

speed(0)

print("Vítej u hry PIŠKVORKY")

#zadání počtu řádků, sloupců a velikosti strany políčka
p_radku = int(input("Zadej počet řádků herního pole: "))
p_sloupcu = int(input("Zadej počet sloupců herního pole: "))
strana = 60

#ošetření toho, že zadaný počet řádků a sloupců není nulový nebo záporný
while (p_radku<1) or (p_sloupcu<1):
    print("Neplatná velikost hracího pole, zadej nové:")
    p_radku = int(input("Počet řádků herního pole: "))
    p_sloupcu = int(input("Počet sloupců herního pole: "))

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

#samotná hra
p_tahu=p_radku*p_sloupcu

for i in range(1, p_tahu+1):   
    #vypsání tahu
    print("Tah",i,"z",p_tahu)

    #zjištění, který hráč je na tahu a výzva k zadání souřadnic
    if (i%2!=0):
        print("Hráči 1, zadej souřadnice pro svůj tah:")
    elif (i%2==0):
        print("Hráči 2, zadej souřadnice pro svůj tah:")
    
    #načtení souřadnic od hráče a ošetření toho, že nejsou mimo hrací pole
    rad = int(input("řádek: "))
    sloup = int(input("sloupec: "))
    while (rad<1) or (rad>p_radku) or (sloup<1) or (sloup>p_sloupcu):
        print("Souřadnice jsou mimo hrací pole, zadej nové:")
        rad = int(input("řádek: "))
        sloup = int(input("sloupec: "))

    #vykreslení křížku nebo kolečka podle pořadí hráče
    penup()
    x= a + ((strana/2) + 1.5*strana*(sloup-1))
    y= b + (sqrt(3)/2.3)*strana*(sloup) + (sqrt(3))*strana*(rad-1)
    setpos(x, y)
    pendown()
    if (i%2!=0):
        write("X", align="center", font=["Arial", 30, "normal"])
    elif (i%2==0):
        pensize(3)
        circle(20)
    penup()       
    setpos(a,b)

print("KONEC HRY")

exitonclick()