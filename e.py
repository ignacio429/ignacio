#uso y explicacion de random
#import random
#j1=random.randint(60,190)

#j2=random.randint(60,190)

#j3=rando,.randint(60,190)
#print(f"el jugador 1 lanzo la pelota a {j1}metros")
#print(f"el jugador 1 lanzo la pelota a {j2}metros")
# print(f"el jugador 1 lanzo la pelota a {j3}metros")

# if j1>j2 and j1>j3
# print(f"el jugador 1 lanzó la pelota más lejos")
# elif j2>j1 and j2>j3:
# print(f"el jugador 2 lanzó la pelota más lejos")
# elif j3>j1 and j3>j2:
# print(f"el jugador 3 lanzó la pelota más lejos")

# # tirar 2 dados
# dado=random.randint(1,6)
# print(f"el dado dio{dado}")

# #si los dados dan el mismo número, el jugador se va a la carcel
# dado=random.randint(1,6)
# print(f"el dado dio{dado}")
# dado2=random.randint(1,6)
# print(f"el dado dio{dado}")
# if dado==dado2



#ludo

posicion=0
meta=50
while posicion<meta:
    dado1=random.randit(1,6)
    dado2=random.randit(1,6)
    print(f"el dado dio{dado1}")
    print(f"el dado dio{dado2}")
    posicion+=dado1+dado2
    time.sleep(1)
    print(f"el jugador esta en la pocision {posicion}")
    turnos+=1
    print(f"ha llegado a la meta en {turnos} turnos")


