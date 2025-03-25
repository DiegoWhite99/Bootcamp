#Calcular la calificación final de un estudiante. Los datos disponibles para lectura son calificación 1, equivale al 30% de la nota final, calificacion2, equivale al 20% de la nota final, calificacion3, equivale al 10% de la nota final, calificacion4, equivale al 40% de la nota final de cada uno de los cuatro exámenes presentados. La información que se debe imprimir es el promedio de las calificaciones.#

cali1 = float(input("Ingrese la calificación 1: "))
cali2 = float(input("Ingrese la calificación 2: "))
cali3 = float(input("Ingrese la calificación 3: "))
cali4 = float(input("Ingrese la calificación 4: "))
caliFinal = (cali1 * 0.3) + (cali2 * 0.2) + (cali3 * 0.1) + (cali4 * 0.4)
print("El estudiante saco: ", round(caliFinal, 2))
#---------------------------------------------------------------------------------------------------------------------#
#Calcular el precio de venta de un articulo.se tienen los datos de descripción del artículo el costo de producción. El precio de venta se calcula añadiendo al costo el 120% como utilidad y el 15%de impuesto.#
nameArticle = input("Ingrese el nombre del articulo: ")
costo = float(input("Ingrese el costo de producción: "))
salePrice = costo + (costo * 1.2)
impuesto = (salePrice * 0.15)
totalPrice = salePrice + impuesto
print("El precio de venta del articulo", nameArticle, "es: ", round(totalPrice, 0))
#---------------------------------------------------------------------------------------------------------------------#
#Teniendo en cuenta la cantidad de dólares que va a comprar y el tipo de cambio en pesos (Costo de un dólar en pesos). Calcular la cantidad que debe pagar en pesos por la cantidad de dólares indicada.#
dolares = float(input("Ingrese la cantidad de dolares a comprar: "))
cambio = dolares * 4117.5
print("El valor a pagar en pesos es: ", cambio)