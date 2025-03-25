'''edad=15
estatura= 1.80
nombre = 'Ramon'
booleanas =True

print(type(edad))
print(type(estatura))
print(type(nombre))
print(type(booleanas))

nombre=input('Digite el nombre\n')
nota_uno=float(input('Ingrese el valor de la nota uno '))
nota_dos=float(input('Ingrese el valor de la nota 2 '))
nota_tres=float(input('Ingrese el valor de la nota 3 '))
nota_cuatro=float(input('Ingrese el valor de la nota 4 '))

suma_notas=(nota_uno+nota_dos+nota_tres+nota_cuatro)/4

print('El promedio de las notas es', suma_notas)
print(f'El promedio es {suma_notas}')


dolares=int(input('Digite el valor de dolares que necesita'))
cambio=4100
peso = dolares*cambio

print(f'Usted necesita {peso} pesos para la cantidad de dolares solicitada')


costos=int(input('Digite el valor de los costos del proucto'))
precioventa=costos+costos*1.2+(costos*1.2)*0.15
print(f'El precio de venta es {precioventa}')'''

estudiante=input('Ingrese su nombre')
nota_uno=float(input('Ingrese el valor de la nota uno '))
nota_dos=float(input('Digite el valor de la nota 2 '))
nota_tres=float(input('Ingrese el valor de la nota tres '))
nota_cuatro=((nota_uno+nota_dos+nota_tres)/3)*0.4
print(nota_cuatro)
nota_final=nota_uno*0.3+nota_dos*0.2+nota_tres*0.1+nota_cuatro

print(f'Su nota final es {nota_final}')
