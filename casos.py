while True:
    print('Seleccione el algoritmo que quiere ejecutar')
    print('1. Suma\n2. Resta\n3. Multiplicacion\n4. Division\n5. Salir')
    opcion = int(input('Digite su opcion '))

    if opcion == 1:
        numero_uno = int(input('Digite su numero '))
        numero_dos = int(input('Digite un numero '))
        respuesta = numero_uno + numero_dos
        print(f'El resultado de la suma es: {respuesta}')
    elif opcion == 2:
        numero_uno = int(input('Digite su numero '))
        numero_dos = int(input('Digite un numero '))
        respuesta = numero_uno - numero_dos
        print(f'El resultado de la resta es: {respuesta}')
    elif opcion==3:
        numero_uno = int(input('Digite su numero '))
        numero_dos = int(input('Digite un numero '))
        respuesta = numero_uno * numero_dos
        print(f'El resultado de la multiplicacion es: {respuesta}')
    elif opcion == 4:
        numero_uno = int(input('Digite su numero '))
        numero_dos = int(input('Digite un numero '))
        respuesta = numero_uno / numero_dos
        print(f'El resultado de la division es: {respuesta}')
    else:
        break
