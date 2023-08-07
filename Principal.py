"""Aca comienza el proyecto para crear un juego de canasta en python desde cero"""

"""Variables basicas:"""
CARTAS = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
COMODINES = ("C?", "C?")
VALORES = {"A": 20,
           "2": 20,
           "3": 100,
           "4": 5,
           "5": 5,
           "6": 5,
           "7": 5,
           "8": 10,
           "9": 10,
           "10": 10,
           "J": 10,
           "Q": 10,
           "K": 10,
           "C": 50}
PALOS = ("♥", "♦", "♣", "♠")
MONOS = ("2♥", "2♦", "2♣", "2♠", "C?")


class MESA:
    def __init__(self, mazo=None, pozo=None):
        self.mazo = mazo if mazo is not None else []
        self.pozo = pozo if pozo is not None else []

    def __str__(self):
        return f"Cartas en el mazo: {len(self.mazo)}\n" \
               f"Pozo ({len(self.pozo)}: {self.pozo[-1]})"


class JUGADOR:
    def __init__(self, mano=None, canastas=None, rojos=None, nombre="CPU", mesa=None, puntaje=0):
        self.nombre = nombre
        self.mano = mano if mano is not None else []
        self.canastas = canastas if canastas is not None else []
        self.rojos = rojos if rojos is not None else []
        self.mesa = mesa if mesa is not None else []
        self.puntaje = puntaje

    def __str__(self):
        return f"{self.nombre}\n" \
               f"Tu mano: {self.mano}\n" \
               f"Juegos en mesa: {self.mesa}\n" \
               f"Tenés {len(self.canastas)} canastas\n" \
               f"Tenés {len(self.rojos)} tres rojos\n" \
               f"Tu puntaje actual es: {self.puntaje}\n"


def completar_mazo():
    mazo_completo = []
    for palo in PALOS:
        for car in CARTAS:
            mazo_completo.append(str(car)+str(palo))
    mazo_completo.extend(COMODINES)
    return mazo_completo


def crear_jugadores(cant: int):
    jugadores = []
    for i in range(cant):
        jugador = JUGADOR()
        jugador.nombre = ("CPU" + str(i+1))
        jugadores.append(jugador)
    return jugadores


if __name__ == "__main__":
    jugs = crear_jugadores(4)
    jugs[2].mano = [1]
    for jg in jugs:
        print(jg)
