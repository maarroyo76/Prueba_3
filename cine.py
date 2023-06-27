peliculas = ['El Rey Leon']
asientos = {}
numero_boleta = 1
alumnos = []
def mostrar_menu():
    print("----- Menú -----")
    print("1) Comprar entrada")
    print("2) Listar todas las compras")
    print("3) Salir")
def mostrar_asientos(asientos_pelicula):
    print("----- Asientos -----")
    for fila in range(10):
        for columna in range(15):
            if asientos_pelicula[fila][columna]:
                print("X", end=" ")
            else:
                print("O", end=" ")
        print()
    print("-------------------")
def comprar_entrada():
    valor_entrada = 2500
    
    numero_entrada= 0
    print("----- Películas Disponibles -----")
    print(f"1){peliculas}")

    pelicula_index = 0
    while True:
        try:
            pelicula_index = int(input("Seleccione una película: ")) - 1
            if pelicula_index < 0 or pelicula_index >= len(peliculas):
                raise ValueError()
            break
        except ValueError:
            print("Opción inválida. Ingrese un número válido.")

    pelicula = peliculas[pelicula_index]
    if pelicula_index not in asientos:
        asientos[pelicula_index] = [[False for _ in range(15)] for _ in range(10)]

    asientos_pelicula = asientos[pelicula_index]
    mostrar_asientos(asientos_pelicula)

    while True:
        try:
            fila = int(input("Ingrese el número de fila (1-15): ")) - 1
            columna = int(input("Ingrese el número de columna (1-10): ")) - 1
            if fila < 0 or fila >= 10 or columna < 0 or columna >= 15:
                raise ValueError()
            if asientos_pelicula[fila][columna]:
                print("El asiento seleccionado ya está ocupado.")
            else:
                break
        except ValueError:
                print("Asiento inválido. Ingrese un número válido.")
    asientos_pelicula[fila][columna] = True
    print('Eres Alumno de DuocUC?')
    print('[1] Si')
    print('[2]No')
    while True:
        try:
            alumno = int(input('>>'))
            if alumno == 1:
                nombre_alumno= input('Ingrese su nombre: ')
                alumnos.append(nombre_alumno)
                print(f'Felicidades tienes un 20% de descuento!')
                valor_descuento = valor_entrada-500
                break
            else:
                print(f'No tienes descuento :(')
                break
        except ValueError:
            print('opcion invalida')
    numero_entrada+=1
    print(f'------- Boleta #{numero_entrada}------')
    print(f"{pelicula}")
    print(f"Valor de entrada: {valor_entrada}")
    if alumno == 1:
        ultimo_alumno = alumnos[-1]
        print(f"{ultimo_alumno}")
        print(f"Descuento: 20%")
        print(f"Monto de decuento : 500")
        print(f"Valor final ${valor_descuento}")
    print(f"---------------------------------------")
def lista_usuarios():
    print(f"{alumnos}")
    print
    
def ejecutar_programa():
    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            comprar_entrada()
        elif opcion == "2":
            lista_usuarios()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Ingrese un número válido.")

ejecutar_programa()