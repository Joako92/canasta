# from MENU.Menu import *
import INICIO.Dealer
from Principal import *
import time
import random as r
r.seed(r.randint(1, 1000))


"""En este modulo tengo que desarrollar las funciones para mezclar, cortar y repartir el mazo"""


def comenzar_juego(jugadores: list):
    """
    Esta funcion controla el inicio del juego,
    desde la cantidad de cartas hasta que se reparte cada mano
    :param jugadores: lista de objetos tipo jugador
    :return: devuelve el mazo y el pozo
    """
    primero = INICIO.Dealer.elegir_primero(jugadores)  # Esto determina a quien se reparte primero
    mesa = MESA()
    mesa.mazo = cantidad_mazos(len(jugadores)//2)  # Llena el mazo dependiendo la cantidad de jugadores
    cartas = mesa.mazo

    print("mezclando mazos...")
    cartas = r.sample(cartas, len(cartas))  # Mezcla el mazo
    time.sleep(2)

    print("Cortando mazo...")
    cartas_arriba, cartas_abajo, extras = cortar(cartas, jugadores)
    while len(cartas_abajo) == 0 and len(cartas_arriba) == 0:
        cartas_arriba, cartas_abajo, extras = cortar(cartas, jugadores)
    time.sleep(2)

    print("Repartiendo cartas..." + "\n"*15)
    cartas = repartir(cartas_arriba, cartas_abajo, jugadores, extras, primero)
    cartas, mesa.pozo = formar_pozo(cartas)
    pote = mesa.pozo
    time.sleep(2)

    # Si la carta es un 3 rojo se vuelve a repartir
    if pote[-1] == "3♥" or pote[-1] == "3♦":
        print("Se vuelve a repartir!")
        time.sleep(2)
        resetear_mazo(jugadores, mesa)
        comenzar_juego(jugadores)

    return mesa, primero


def cantidad_mazos(jugadores: int):
    # Jugadores puede ser 1, 2 o 3
    mazo = completar_mazo()*(2**jugadores)  # Devuelve 2, 4 u 8 mazos
    return mazo


def cortar(mazo: list, jugadores: list):
    """
    :param mazo: lista con todas las cartas en juego
    :param jugadores: lista de objetos jugador
    :return: el mazo dividido en 2, mas una lista de comodines que hayan sido encontrados abajo
    """
    extras: list = []
    # corte_perf = False  # Esto se va a usar en el puntaje
    repartidas: int = (15 * len(jugadores)) + 7  # cantidad total de cartas repartidas
    # Cortar el mazo en un punto por debajo de la mitad
    corte = r.randint((len(mazo)//2), len(mazo)-1)
    if corte == repartidas:
        print("Corte perfecto!")
        # corte_perf = True
    # Determinar la carta que quedo arriba si es un comodin, un 2, o un 3 de corazones
    carta_arriba: str = mazo[corte]
    print("Carta que quedo abajo: ", carta_arriba)
    # Si es un comodin o 3 rojo se lo queda el jugador
    while carta_arriba == "C?" or carta_arriba[0] == "2" or carta_arriba == "3♥" or carta_arriba == "3♦":
        print("Esta te la quedas: ", carta_arriba)
        extras.append(mazo.pop(corte))
        carta_arriba = mazo[corte-1]
        corte -= 1

    # Devolver la parte de abajo del mazo separada de la de arriba
    mazo_arriba: list = mazo[0: corte+1]
    mazo_abajo: list = mazo[corte+1:]
    return mazo_arriba, mazo_abajo, extras


def repartir(mazo_sup: list, mazo_inf: list, jugadores: list, extras: list, primero: int):
    """
    :param mazo_sup: Parte que quedo arriba en el mazo, siempre mayor
    :param mazo_inf: Parte con la que se reparte primero
    :param jugadores: lista de objetos tipo jugador
    :param extras: lista de comodines para el jugador que hizo el corte
    :param primero: Int que representa el jugador que reparte
    :return: nuevo mazo con las cartas que no se repartieron
    """
    num_cartas_por_jugador: int = 15

    # Asignar cartas extras al primer jugador
    if jugadores:
        jugadores[primero].mano.extend(extras)

    for jugador in jugadores:
        # Verificar si hay suficientes cartas en el mazo inferior antes de repartir
        while len(jugador.mano) < num_cartas_por_jugador and mazo_inf:
            jugador.mano.append(mazo_inf.pop())

        # Repartir cartas del mazo superior si aún faltan cartas en la mano del jugador
        while len(jugador.mano) < num_cartas_por_jugador and mazo_sup:
            jugador.mano.append(mazo_sup.pop())

    # Combinar los mazos restantes y devolverlos como el nuevo mazo completo
    nuevo_mazo: list = mazo_inf + mazo_sup
    return nuevo_mazo


def formar_pozo(mazo: list):
    pote: list = []
    for v in range(7):
        pote.append(mazo.pop())
    return mazo, pote


def resetear_mazo(jugadores: list, mesa):
    # resetear cada jugador
    jugadores.clear()
    # resetear la mesa
    mesa.pozo.clear()
    mesa.mazo.clear()
    return


if __name__ == "__main__":
    print(cantidad_mazos(2))
