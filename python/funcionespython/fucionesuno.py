import random

lista = []
listado=[]

def listaaleatoria():
    for _ in range(10):
        numeroRandom=random.randint(50,100)
        lista.append(numeroRandom)
    print(lista)



def lista_aleatoria_dos(tamano):
    for _ in range(tamano):
        numero_random = random.randint(50, 100)
        lista.append(numero_random)
    print(listado)
    

