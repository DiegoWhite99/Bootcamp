'''
x = 1
while x<10:
    print('Hola')
    x+=1
print('Fin del programa')


suma = 0
while suma <=100:
    num=int(input('Ingrese un numero'))
    suma+=num
print(f'El resultado final es {suma}')'

pares=0
inpares=0
negativos=0
positivos=0

while True:
    x=float(input('Ingrese un numero'))
    if x != 0:
        if x<0:
            negativos+=x
        elif x>0:
            positivos+=x
            if x%2 == 0:
                pares+=x
            else:
                inpares+=x
    else:
        break
print(f'Los numeros pares son: {pares} \nLos numeros inpares son: {inpares} \nLos numeros negativos son: {negativos} \nLos numeros positivos son: {positivos}')
'''
precio_hoja=int(input('Ingrese el precio por hojas'))
valor_final=0
precio_descuento=0
while True:
    pregunta = input('Quieres continuar? ').lower()
    if pregunta != 'no':
        cliente = input('Ingrese el nombre del cliente ')
        tipo = int(input('Ingrese el tipo que es 1, 2, 3 o 4'))
        cantidad = int(input('Ingrese la cantidad de hojas'))
        if tipo == 1:
            valor_final=cantidad*precio_hoja-cantidad*precio_hoja*0.05
            precio_descuento=valor_final/cantidad
        elif tipo == 2:
            valor_final=cantidad*precio_hoja-cantidad*precio_hoja*0.1
            precio_descuento=valor_final/cantidad
        elif tipo == 3:
            valor_final=cantidad*precio_hoja-cantidad*precio_hoja*0.12
            precio_descuento=valor_final/cantidad
        elif tipo == 4:
            valor_final=cantidad*precio_hoja-cantidad*precio_hoja*0.05
            precio_descuento=valor_final/cantidad
    else:
        break


