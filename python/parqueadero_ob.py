class Parqueadero:
    def __init__(self, horas, minutos):
        self.__horas = horas
        self.__minutos = minutos

    def pagoParqueadero(self):
        if self.__minutos > 0:
            totalPago = (self.__horas * 1500) + 1500
        else:
            totalPago = (self.__horas * 1500)

        return totalPago