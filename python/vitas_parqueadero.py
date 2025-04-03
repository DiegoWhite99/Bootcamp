from parqueadero_ob import Parqueadero

horas = int(input('Ingrese las horas: '))
minutos = int(input('Ingrese los minutos: '))
parqueaderoUno = Parqueadero(horas, minutos)
resultado = parqueaderoUno.pagoParqueadero()
print("El pago del parqueadero es: " + str(resultado))