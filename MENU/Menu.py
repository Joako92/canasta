import INICIO.Reglas
from DESARROLLO.desarrollo import *
import time

"""Menu de opciones:"""

MENU: str = """1- Seleccionar modo de juego
2- Comenzar partida
3- Reglas
4- Salir"""


def inicio():
    motd = 'BIENVENIDO AL JUEGO DE CANASTA'
    plantilla = f"{'#'*50}\n#{' '*48}#\n#{' '*48}#\n#{motd.center(48)}#\n#{' '*48}#\n#{' '*48}#\n{'#'*50}"
    print(plantilla)
    time.sleep(4)


def ejecutar_menu():
    modo: int = 1
    op: str = "0"
    usuario: JUGADOR = setear_jugador()
    jugadores: list = [usuario, JUGADOR()]  # Por defecto el juego es individual
    while op != "4":
        print("Modo de juego seleccionado: ", modo_juego(modo-1))
        print("{:^50}".format('MENU PRINCIPAL'))
        print(MENU)
        op: str = seleccionar_opcion("Seleccione una opcion del menú: ", 1, 4)
        print()

        if op == "1":  # Modo de juego
            jugadores: list = [usuario]  # vacía la lista, excepto el usuario
            print("""1- Juego individual\n2- Juego en pareja\n3- Juego en trío""")
            modo = int(seleccionar_opcion("Seleccione modo de juego: ", 1, 3))
            bots = (1, 3, 5)
            jugadores.extend(crear_jugadores(bots[modo-1]))

        elif op == "2":  # Comenzar partida
            mesa, primero = comenzar_juego(jugadores)
            desarrollo(mesa, jugadores, primero)

        elif op == "3":  # Reglas
            INICIO.Reglas.ver_reglas()

    print(f"{'-'*50}\nGracias por jugar!")


def setear_jugador():
    usuario = JUGADOR()
    nombre = input("Ingresa tu nombre:_")
    if nombre.strip() == "":
        print("Perfecto! te mantendremos ANONIMO")
        usuario.nombre = "ANONIMO"
    else:
        usuario.nombre = nombre
    return usuario


def modo_juego(jugadores):
    modo: tuple = ("Individual", "Parejas", "Tríos")
    return modo[jugadores]


if __name__ == "__main__":
    inicio()
    ejecutar_menu()
