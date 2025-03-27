import random

def lanzar_dados():
    """Lanza dos dados y devuelve su suma"""
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2, dado1 + dado2

def craps():
    """Simula el juego de Craps"""
    print("¡Bienvenido a Craps!")
    
    dado1, dado2, suma = lanzar_dados()
    print(f"Tiraste {dado1} y {dado2}, suma: {suma}")


    if suma in [7, 11]:
        print("¡Ganaste!")
        return
    elif suma in [2, 3, 12]:
        print("¡Perdiste!")
        return
    else:
        punto = suma
        print(f"Tu punto es {punto}. Debes seguir lanzando hasta sacar {punto} o un 7.")

    
    while True:
        input("Presiona Enter para lanzar los dados...")
        dado1, dado2, nueva_suma = lanzar_dados()
        print(f"Tiraste {dado1} y {dado2}, suma: {nueva_suma}")

        if nueva_suma == punto:
            print("¡Ganaste!")
            break
        elif nueva_suma == 7:
            print("¡Perdiste!")
            break

craps()
