import random
lista=[]
listados=[]

def lista_aleatoria():
    for _ in range(10):
        numeroRandom=random.randint(50,100)
        lista.append(numeroRandom)
    print(lista)

def lista_aleatoria_dos(t):
    for _ in range(t):
        numeroRandom=random.randint(50,100)
        listados.append(numeroRandom)
    print(listados)

tamano=int(input("Digite el tamaño de la lista"))
lista_aleatoria_dos(tamano)
