"""Determinar quien empieza jugando"""
import Principal
import random


def elegir_primero(jugadores):
    """
    Para inciar el juego se barajan las cartas
    y se decide quién empieza mediante “la carta más alta”.
    Es decir, cada jugador levanta una carta del mazo (las 216 iniciales)
    y el que saque la carta más alta será el primero en empezar.
    Si se saca un joker, se tomará la carta inmediatamente inferior.
    Hay que resaltar que la carta más baja sería el As y la más alta la (o rey).
    :param jugadores:
    :return:
    """
    mazo = un_mazo()
    cartas = []
    for jugador in jugadores:
        carta = random.choice(mazo)
        cartas.append(carta)
        print(f"Carta {jugador.nombre}:{carta}")
    primero = cartas.index(carta_mayor(cartas))
    print(f"Comienza jugando {jugadores[primero].nombre}")
    return primero


def un_mazo():
    mazo = []
    for valor in Principal.CARTAS:
        for palo in Principal.PALOS:
            mazo.append(valor + palo)
    return mazo


def carta_mayor(cartas: list):
    """
    Encontrar la carta mas alta segun su orden
    :param cartas:
    :return:
    """
    orden = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    mayor = None
    for carta in cartas:
        if mayor is None:
            mayor = carta
        elif orden.index(carta[:-1]) > orden.index(mayor[:-1]):
            mayor = carta
    return mayor
