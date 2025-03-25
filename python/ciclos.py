'''
x = 1

while x < 10:
    print(f"Hola - x vale {x}")  # Muestra el valor de x en cada iteración
    x += 1
print("Fin del programa")
'''
'''
numero = 0

while numero <= 100:
    numero_suma = int(input('Ingrese el numero: '))
    numero += numero_suma
    print(f"El resultado parcial es: {numero}")

print(f"El resultado final es: {numero}") '''


'''
suma_negativos = 0
suma_positivos = 0
suma_pares = 0
suma_impares = 0

while True:
    n = int(input('Ingrese un número (0 para terminar): '))

    if n == 0:
        break

    if n < 0:
        suma_negativos += n
    else:
        suma_positivos += n

    if n % 2 == 0:
        suma_pares += n
    else:
        suma_impares += n

print(f"Suma de números negativos: {suma_negativos}")
print(f"Suma de números positivos: {suma_positivos}")
print(f"Suma de números pares: {suma_pares}")
print(f"Suma de números impares: {suma_impares}")
'''

#El sueldo que perciben 10 vendedores de una empresa automotriz está integrado de la siguiente manera: el
#salario mínimo, mas $ 100.000 por cada auto vendido más el 2% del valor de los autos vendidos. Debe realizar
#un algoritmo que imprima el nombre del vendedor que tuvo el mayor sueldo, suponiendo que no hay
#cantidades iguales de total de venta.


