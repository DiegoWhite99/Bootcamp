def game():
    p1 = input("Nombre jugador 1: ")
    p2 = input("Nombre jugador 2: ")
    scoreP1 = 0
    scoreP2 = 0
    for _ in range(3):
        choose1 = int(input(f"{p1} selecciona una de las siguientes opcines; piedra = 1, papel = 2, tijera = 3: "))
        choose2 = int(input(f"{p2} selecciona una de las siguientes opcines; piedra = 1, papel = 2, tijera = 3: "))
        if choose1 == 1 and choose2 == 3:
            scoreP1 += 10
            print(f"Punto para {p1}")
        elif choose1 == 1 and choose2 == 2:
            scoreP2 += 10
            print(f"Punto para {p2}")
        elif choose1 == 2 and choose2 == 1:
            scoreP1 += 10
            print(f"Punto para {p1}")
        elif choose1 == 2 and choose2 == 3:
            scoreP2 += 10
            print(f"Punto para {p2}")
        elif choose1 == 3 and choose2 == 1:
            scoreP1 += 10
            print(f"Punto para {p1}")
        elif choose1 == 3 and choose2 == 2:
            scoreP2 += 10
            print(f"Punto para {p2}")
        elif choose1 == choose2:
            print("Turno en empate")
        print("_")
    if scoreP1 > scoreP2:
        print(f"El ganador es {p1}")
    elif scoreP2 > scoreP1: 
        print(f"El ganador es {p2}")
    elif scoreP1 == scoreP2:
        print(f"Juego en empate")