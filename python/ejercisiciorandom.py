import random
lista = []
numero_buscar = int(input("Digite el numero que desee buscar en la lista\n"))
for i in range(20):
    numero_random = random.randint(1,20)
    lista.append(numero_random)
contador = lista.count(numero_buscar)
print(lista)
if numero_buscar > 0:
    print(f"El numero {numero_buscar} se repite: {contador} Veces")
else:
    print("El numero no esta en la lista")