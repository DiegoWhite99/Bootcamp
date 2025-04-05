class Nomina:
    def __init__(self, empleado, horas):
        self.__empleado = empleado
        self.__horas = horas

    def pago_nomina(self):
        sueldo = self.__horas * 8000
        if sueldo > 700000:
            seguro = sueldo * 0.085
        else:
            seguro = sueldo * 0.035
        total_pagar = sueldo - seguro
        return total_pagar
        