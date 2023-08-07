def validar_vacio(num):
    if num.strip() == "":
        return False
    return True


def validar_numero(num):
    if num.isdigit():
        return True
    return False


def validar_positivo(num):
    return int(num) > 0


def validar_conjunto(inf, sup, num):
    return inf <= int(num) <= sup


def validar():
    num = input("Ingrese un numero mayor a 0: ")
    while not validar_vacio(num) or not validar_numero(num) or not validar_positivo(num):
        print("Error...")
        num = input("Ingrese un numero mayor a 0: ")

    return int(num)


def validar_entre(inf, sup):
    num = input(f"Ingrese un numero entre {inf} y {sup}: ")
    while not validar_vacio(num) or not validar_numero(num) or not validar_conjunto(inf, sup, num):
        print("Error...")
        num = input(f"Ingrese un numero entre {inf} y {sup}: ")

    return int(num)


def seleccionar_opcion(msj, primera, ultima):
    opc = input(msj)
    while not validar_vacio(opc) or not validar_numero(opc) or not validar_conjunto(primera, ultima, opc):
        print("La opcion ingresada es incorrecta")
        opc = input(msj)
    return opc
