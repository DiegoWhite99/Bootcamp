'''while True:
    print('Menu de opciones')
    print('1. Suma\n2. Resta\n3. Multiplicacion\n4. Division\n5. Salir')
    opcion = int(input('Digite su opcion '))
    
    match opcion:

        case 1:
            numero_uno = int(input('Digite su numero '))
            numero_dos = int(input('Digite un numero '))
            respuesta = numero_uno + numero_dos
            print(f'El resultado de la suma es: {respuesta}')
        case 2:
            numero_uno = int(input('Digite su numero '))
            numero_dos = int(input('Digite un numero '))
            respuesta = numero_uno - numero_dos
            print(f'El resultado de la resta es: {respuesta}')
        case 3:
            numero_uno = int(input('Digite su numero '))
            numero_dos = int(input('Digite un numero '))
            respuesta = numero_uno * numero_dos
            print(f'El resultado de la multiplicacion es: {respuesta}')
        case 4:
            numero_uno = int(input('Digite su numero '))
            numero_dos = int(input('Digite un numero '))
            respuesta = numero_uno / numero_dos
            print(f'El resultado de la division es: {respuesta}')
        case _:
            break

7. Debe hacer un programa que indique el valor de alquiler de cualquiera de los vehículos relacionados en la tabla, dependiendo del número de días de alquiler existe un descuento que se
relaciona en la segunda tabla, y el cliente puede sí o no tomar un seguro. Se debe mostrar total de alquiler descuento y si toma el seguro o no
- Los precios del alquiler son los siguientes:
'''

""" nombre_cliente = input('Ingrese el nombre del cliente ')
tiempo = int(input('Por cuanto tiempo necesitas el vehiculo '))
valor_total=0
bmw = 650000*tiempo
megane = 120000*tiempo
mercedez = 700000*tiempo
twingo = 100000*tiempo
chevrolet_aveo = 150000*tiempo
while True:
    print(f'Bienvenido {nombre_cliente}\nEstas son las opciones: ')
    
    if tiempo >= 3 and tiempo <= 5:
        print('1. BMW\n2. MEGANE\n3. MERCEDEZ\n4. TWINGO \n5. CHEVROLET AVEO\n6. Salir')
        opcion = int(input('Digite la opcion '))
    
        match opcion:

            case 1:
            
                seguro = input('Desea incluir seguro todo riesgo? si/no ').lower()
                if seguro == 'si':
                    valor_total=bmw-bmw*0.1+bmw*0.05
                else:
                    valor_total=bmw-bmw*0.1
            case 2:
                seguro = input('Desea incluir seguro todo riesgo? ').lower()
                if seguro == 'si':
                    valor_total=megane-megane*0.1+megane*0.05
                else:
                    valor_total=megane-megane*0.1
            case 3:
                seguro = input('Desea incluir seguro todo riesgo? ').lower()
                if seguro == 'si':
                    valor_total=mercedez-mercedez*0.1+mercedez*0.05
                else:
                    valor_total=mercedez-mercedez*0.1
            case 4:
                seguro = input('Desea incluir seguro todo riesgo? ').lower()
                if seguro == 'si':
                    valor_total=twingo-twingo*0.1+twingo*0.05
                else:
                    valor_total=twingo-twingo*0.1
            case 5:
                seguro = input('Desea incluir seguro todo riesgo? ').lower()
                if seguro == 'si':
                    valor_total=chevrolet_aveo-chevrolet_aveo*0.1+chevrolet_aveo*0.05
                else:
                    valor_total=chevrolet_aveo-chevrolet_aveo*0.1
            case _:
                break
    elif tiempo >= 6 and tiempo <= 10:
        match opcion:

            case 1:
                seguro = input('Desea incluir seguro todo riesgo? ').lower()
                if seguro == 'si':
                    valor_total=bmw-bmw*0.15+bmw*0.05
                else:
                    valor_total=bmw-bmw*0.15
            case 2:
                seguro = input('Desea incluir seguro todo riesgo? ').lower()
                if seguro == 'si':
                    valor_total=megane-megane*0.15+megane*0.05
                else:
                    valor_total=megane-megane*0.15
            case 3:
                seguro = input('Desea incluir seguro todo riesgo? ').lower()
                if seguro == 'si':
                    valor_total=mercedez-mercedez*0.15+mercedez*0.05
                else:
                    valor_total=mercedez-mercedez*0.15
            case 4:
                seguro = input('Desea incluir seguro todo riesgo? ').lower()
                if seguro == 'si':
                    valor_total=twingo-twingo*0.15+twingo*0.05
                else:
                    valor_total=twingo-twingo*0.15
            case 5:
                seguro = input('Desea incluir seguro todo riesgo? ').lower()
                if seguro == 'si':
                    valor_total=chevrolet_aveo-chevrolet_aveo*0.15+chevrolet_aveo*0.05
                else:
                    valor_total=chevrolet_aveo-chevrolet_aveo*0.15
            case _:
                break
    
    elif tiempo >= 6 and tiempo <= 10:
        match opcion:

            case 1:
                seguro = input('Desea incluir seguro todo riesgo? ').lower()
                if seguro == 'si':
                    valor_total=bmw-bmw*0.2+bmw*0.05
                else:
                    valor_total=bmw-bmw*0.2
            case 2:
                seguro = input('Desea incluir seguro todo riesgo? ').lower()
                if seguro == 'si':
                    valor_total=megane-megane*0.2+megane*0.05
                else:
                    valor_total=megane-megane*0.2
            case 3:
                seguro = input('Desea incluir seguro todo riesgo? ').lower()
                if seguro == 'si':
                    valor_total=mercedez-mercedez*0.2+mercedez*0.05
                else:
                    valor_total=mercedez-mercedez*0.2
            case 4:
                seguro = input('Desea incluir seguro todo riesgo? ').lower()
                if seguro == 'si':
                    valor_total=twingo-twingo*0.2+twingo*0.05
                else:
                    valor_total=twingo-twingo*0.2
            case 5:
                seguro = input('Desea incluir seguro todo riesgo? ').lower()
                if seguro == 'si':
                    valor_total=chevrolet_aveo-chevrolet_aveo*0.2+chevrolet_aveo*0.05
                else:
                    valor_total=chevrolet_aveo-chevrolet_aveo*0.2
            case _:
                break
    
    else:
        match opcion:

            case 1:
                seguro = input('Desea incluir seguro todo riesgo? ').lower()
                if seguro == 'si':
                    valor_total=bmw+bmw*0.05
                else:
                    valor_total=bmw
            case 2:
                seguro = input('Desea incluir seguro todo riesgo? ').lower()
                if seguro == 'si':
                    valor_total=megane+megane*0.05
                else:
                    valor_total=megane
            case 3:
                seguro = input('Desea incluir seguro todo riesgo? ').lower()
                if seguro == 'si':
                    valor_total=mercedez+mercedez*0.05
                else:
                    valor_total=mercedez
            case 4:
                seguro = input('Desea incluir seguro todo riesgo? ').lower()
                if seguro == 'si':
                    valor_total=twingo+twingo*0.05
                else:
                    valor_total=twingo
            case 5:
                seguro = input('Desea incluir seguro todo riesgo? ').lower()
                if seguro == 'si':
                    valor_total=chevrolet_aveo+chevrolet_aveo*0.05
                else:
                    valor_total=chevrolet_aveo
            case _:
                break

print(f'Senor {nombre_cliente}\nEl tiempo es: {tiempo}\nEl valor a pagar es: {valor_total}') """


""" descuento=0
valor_unidad = 11000
while True:
    num_computadoras= int(input('Ingrese el numero de computadoras'))
    if  num_computadoras <= 5:
        descuento = 0.1
    elif num_computadoras >= 6 and num_computadoras <= 9:
        descuento = 0.2
    elif num_computadoras >= 10:
        descuento = 0.4
    else:
        break

    precio_final = num_computadoras*valor_unidad-num_computadoras*valor_unidad*descuento
    print(f'El valor total de las computadoras es {precio_final} como haz comprado {num_computadoras} tienes un descuento del {descuento}')
 """


""" precio_unidad = 0
num_llantas = int(input('Ingrese el numero de llantas compradas'))
if num_llantas < 5:
    precio_unidad = 300
elif num_llantas <= 10:
    precio_unidad = 250
elif num_llantas > 10:
    precio_unidad = 200

valor_pagar = precio_unidad*num_llantas
print(f'Usted ha comprado {num_llantas}. Por esta razon, pagara {precio_unidad} por unidad\nEl valor a pagar es de {valor_pagar}')
 """

""" Realice un ejercicio donde al insertar las notas de cuatro materias de un estudiante,
le muestre si según la nota numérica el estudiante tiene excelente sobresaliente
aceptable insuficiente y deficiente. El rango es el siguiente 0 a 1 D, 1,1 a 2,9 I,
3 a 3,8 A, de 3,9 a 4,6 S y de 4,7 a 5 E debe calcularlo para 4 periodos del año
y hacer un promedio de todas las notas si el promedio es igual o mayor a 3,5 debe
salir un mensaje que diga el estudiante es Promovido al siguiente grado debe
aparecer al grado al que es promovido. Si el estudiante está cursando 11 debe
aparecer el estudiante puede graduarse de lo contrario debe aparecer un letrero
que diga el estudiante NO ES PROMOVIDO """

""" estudiante = input('Nombre del estudiante ')
grado = int(input('Digite el grado del estudiante'))

while True: 
    print("1. Mat\n2. Quimica\n3. Fisica\n4. Ingles\n5. Salir" )
    opc = int(input('Ingrese el numero de la materia'))

    match opc:

        case 1:
            nota_mat1=float(input('Ingrese el valor de la nota 1'))
            nota_mat2=float(input('Ingrese el valor de la nota 2'))
            nota_mat3=float(input('Ingrese el valor de la nota 3'))
            nota_mat4=float(input('Ingrese el valor de la nota 4'))
            nota_cortemat = (nota_mat1+nota_mat2+nota_mat3+nota_mat4)/4
            if nota_cortemat >=0 and nota_cortemat <=1:
                print(f'La nota para el period {i} fue D')
            elif nota_cortemat >=1.1 and nota_cortemat <=2.9:
                print(f'La nota para el period {i} fue I')
            elif nota_cortemat >= 3 and nota_cortemat <=3.8:
                print(f'La nota para el period {i} fue A')
            elif nota_cortemat >= 3.9 and nota_cortemat <= 4.6:
                print(f'La nota para el period {i} fue S')
            else:
                print(f'La nota para el period {i} fue E')
            nota_finalmat+=nota_cortemat
        case 2:
            nota_quimica1=float(input('Ingrese el valor de la nota 1'))
            nota_quimica2=float(input('Ingrese el valor de la nota 2'))
            nota_quimica3=float(input('Ingrese el valor de la nota 3'))
            nota_quimica4=float(input('Ingrese el valor de la nota 4'))
            nota_cortequimica=(nota_quimica1+nota_quimica2+nota_quimica3+nota_quimica4)/4
            if nota_cortequimica >=0 and nota_cortequimica <=1:
                print(f'La nota para el period {i} fue D')
            elif nota_cortequimica >=1.1 and nota_cortequimica <=2.9:
                print(f'La nota para el period {i} fue I')
            elif nota_cortequimica >= 3 and nota_cortequimica <=3.8:
                print(f'La nota para el period {i} fue A')
            elif nota_cortequimica >= 3.9 and nota_cortequimica <= 4.6:
                print(f'La nota para el period {i} fue S')
            else:
                print(f'La nota para el period {i} fue E')
            nota_cortequimica+=nota_cortequimica
        case 3:
            nota_fisica1=float(input('Ingrese el valor de la nota 1'))
            nota_fisica2=float(input('Ingrese el valor de la nota 2'))
            nota_fisica3=float(input('Ingrese el valor de la nota 3'))
            nota_fisica4=float(input('Ingrese el valor de la nota 4'))
            nota_cortefisica=(nota_fisica1+nota_fisica2+nota_fisica3+nota_fisica4)/4
            if nota_cortefisica >=0 and nota_cortefisica <=1:
                print(f'La nota para el period {i} fue D')
            elif nota_cortefisica >=1.1 and nota_cortefisica <=2.9:
                print(f'La nota para el period {i} fue I')
            elif nota_cortefisica >= 3 and nota_cortefisica <=3.8:
                print(f'La nota para el period {i} fue A')
            elif nota_cortefisica >= 3.9 and nota_cortefisica <= 4.6:
                print(f'La nota para el period {i} fue S')
            else:
                print(f'La nota para el period {i} fue E')
            nota_final_fisica+=nota_cortefisica
        case 4:
            nota_ingles1=float(input('Ingrese el valor de la nota 1'))
            nota_ingles2=float(input('Ingrese el valor de la nota 2'))
            nota_ingles3=float(input('Ingrese el valor de la nota 3'))
            nota_ingles4=float(input('Ingrese el valor de la nota 4'))
            nota_corteingles=(nota_fisica1+nota_fisica2+nota_fisica3+nota_fisica4)/4
            if nota_corteingles >=0 and nota_corteingles <=1:
                print(f'La nota para el period {i} fue D')
            elif nota_corteingles >=1.1 and nota_corteingles <=2.9:
                print(f'La nota para el period {i} fue I')
            elif nota_corteingles >= 3 and nota_corteingles <=3.8:
                print(f'La nota para el period {i} fue A')
            elif nota_corteingles >= 3.9 and nota_corteingles <= 4.6:
                print(f'La nota para el period {i} fue S')
            else:
                print(f'La nota para el period {i} fue E')
            nota_final_ingles+=nota_corteingles
        case _:
            break


final_mat=nota_finalmat/4
final_quimica = nota_cortequimica/4
final_fisica = nota_final_fisica/4
final_ingles = nota_final_ingles/4

nota_final_ano = (final_mat+final_quimica+final_fisica+final_ingles)/4

if grado == 11 and nota_final_ano >= 3.5:
    print(f'{estudiante} Puedes graduarse')
elif grado != 11 and nota_final_ano >= 3.5:
    print(f'Felicidades {estudiante} has sido promovido')
else:
    print(f'Lo sentimos {estudiante} no seras promovido este ano') 
 """
""" valor=0
puesto = int(input('Ingrese el puesto ocupado'))
print('1. Pitbull\n2. Buly\n3. Rottwhiler\n4. Labrador retriever\n5. Golden retriever\n6.Doberman\n7. Dogo argentino')
raza = int(input('Ingrese la raza del perro'))

if raza == 1:
    valor = 6000000
elif raza == 2:
    valor = 6500000
elif raza == 3:
    valor == 4000000
elif raza == 4:
    valor = 3500000
elif raza == 5:
    valor = 3500000
elif raza == 6:
    valor = 5000000
elif raza == 7:
    valor = 5500000
else:
    print('Digite un valor valido')

if puesto == 1:
    valor = valor*2
elif puesto == 2:
    valor = valor + 800000
elif puesto == 3:
    valor = valor + 200000

print(f'El valor obtenido por {raza} despues que ocupara el puesto {puesto} es de {valor}') """

''' a*b + a*c = a(b+c)

    estudiantes*1 + estudiantes*0.12 = estudiantes*(1+0.12)

    '''

""" victorias_usuario1=0
victorias_usuario2=0
Nombreusuario1 = input('Ingrese el nombre del usuario 1 ')
nombreusuario2 = input('Ingrese el nombre del usuario 2 ')

while True:
    print('Seleccione la opcion en su turno/nPuede escoger: Piedra, Papel o Tijera')

    
    usuario1 = input('Ingrese la opcion su eleccion ').lower()
    usuario2 = input('Ingrese la opcion su eleccion ').lower()

    if usuario1 == 'papel' and usuario2 == 'piedra' or usuario1 == 'tijera' and usuario2 == 'papel' or usuario1 == 'piedra' and usuario2 == 'tijera':
        victorias_usuario1+=1
    elif usuario1 == 'piedra' and usuario2 == 'papel' or usuario1 == 'papel' and usuario2 == 'tijera' or usuario1 == 'tijera' and usuario2 == 'piedra':
        victorias_usuario2+=1
    elif usuario1 == 'piedra' and usuario2 == 'piedra' or usuario1 == 'papel' and usuario2 == 'papel' or usuario1 == 'tijera' and usuario2 == 'tijera':
        print('Es empate')
    else:
        print('Ingrese un valor valido')

    if victorias_usuario1 >= 3 or victorias_usuario2 >= 3:
        break
    else:
        pass

if victorias_usuario1 > victorias_usuario2:
    print(f'Felicidades {Nombreusuario1} eres el ganador')
else:
    print(f'Felicidades {nombreusuario2} eres el ganador')  """

import time
alarmahora = int(input('Ingrese la hora de su alarma'))
alarmaminuto = int(input('Ingrese los minutos de su alarma'))
repita = int(input('Cuantas veces sonara la alarma'))


dias = 0
horas = 0
minutos = 0
segundos = 45

while True:
    time.sleep(1)
    segundos += 1

    if segundos == 60:
        segundos = 0
        minutos += 1

    if minutos == 60:
        minutos = 0
        horas += 1

    if horas == 24:
        horas = 0
        dias += 1

    if horas == alarmahora and minutos == alarmaminuto and segundos % 5 == 0:
        print('alarma')

    print(f"{dias} dias {horas}:{minutos}:{segundos}")
    
