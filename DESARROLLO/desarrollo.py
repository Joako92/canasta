from Auxiliares import *
from INICIO.Repartir import *

"""En este modulo tengo que controlar el flujo del juego
puedo darle opcion al jugador de jugar la mano, acomodar las cartas,
salir, tomar del mazo, levantar el pote"""

MENU_TURNO: str = """1- Agregar carta al juego\n2- Mostrar juegos\n3- Levantar pozo\n4- Bajar juego\n5- Levantar del mazo\n6- Descartar y terminar turno\n7- Abandonar partida"""


def desarrollo(mesa, jugadores: list, primero: int):
    mazo: list = mesa.mazo
    continuar: bool = True
    turno: int = primero

    # Verificar que los jugadores no tengan 3 rojos
    verificar_rojos(jugadores, mazo)

    # Seleccion de turnos
    while continuar:
        if turno == 0:
            continuar: bool = turno_jugador(mesa, jugadores[0])
            turno += 1
        else:
            print("\nTurno del siguiente jugador")
            turno_pc(mesa, jugadores, turno)
            turno += 1
            if len(jugadores) == turno:
                turno = 0

    # Si no se continua se resetea el mazo
    resetear_mazo(jugadores, mesa)
    return


def turno_jugador(mesa, jugador):
    mazo = mesa.mazo
    pote = mesa.pozo
    print(f"\nCarta superior del pozo ({len(pote)}): ", pote[-1])
    continuar: bool = True
    levanto = False
    while continuar:
        ordenar_cartas(jugador)
        # mostrar un menu segun las opciones que tenga
        print("{:^50}".format('MENU DE TURNO'))
        print(f"Tu mano:\n{jugador.mano}")
        print(MENU_TURNO)
        opc: str = seleccionar_opcion("Elegí tu jugada:_", 1, 7)
        if opc == "1":  # Agregar carta al juego
            if not jugador.mesa:
                print("Todavia no bajaste ningun juego!")
                time.sleep(2)
            else:
                carta_para_agregar = input("Ingresá el numero o la letra de la carta que queres bajar:_")
                while not verificar_carta(carta_para_agregar, jugador.mano):
                    print("No tenes esa carta!")
                    carta_para_agregar = input("Ingresá el numero o la letra de la carta que queres bajar:_")

                # Crea una lista con todas las que coincidan
                cartas_para_agregar = [carta for carta in jugador.mano if carta[0:-1] == carta_para_agregar]
                for carta in cartas_para_agregar:
                    agregar_al_juego(carta, jugador)

        elif opc == "2":  # mostrar jugador
            mostrar_mesa(jugador)
            time.sleep(2)

        elif opc == "3":  # Levantar pozo TODO verificar que no tenga un 3 negro
            if not jugador.mesa:
                # En realidad aca iria una funcion para comparar el puntaje
                print("Primero debes abrirte!")
                time.sleep(2)
            else:
                if levanto:
                    print("Ya levantaste en este turno!")
                    time.sleep(2)
                else:
                    levantar_pozo(jugador, pote)
                    print(mostrar_mano(jugador))
                    print(mostrar_mesa(jugador))
                    levanto = True
                    time.sleep(2)

        elif opc == "4":  # Abrirse
            abrirse(jugador)

        elif opc == "5":  # Levantar del mazo
            if levanto:
                print("Ya levantaste en este turno!")
                time.sleep(2)
            else:
                levantar_mazo(jugador, mazo)
                print(f"Levantaste: {jugador.mano[-2:]}")
                levanto = True
                time.sleep(2)

        elif opc == "6":  # Descartar y terminar turno
            if not levanto:
                print("Primero debes levantar del mazo o del pozo!")
                time.sleep(2)
            else:
                descartarse(jugador, pote)
                return continuar

        elif opc == "7":  # Salir
            print("Volviendo al menu principal...")
            time.sleep(2)
            continuar = False
    return continuar


def verificar_carta(valor: str, lista_cartas: list):
    """
    toma un numero o letra y verifica si esta en la lista
    :param valor: un numero o letra del tipo str
    :param lista_cartas: puede ser la mano del jugador o un juego en mesa
    :return: True si pertenece a la lista
    """
    for carta in lista_cartas:
        if carta[:-1] == valor:
            return True
    return False


def turno_pc(mesa, jugadores: list, turno: int):
    mazo = mesa.mazo
    pote = mesa.pozo
    jugador = jugadores[turno]
    ya_levanto = False
    top = pote[-1]
    puntaje_minimo = 50  # TODO determinar segun el puntaje
    print(f"\nJuega {jugador.nombre}\n")
    time.sleep(2)

    # Determinar si tiene algun juego para bajar, y para levantar el pozo TODO verificar que no tenga un 3 negro
    cuenta = sum(1 for carta in jugador.mano if top[:-1] == carta[:-1])
    if cuenta >= 2 and valor_mesa(jugador) >= puntaje_minimo and not ya_levanto:
        # Levantar pozo
        levantar_pozo(jugador, pote)
        print(f"{jugador.nombre} levanta el pozo.")
        ya_levanto = True

    # Si no, alzar 2 cartas del mazo.
    if not ya_levanto:
        levantar_mazo(jugador, mazo)

    # Determinar si puede bajar algun juego
    if jugador.mesa:
        for carta in jugador.mano:
            agregar_al_juego(carta, jugador)
    abrirse_pc(jugador)
    print(mostrar_mesa(jugador))

    # Si no, descartar y terminar turno
    descartarse_pc(jugador, mesa)


def mostrar_mano(jugador):
    """
    Devuelve una cadena mostrando las cartas de la mano del jugador
    :param jugador: objeto clase JUGADOR
    :return: cadena
    """
    cadena = f"Mano {jugador.nombre}:\n{jugador.mano}"
    return cadena


def mostrar_mesa(jugador):
    """
    Devuelve una cadena mostrando las cartas de la mesa del jugador
    :param jugador: objeto clase JUGADOR
    :return: cadena
    """
    print(f"Juegos bajados {jugador.nombre}:\n")
    for juego in jugador.mesa:
        print(juego)
    return


def verificar_rojos(jugadores: list, mazo: list):
    """
    Funcion para verificar la mano de cada jugador, controlando que no sea un 3 rojo
    :param jugadores: Lista de objetos tipo jugador
    :param mazo: Lista de str que representan cartas
    :return:
    """
    for jugador in jugadores:
        jugador.mano = [carta for carta in jugador.mano if not is_rojo(carta, jugador, mazo)]
        time.sleep(2)


def is_rojo(carta: str, jugador, mazo):
    if carta in ["3♥", "3♦"]:
        print(f"{jugador.nombre} tiene un 3 rojo, se descarta.")
        rojo = carta
        jugador.rojos.append(rojo)
        nueva_carta = mazo.pop()
        while is_rojo(nueva_carta, jugador, mazo):
            print(f"{jugador.nombre} toma otra carta: {nueva_carta}")
            nueva_carta = mazo.pop()
        jugador.mano.append(nueva_carta)
        return True
    return False


def valor_mesa_1(jugador):
    valor = sum(VALORES[carta[0:-1]] for carta in jugador.mesa if carta[0:-1] in VALORES)
    return valor


def valor_mesa(jugador):
    valor = 0
    for juego in jugador.mesa:
        for carta in juego:
            if carta[0:-1] in VALORES:
                valor += VALORES[carta[0:-1]]
    return valor


def ordenar_cartas(jugador):
    """
    funcion que ordena la mano de un jugador
    :param jugador: objeto tipo JUGADOR
    :return: el vector mano ordenado
    """
    jugador.mano = sorted(jugador.mano, key=sorter)


def sorter(elem: str):
    """
    devuelve el criterio de orden de las cartas
    :param elem: cadena o iterable
    :return: el primer elemento de la cadena
    """
    return elem[0]


def abrirse(jugador):  # TODO determinar si se formo alguna canasta
    # Se le muestra la mano al jugador
    mostrar_mano(jugador)

    # Seleccionar el numero de la carta del juego que quiere bajar
    valor = (input("Seleccioná el número o letra del juego que querés bajar: ")).upper()

    # Verificar que existan al menos 3 cartas iguales en la mano del jugador
    cuenta = sum(1 for carta in jugador.mano if carta[0:-1] == valor)
    if cuenta < 3:
        print("No tenés suficientes cartas para abrir ese juego.")
        return

    # Validar que el valor ingresado esté en la mano del jugador
    if valor not in [carta[0:-1] for carta in jugador.mano]:
        print("No tenés esa carta en tu mano.")
        return

    # Sacar de la lista todas las cartas que coincidan con el valor indicado
    print(f"Se baja el juego de las cartas {valor}")
    jugador.mesa.append([carta for carta in jugador.mano if carta[0:-1] == valor])
    jugador.mano = [carta for carta in jugador.mano if carta[0:-1] != valor]

    # Calcular el puntaje del juego bajado a la mesa
    print("El valor de los juegos en la mesa es:", valor_mesa(jugador))


def contar_cartas(mano: list):
    """
    La funcion debe devolver la cantidad de cada carta segun su valor,
    que se encuentra en cada carta [0:-1]
    :param mano: lista de cartas tipo str, por ejemplo '10♥'
    :return: un dict con el valor de la carta y su cantidad
    """
    cartas: dict = {}  # {valor: cantidad}
    for carta in mano:
        if carta[:-1] not in cartas:
            cartas[carta[:-1]] = 1
        else:
            cartas[carta[:-1]] += 1
    return cartas


def abrirse_pc(jugador):  # TODO determinar si se formo alguna canasta
    # Determinar si hay algun juego de 3 o mas cartas iguales
    cuenta = contar_cartas(jugador.mano)  # Un dict con la cantidad de cada carta
    for valor in cuenta:
        if cuenta[valor] > 2:  # Como minimo deben ser 3 cartas
            juego = [carta for carta in jugador.mano if carta[:-1] == valor]
            jugador.mesa.append(juego)  # Agregar el juego de cartas a la mesa como una lista
            jugador.mano = [carta for carta in jugador.mano if carta[:-1] != valor]  # Eliminar las cartas del juego de la mano
    return


def levantar_pozo(jugador, pozo: list):
    # Comparar la carta de arriba del pozo, debe ser igual a 2 cartas en la mano
    top = pozo[-1]
    cuenta = sum(1 for carta in jugador.mano if carta[0:-1] == top[0:-1])

    # Verificar el puntaje actual, compararlo con el puntaje minimo
    puntaje_minimo = 50
    if cuenta >= 2 and valor_mesa(jugador) >= puntaje_minimo:
        jugador.mano.extend(pozo)
        jugador.mesa.extend(carta for carta in jugador.mano if carta[0:-1] == top[0:-1])
        pozo.clear()
        return
    print("No cumplís las condiciones para levatar el pozo aún.")
    return


def levantar_mazo(jugador, mazo: list):
    for vez in range(2):
        carta = mazo.pop()
        while is_rojo(carta, jugador, mazo):
            carta = mazo.pop()
        jugador.mano.append(carta)


def descartarse(jugador, pozo):
    mostrar_mano(jugador)
    valor_carta = input("Elegi el numero o letra que queres bajar:_")
    while valor_carta not in [carta[0:-1] for carta in jugador.mano]:
        print("No tenés esa carta en tu mano.")
        valor_carta = input("Elegi el numero o letra que queres bajar:_")
    descartada = [carta for carta in jugador.mano if carta[0:-1] == valor_carta]
    descartada = descartada[0]
    print(f"Descartando {descartada}")
    jugador.mano.remove(descartada)  # Usamos remove() para eliminar la carta directamente
    pozo.append(descartada)
    time.sleep(2)


def descartarse_pc(jugador, mesa):
    pozo = mesa.pozo
    # Encontrar la carta que se repite menos veces
    carta_menor_cantidad = None
    for carta in jugador.mano:
        contar = jugador.mano.count(carta[:-1])
        if not carta_menor_cantidad or contar < jugador.mano.count(carta_menor_cantidad[:-1]):
            carta_menor_cantidad = carta

    descartada = jugador.mano.pop(jugador.mano.index(carta_menor_cantidad))
    print(f"Descartando {descartada}")
    pozo.append(descartada)
    time.sleep(2)


def agregar_al_juego(carta: str, jugador):
    """
    Si encuentra la carta en algun juego de la mesa la agrega
    :param carta: str de la forma '10♥'
    :param jugador: objeto del tipo JUGADOR
    :return:
    """
    if jugador.mesa:
        for juego in jugador.mesa:
            if carta in juego:
                juego.append(carta)
                jugador.mano.remove(carta)
    return


def verificar_canasta(juego: list):
    """
    toma un juego y determina si es canasta o no
    :param juego:
    :return:
    """
    pass


if __name__ == "__main__":
    pass
