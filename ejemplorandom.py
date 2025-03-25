import random
numero=random.randint(1,10)
print(numero)

datos=[]
datos.append(100)
datos.append(200)
datos.append(400)
datos.append(500)
datos.append(500)
datos.append(500)
datos.append(2300)
pos=datos.index(200)
print("El dato esta en", pos)
datos.insert(pos+1,250)

#datos.pop()

contador=datos.count(500)
print("contar un datos ", contador)
print(datos)