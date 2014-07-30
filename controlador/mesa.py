"""
Almacena las cartas que estan en la mesa
Maneja los turnos
Proporciona los metodos para levantar cartas
"""

class Mesa():
    cartas = []
    jugadores_idx = []
    jugador_turno = 0

    def __init__(jugadores = []):
        """
        Inicializa el objeto con los jugadores
        """
        self.jugadores = jugadores

    def jugada(jugador, carta):
        """
        Pasa la carta jugada a la mesa
        """
        cartas.append(jugadores[jugador][carta])

    def sumar(jugador, carta):
        """
        Suma todos los pares de cartas y retorna las cartas
        que cumplen la condicion
        """
        pass

    def sacar_igual(jugador_carta):
        """
        Identifica si existe una carta de igual valor
        """
        pass

    def turno():
        """
        Controla la secuencia de turnos
        """
        pass

class Juez():
    pass

