import random

lista = []
def listaaleatoria():
    for _ in range(10):
        numeroRandom=random.randint(50,100)
        lista.append(numeroRandom)
print(lista)

def lista_aleatoria_dos(t):
    for _ in range(t):
        numero_random = random.randint(50, 100)
        lista.append(numero_random)
    print(f"Lista generada con tamaño dinámico ({t} elementos):", lista)

tamano = int(input("Digite el tamaño de la lista: "))
lista_aleatoria_dos(tamano)

listaaleatoria()    