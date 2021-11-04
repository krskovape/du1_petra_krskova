from turtle import speed, penup, pendown, setpos, forward, left, right, write, pensize, circle, exitonclick

speed(0)

print("Vítej u hry PIŠKVORKY")

#zadání počtu řádků, sloupců a velikosti strany políčka
p_radku = int(input("Zadej počet řádků herního pole: "))
p_sloupcu = int(input("Zadej počet sloupců herního pole: "))
strana = 90

#ošetření toho, že zadaný počet řádků a sloupců není nulový nebo záporný
while (p_radku<1) or (p_sloupcu<1):
    print("Neplatná velikost hracího pole, zadej nové:")
    p_radku = int(input("Počet řádků herního pole: "))
    p_sloupcu = int(input("Počet sloupců herního pole: "))

#nastavení počátku tak, aby se střed hracího pole zobrazoval doprostřed okna
penup()
a = -((strana/2)*p_sloupcu)
b = -((strana/2)*p_radku)
setpos(a,b)
pendown()

#vykreslení hracího pole
for _ in range(p_radku):
    for _ in range(p_sloupcu):
        for _ in range(4):
            forward(strana)
            left(90)
        forward(strana)
    left(180)
    forward(strana*p_sloupcu)
    right(90)
    forward(strana)
    right(90)
setpos(a,b)

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
    x= a + ((strana/2) + strana*(sloup-1))
    y= b + ((strana/4) + strana*(rad-1))
    setpos(x, y)
    pendown()
    if (i%2!=0):
        vel_pisma=int(strana/3)
        write("X", align="center", font=["Arial", vel_pisma, "normal"])
    elif (i%2==0):
        vel_pisma=int(strana/2.5)
        write("O", align="center", font=["Arial", vel_pisma, "normal"])
    penup()       
    setpos(a,b)

print("KONEC HRY")

exitonclick()