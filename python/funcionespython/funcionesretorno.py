def parqueadero(horas, minutos):
    if minutos > 0:
        total_pagar = (horas + 1) * 1500
    else:
        total_pagar = horas * 1500

    return total_pagar