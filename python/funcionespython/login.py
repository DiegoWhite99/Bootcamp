
def login():
    usuario_correcto = "admin-root"
    contraseña_correcta = "python123"
    intentos = 0
    max_intentos = 3

    while intentos < max_intentos:
        user = input('Ingrese su usuario: ')
        password = getpass.getpass('Ingrese su contraseña: ')

        if user == usuario_correcto and password == contraseña_correcta:
            print('''¡Acceso concedido! 
                Bienvenido señor stark''')
            return  
        else:
            intentos += 1
            print(f'Usuario o contraseña incorrectos. Intento {intentos}/{max_intentos}')

    print("Acceso bloqueado. Demasiados intentos fallidos.contactese con soporte")

login()
 