# En un estacionamiento cobran $ 1.500 por hora o fracción. Diseñe un algoritmo que determine cuanto debe pagar un cliente por el estacionamiento de su vehículo, conociendo el tiempo de estacionamiento en horas y minutos.
# estacionamiento = int(input("Ingrese el tiempo de estacionamiento en horas: "))
# pay = 1500 * estacionamiento
# print("El tiempo transcurrido en horas es de ", estacionamiento, ", en minutos fue de ",estacionamiento * 60," y el valor a pagar es: ", pay)
# -------------------------------------------------------------------------------------------
# Ingresar el nombre de un empleado, las horas trabajadas, luego Calcular pago bruto 8.000 pesos por hora trabajada y total a pagar, presentar los resultados del programa. Nota: el seguro social es de 8.5% del total de lo que recibe si el sueldo es mayor 700.000 sino es el 3.5% del sueldo del empleado.
# employeeName = input("Ingrese el nombre del empleado: ")
# hours = int(input("Ingrese las horas trabajadas: "))
# pay = 8000 * hours
# socialSecure = 0
# if pay > 700000:
#     discount = "8.5%"
#     socialSecure = pay * 0.085
# else:
#     discount = "3.5%"
#     socialSecure = pay * 0.035
# totalPay = pay - socialSecure
# print("El empleado ", employeeName, "trabajo ", hours, " horas, el valor a pagar es: ", pay, " y el total a pagar es: ", totalPay, " aplicando el descuento de segura social en un ", discount)
# ---------------------------------------------------------------------------------------------------------------------
# Un supermercado ha puesto en oferta la venta al por mayor de cierto producto, ofreciendo un descuento del 15% por la compra de más de 3 docenas y 10% en caso contrario. Además, por la compra de más de 3 docenas se obsequia una unidad del producto por cada tres docenas. Diseñe un algoritmo que determine el monto de la compra, el monto del descuento, el monto a pagar y el número de unidades de obsequio por la compra de cierta cantidad de docenas del producto.
# cantidadDocenas = int(input("Ingrese la cantidad de docenas a comprar: "))
# if cantidadDocenas > 3:
#     discount = 0.15
#     gift = (cantidadDocenas * 12) // 3
# else:
#     gift = 0
#     discount = 0.10
# print("El descuento aplicado es de: ", discount * 100, "% y el número de unidades de obsequio es: ", gift, " por lo tanto el monto total es de: ", (cantidadDocenas * 12) + gift, " unidades pagando por el valor de ", (cantidadDocenas * 12) - (discount *(cantidadDocenas * 12)) , " cada una.")
# ---------------------------------------------------------------------------------------------------------------------
# En un juego de preguntas a las que se responde Si o No gana quien responda correctamente las tres preguntas. Si se responde mal a cualquiera de ellas ya no se pregunta la siguiente y termina el juego. Las preguntas son:  ¿Colon descubrió América?  ¿La independencia de México fue en el año 1810?  ¿The Doors fue un grupo de rock Americano?
def juego_preguntas():
    quetion1 = input("¿Colon descubrió América? ")
    if quetion1 == "Si" or quetion1 == "si" or quetion1 == "SI":
        print("Bien hecho!!, siguiente pregunta")
        quetion2 = input("¿La independencia de México fue en el año 1810? ")
        if quetion2 == "No" or quetion2 == "no" or quetion2 == "NO":
            print("Bien hecho!!, siguiente pregunta")
            quetion3 = input("¿The Doors fue un grupo de rock Americano? ")
            if quetion3 == "Si" or quetion3 == "si" or quetion3 == "SI":
                print("Ganaste!!")
            else:
                print("Perdiste")
                return
        else:
            print("Perdiste")
            return
    else:
        print("Perdiste")
        return
juego_preguntas()
# Obtener el total que tendrá que pagar un alumno si la colegiatura para alumnos de profesional es de $300 por cada cinco unidades y para alumnos de preparatoria es de $180 por cada cinco unidades, de acuerdo a los siguientes criterios:  Si el promedio es de 9.5 o más y el alumno es de preparatoria, entonces este podrá cursar 55 unidades y se le hará un 25% de descuento.  Si el promedio es mayor o igual a 9 pero menor que 9.5 y el alumno es de preparatoria, entonces este podrá cursar 50 unidades