"""En este modulo voy a poner los textos que sirven para mostrar las reglas al jugador"""


def ver_reglas():
    """
    Al llamar esta funcion muestra las instrucciones para jugar paso a paso
    :return:
    """
    num_hoja = 1
    for hoja in LIBRO:
        print(f"Hoja numero {num_hoja}")
        print(hoja)
        input("Pulse ENTER para pasar a la siguiente hoja" + "\n"*20 + "Click acá")
        num_hoja += 1


ENCUADRE = f"{'#'*100}\n" \
           + "#" + "{:^98}".format("") + "#\n" \
           + "#" + "{:^98}".format("") + "#\n" \
           + "#" + "{:^98}".format("") + "#\n" \
           + "#" + "{:^98}".format("") + "#\n" \
           + "#" + "{:^98}".format("") + "#\n" \
           + f"{'#'*100}\n"

HOJA_1 = f"{'#'*100}\n" \
           + "#" + "{:^98}".format("") + "#\n" \
           + "#" + "{:^98}".format("") + "#\n" \
           + "#" + "{:^98}".format("LAS REGLAS DE LA CANASTA") + "#\n" \
           + "#" + "{:^98}".format("") + "#\n" \
           + "#" + "{:^98}".format("") + "#\n" \
           + f"{'#'*100}\n"

HOJA_2 = f"{'#'*100}\n" \
           + "#" + "{:^98}".format("La canasta es un juego de naipes cuyo objetivo") + "#\n" \
           + "#" + "{:^98}".format("es crear grupos de cartas del mismo valor,") + "#\n" \
           + "#" + "{:^98}".format("para luego finalizar jugando o descartando") + "#\n" \
           + "#" + "{:^98}".format("todas las cartas de la mano.") + "#\n" \
           + "#" + "{:^98}".format("") + "#\n" \
           + f"{'#'*100}\n"

HOJA_3 = f"{'#'*100}\n" \
           + "#" + "{:^98}".format("El valor de cada carta es el siguiente:") + "#\n" \
           + "#" + "{:^98}".format("") + "#\n" \
           + "#" + "{:^98}".format("• As (20 puntos)") + "#\n" \
           + "#" + "{:^98}".format("• 8, 9, 10, J, Q y K (10 puntos)") + "#\n" \
           + "#" + "{:^98}".format("• 4, 5, 6 y 7 (5 puntos)") + "#\n" \
           + f"{'#'*100}\n"

HOJA_4 = f"{'#'*100}\n" \
           + "#" + "{:^98}".format("• el 3 rojo (corazones o diamantes)") + "#\n" \
           + "#" + "{:^98}".format("Es una carta honorífica, nunca se juega.") + "#\n" \
           + "#" + "{:^98}".format("En cuanto se consigue, se muestra sobre la mesa y se reemplaza por otra carta del mazo.") + "#\n" \
           + "#" + "{:^98}".format("Vale 100 puntos en el caso de haber conseguido por lo menos una canasta") + "#\n" \
           + "#" + "{:^98}".format("en caso contrario, valdrá 100 puntos en contra. 4 Tres rojos valen 800 puntos.") + "#\n" \
           + f"{'#'*100}\n"

HOJA_5 = f"{'#'*100}\n" \
           + "#" + "{:^98}".format("• el 3 negro (picas y tréboles) se considera tapón,") + "#\n" \
           + "#" + "{:^98}".format("es decir, cuando un jugador coloca un 3 negro en la pila de descarte,") + "#\n" \
           + "#" + "{:^98}".format("el siguiente no puede llevársela.") + "#\n" \
           + "#" + "{:^98}".format("Cada 3 negro que quede en la mano de un jugador vale 100 puntos en contra (negativos).") + "#\n" \
           + "#" + "{:^98}".format("") + "#\n" \
           + f"{'#'*100}\n"

HOJA_6 = f"{'#'*100}\n" \
           + "#" + "{:^98}".format("") + "#\n" \
           + "#" + "{:^98}".format("• el 2 vale 20 puntos (comodines)") + "#\n" \
           + "#" + "{:^98}".format("") + "#\n" \
           + "#" + "{:^98}".format("• los jokers valen 50 puntos (comodines)") + "#\n" \
           + "#" + "{:^98}".format("") + "#\n" \
           + f"{'#'*100}\n"

HOJA_7 = f"{'#'*100}\n" \
           + "#" + "{:^98}".format("El Objetivo") + "#\n" \
           + "#" + "{:^98}".format("consiste en llegar a los 5.000 puntos (partida rápida)") + "#\n" \
           + "#" + "{:^98}".format("o a los 7.000 (partida normal o standard).") + "#\n" \
           + "#" + "{:^98}".format("Para conseguir estos puntos se deben hacer “canastas”.") + "#\n" \
           + "#" + "{:^98}".format("Las canastas son grupos de siete cartas del mismo número.") + "#\n" \
           + f"{'#'*100}\n"

HOJA_8 = f"{'#'*100}\n" \
           + "#" + "{:^98}".format("Para inciar el juego se decide quién empieza mediante “la carta más alta”.") + "#\n" \
           + "#" + "{:^98}".format("el que saque la carta más alta será el primero en empezar.") + "#\n" \
           + "#" + "{:^98}".format("la carta más baja sería el As y la más alta la (o rey).") + "#\n" \
           + "#" + "{:^98}".format("Si saca un joker, un 2(comodín) o un 3 rojo podrá quedárselo,") + "#\n" \
           + "#" + "{:^98}".format("Si el jugador que corta, corta exacto, se le bonificará con 100 puntos") + "#\n" \
           + f"{'#'*100}\n"

HOJA_9 = f"{'#'*100}\n" \
           + "#" + "{:^98}".format("Después de repartir las 15 cartas a cada jugador,") + "#\n" \
           + "#" + "{:^98}".format("el que reparte colocará 6 cartas apiladas sobre la mesa boca abajo") + "#\n" \
           + "#" + "{:^98}".format("y encima de estas colocará una boca arriba.") + "#\n" \
           + "#" + "{:^98}".format("") + "#\n" \
           + "#" + "{:^98}".format("Estas 7 cartas configuran el “pote” inicial.") + "#\n" \
           + f"{'#'*100}\n"

HOJA_10 = f"{'#'*100}\n" \
           + "#" + "{:^98}".format("El jugador que empieza decide si llevarse el pote le interesa.") + "#\n" \
           + "#" + "{:^98}".format("Debe tener dos cartas del mismo número que la carta que está boca arriba en el pote,") + "#\n" \
           + "#" + "{:^98}".format("más los puntos necesarios para llevarse el pote.") + "#\n" \
           + "#" + "{:^98}".format("Si tiene las cartas y los puntos puede llevarse el pote,") + "#\n" \
           + "#" + "{:^98}".format("es decir, llevarse la pila de cartas.") + "#\n" \
           + f"{'#'*100}\n"

HOJA_11 = f"{'#'*100}\n" \
           + "#" + "{:^98}".format("El 3 negro se usa como tapón.") + "#\n" \
           + "#" + "{:^98}".format("Cuando un jugador lo tira al pote,") + "#\n" \
           + "#" + "{:^98}".format("el siguiente no puede llevarse el pote,") + "#\n" \
           + "#" + "{:^98}".format("tiene que llevarse dos cartas del mazo y jugar habitualmente.") + "#\n" \
           + "#" + "{:^98}".format("") + "#\n" \
           + f"{'#'*100}\n"

HOJA_12 = f"{'#'*100}\n" \
           + "#" + "{:^98}".format("Para abrirse se requiere un número de puntos que se deben poner sobre la mesa,") + "#\n" \
           + "#" + "{:^98}".format("que dependerá del puntaje que tenga el jugador o la pareja de jugadores") + "#\n" \
           + "#" + "{:^98}".format("al inicio de la partida,") + "#\n" \
           + "#" + "{:^98}".format("") + "#\n" \
           + "#" + "{:^98}".format("según el siguiente cuadro:") + "#\n" \
           + f"{'#'*100}\n"

HOJA_13 = f"{'#'*100}\n" \
           + "#" + "{:^98}".format("• En negativo: 15 puntos") + "#\n" \
           + "#" + "{:^98}".format("• De 0 a 1495: 50 puntos") + "#\n" \
           + "#" + "{:^98}".format("• De 1500 a 2995: 90 puntos") + "#\n" \
           + "#" + "{:^98}".format("• De 3000 a 4995: 120 puntos") + "#\n" \
           + "#" + "{:^98}".format("• De 5000 a 7495: 150 puntos") + "#\n" \
           + f"{'#'*100}\n"

HOJA_14 = f"{'#'*100}\n" \
           + "#" + "{:^98}".format("Al abrirse, el jugador tiene que poner las cartas sobre la mesa en grupos de 3 o más") + "#\n" \
           + "#" + "{:^98}".format("e intentará completar las 7 necesarias para la canasta.") + "#\n" \
           + "#" + "{:^98}".format("En las canastas, tiene que haber un número mayor de cartas del mismo número que comodines.") + "#\n" \
           + "#" + "{:^98}".format("") + "#\n" \
           + "#" + "{:^98}".format("Existen los siguientes tipos de canastas:") + "#\n" \
           + f"{'#'*100}\n"

HOJA_15 = f"{'#'*100}\n" \
           + "#" + "{:^98}".format("• Limpia: Canasta de 7 cartas de números iguales, sin comodines. Vale 500 puntos.") + "#\n" \
           + "#" + "{:^98}".format("• Sucia: Canasta de 7 cartas con  1, 2 ó 3 comodines. Vale 300 puntos.") + "#\n" \
           + "#" + "{:^98}".format("• Oculta: Canasta que se realiza en la mano, sin mostrar ninguna carta. Vale 1000 puntos.") + "#\n" \
           + "#" + "{:^98}".format("• De Comodines Sucia: Canasta de 7 comodines, combinando jokers con dos. Vale 2000 puntos.") + "#\n" \
           + "#" + "{:^98}".format("• De Comodines Limpia: Canasta de 7 comodines iguales: 7 dos o 7 jokers. Vale 3000 puntos.") + "#\n" \
           + f"{'#'*100}\n"

LIBRO = [HOJA_1, HOJA_2, HOJA_3, HOJA_4, HOJA_5,
         HOJA_6, HOJA_7, HOJA_8, HOJA_9, HOJA_10,
         HOJA_11, HOJA_12, HOJA_13, HOJA_14, HOJA_15]


if __name__ == "__main__":
    ver_reglas()
