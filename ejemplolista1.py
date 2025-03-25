numeros_pares = []
numeros_impares = []

# Pedimos al usuario la cantidad de números que desea ingresar
cantidad = int(input('¿Cuántos números desea ingresar? '))

# Recorremos la cantidad de números indicada por el usuario
for i in range(cantidad):
    numero = int(input(f'Ingrese el número {i + 1}: '))
    if numero % 2 == 0:
        numeros_pares.append(numero)  # Clasificamos como par
    else:
        numeros_impares.append(numero)  # Clasificamos como impar

# Calculamos las sumas de las listas
suma_pares = sum(numeros_pares)
suma_impares = sum(numeros_impares)

# Mostramos los resultados
print(f'Números pares: {numeros_pares}')
print(f'Suma de números pares: {suma_pares}')
print(f'Números impares: {numeros_impares}')
print(f'Suma de números impares: {suma_impares}')