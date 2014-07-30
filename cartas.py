#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Juego cuarenta
----------------------------
Se reparten cartas del As al 7 más J, Q y K
entre dos jugadores por turnos. Cada jugador recibe
4 cuartas en cada mano.
La ronda termina cuando cada jugador a jugado todas sus cartas.
Si quedan más cartas por repartir se reparten caso contrario
se cuentan las cartas y se verifica si se ha ganado algún puntaje
y se vuelve a barajar.
**** Mecánica del juego *****
Se coloca una carta sobre la mesa y se queda ahí hasta que
algún jugador la levante
Una carta se levanta cuando:
    - Se coloca una carta del mismo valor de otra en la mesa
    - La carta es igual a la sumatoria de dos cartas en la mesa
    - Una carta en la mesa es inmediatamente superior a otra recogida
Puntuacion:
    - Si se retira la ultima carta que ha jugado el openente
      se dice que es caida y el jugador que levanta la carta
      recibe 2 puntos.
    - Si al levantar las cartas la mesa queda vacia se dice
      que es limpia y el jugador que ha levantado recibe 2
      puntos
    - Si se han levantado más de 16 cartas la que le sigue tiene una
      puntuacion de 2, cada carta adicional tiene una puntuacion de 2
      Si se termina en numero impar la puntuacion es el inmediato
      superior
"""

from random import randrange as R
numeros = ((1,'As'), (2, 'Dos'), (3, 'Tres'), (4, 'Cuatro'), (5, 'Cinco')
        , (6, 'Seis'), (7, 'Siete'), (8, 'J'), (9, 'Q'), (10, 'K'))

pila = []
palos = ('Treboles', 'Espadas', 'Corazones', 'Diamantes')
num_jugadores = 2
jugadores = {}
mesa = []
order = [0 for x in xrange(0, 39)]

def crear_cartas():
    global pila
    pila = []
    for n in numeros:
        for p in palos:
            pila.append((n,p))

def repartir_mesa():
    global jugadores
    global pila
    for i in xrange(2):
        jugadores.setdefault(i, [])
        for j in xrange(4):
            jugadores[i].append(pila.pop())


def barajar():
    for b in pila:
        idx = pila.index(b)
        idx_new = R(0,39)
        temp = pila[idx_new]
        pila[idx_new] = b
        pila[idx] = temp


crear_cartas()
barajar()
repartir_mesa()
print "Mis cartas"
for k,v in jugadores.iteritems():
    print k, v
