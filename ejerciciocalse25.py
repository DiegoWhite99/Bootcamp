#Vamos a crear un programa que tenga el siguiente menú:
#Añadir número a la lista: Me pide un número de la lista y lo añade al final de la lista.

#Añadir número de la lista en una posición: Me pide un número y una posición, y si la posición existe en la lista lo añade a ella (la posición se pide a partir de 1).

#Longitud de la lista: te muestra el número de elementos de la lista.12

#Eliminar el último número: Muestra el último número de la lista y lo borra.

#Eliminar un número: Pide una posición, y si la posición existe en la lista lo borra de ella (la posición se pide a partir de 1).

#Contar números: Te pide un número y te dice cuantas apariciones hay en la lista.

#Posiciones de un número: Te pide un número y te dice en que posiciones está (contando desde 1).

#Mostrar números: Muestra los números de la lista


lista = []

while True:  # Ciclo infinito para mostrar el menú hasta que el usuario elija salir
    print("\nMenú:")
    print("1. Añadir número a la lista")
    print("2. Añadir número en una posición específica")
    print("3. Mostrar la longitud de la lista")
    print("4. Eliminar el último número")
    print("5. Eliminar un número en una posición")
    print("6. Contar ocurrencias de un número")
    print("7. Mostrar posiciones de un número")
    print("8. Mostrar la lista")
    print("9. Salir")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        numero = int(input("Ingrese un número: "))
        lista.append(numero)  # Agrega el número al final de la lista
        print("Número agregado correctamente.")
        
    elif opcion == "2":
        numero = int(input("Ingrese un número: "))
        posicion = int(input("Ingrese una posición: "))
        if 1 <= posicion <= len(lista) + 1:
            lista.insert(posicion - 1, numero)  # Inserta en la posición indicada
            print("Número insertado correctamente.")
        else:
            print("Posición inválida.")

    elif opcion == "3":
        print("La lista tiene", len(lista), "elementos.")

    elif opcion == "4":
        if lista:
            print("El último número eliminado fue:", lista.pop())  # Elimina el último número
        else:
            print("La lista está vacía, no hay nada que eliminar.")

    elif opcion == "5":
        posicion = int(input("Ingrese la posición a eliminar: "))
        if 1 <= posicion <= len(lista):
            eliminado = lista.pop(posicion - 1)  # Guarda y elimina el número
            print("Número", eliminado, "eliminado de la posición", posicion)
        else:
            print("Posición inválida.")

    elif opcion == "6":
        numero = int(input("Ingrese un número: "))
        print("El número", numero, "aparece", lista.count(numero), "veces en la lista.")

    elif opcion == "7":
        numero = int(input("Ingrese un número: "))
        posiciones = [i + 1 for i in range(len(lista)) if lista[i] == numero]  # Guarda las posiciones donde aparece
        if posiciones:
            print("El número", numero, "está en las posiciones:", posiciones)
        else:
            print("El número no está en la lista.")

    elif opcion == "8":
        if lista:
            print("Los números en la lista son:", lista)
        else:
            print("La lista está vacía.")

    elif opcion == "9":
        print("Fin del programa.")
        break  # Sale del bucle y termina el programa

    else:
        print("Opción inválida, intente de nuevo.")
    
    input("Presiona Enter para continuar...")  # Pausa antes de volver al menú



    






        


























