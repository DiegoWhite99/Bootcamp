'''edad=int(input('Digite su edad'))

if edad <= 10:
    print('Es menor de edad')
else:
    print('Es mayor de edad')
import math
precio_hora=1500
horas=float(input('Ingrese el numero de horas'))
precio_final=0
if horas > 0.0:
    precio_final=math.ceil(horas)*precio_hora
else:
    precio_final=horas*precio_hora

print(f'El valor a pagar es {precio_final}')

cliente=input('Digite el nombre del cliente ')
unidades=int(input(f'Ingrese las unidades compradas por {cliente} '))
Precio=int(input('Ingrese el precio del producto por docena '))
docenas=int(unidades//12)
unidades_extra=int(unidades/36)
if docenas > 3:
    valor_pagar=Precio*docenas-Precio*docenas*0.15
    unidades=unidades+unidades_extra
    print('El descuento obtenido fue ',Precio*docenas*0.15,'\nEl valor a pagar es ',valor_pagar,'\nEl numero de unidades de obsequio son ',unidades_extra)
else:
    valor_pagar=Precio*docenas-Precio*docenas*0.1
    print('El descuento obtenido fue ', Precio*docenas*0.1,'\nEl valor a pagar es ',valor_pagar,'\nEl numero de unidades de obsequio son ',unidades_extra)

#lower me combierte todo el texto a palabras minusculas
#upper me convierte todo el texto a palabras mayusculas
edad=int(input('Digite su edad'))
sexo=input("Digite m para mujer o h para hombre").lower()

if edad >= 6 and edad <= 12:
    if sexo == "h":
        print('Es un nino pequeno')
    elif sexo == "m"
        print('Es una nina pequena')
    else:
        print(f'Usted digito {sexo} y es un sexo invalido')

elif edad > 12 and edad <= 17:
    print('Es un adolecente')

elif edad > 17 and edad <= 65:
    print('Es un adulto')

elif edad > 65 and edad <= 100:
    print('Es un adulto mayor')

else:
    print('Digite un valor valido')

Obtener el total que tendrá que pagar un alumno si la 
colegiatura para alumnos de profesional es de $300 por 
cada cinco unidades y para alumnos de preparatoria es 
de $180 por cada cinco unidades, de acuerdo a los 
siguientes criterios:  Si el promedio es de 9.5 o más 
y el alumno es de preparatoria, entonces este podrá cursar
55 unidades y se le hará un 25% de descuento.  
Si el promedio es mayor o igual a 9 pero menor que 9.5 
y el alumno es de preparatoria, entonces este podrá 
cursar 50 unidades

nombre = input('Ingrese el nombre del estudiante ')
nivel_educacion = input('Ingrese el valor nivel educativo ').lower()
pago_uno = 300
pago_preparatoria = 180

if nivel_educacion == pago_preparatoria:
    nota = float(input('Ingrese el promedio'))
    if nota >= 9.5:
        pago_total  = (55/5)*pago_preparatoria-(55/5)*pago_preparatoria*0.25
    else:
        pago_total = (50/5)*pago_preparatoria
else:
    nota = float(input('Ingrese el promedio'))
    if nota >= 9.5:
        pago_total  = (55/5)*pago_uno-(55/5)*pago_preparatoria*0.25
    else:
        pago_total = (50/5)*pago_uno
print(f' {nombre} debe pagar {pago_total}')'''

