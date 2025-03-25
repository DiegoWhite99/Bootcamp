'''
texto = "aaaaaaaaaa"
for i in texto:
    print("Programadores")



suma=0
for i in range(0,10,1):
    numero=int(input('Digite un numero'))


inicio = int(input('Ingrese el numero de inico de la tabla '))
fin = int(input('Ingrese el ultimo numero de la tabla '))
tabla = int(input('Ingrese el numero de la tabla '))

for i in range(inicio, fin+1):
    print(f'{i} * {tabla} = {tabla*i}')


t=1
while t <= 10:
    m = 1
    while m <= 10:
        resultado = t * m 
        print(f'{m} * {t} = {resultado}')
        m+=1
    t+=1
    print()

iniciot = int(input('Ingrese el numero de inico de la tabla '))
fint = int(input('Ingrese el ultimo numero de la tabla '))
inicion = int(input('Ingrese el numero de inico de la tabla '))
finn = int(input('Ingrese el ultimo numero de la tabla '))
for p in range(iniciot, fint+1):
    for i in range(inicion,finn+1):
        print(f'{i} * {p} = {i*p}')
    print()
'''
num_estudiantes = 750
num_new = 0
for i in range(2025,2036):
    num_new = num_estudiantes+num_new*0.12
    num_estudiantes = num_new
    print(f'La cantidad de estudiantes esperada para el {i} sera: {num_estudiantes:.0f}')