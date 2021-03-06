"""
Alex Remstedt
03/03/2021

Week 4 opdracht 1 - Een stuiterend object
https://secure.ans-delft.nl/universities/1/courses/63457/assignments/213009/quiz/show/38932272
"""
# Imports
import numpy as np


# Variables
m = 1.0         # kg
g = 9.81        # m/s^2
y0 = 1.1        # m
v0 = 0          # m/s
a0 = 0          # m/s^2
t0 = 0          # s
t1 = 1          # s
dt = 0.001      # s

# Answer vars
b = 0

time = np.linspace(t0, t1, round(1 + (t1 - t0) / dt))


# Functions
def f_zwaartekracht():
    """
    Bereken de zwaartekracht die werkt op het deeltje.

    :return: zwaartekracht
    """
    return m * -g


def f_totaal(y):
    """
    Tel de verschillende krachten die op het deeltje werken bij elkaar op

    :param y: Verplaatsing [m]

    :type y: float

    :return: Totale kracht
    """
    f = f_zwaartekracht()
    return f


def versnelling(y):
    """
    Bereken de versnelling van het deeltje op basis van de krachten die erop werken

    :param y: verplaatsing

    :type y: float

    :return: De acceleratie
    """
    a = f_totaal(y)/m
    return a


def numeriek(y0=0, v0=0, a0=0, t=None):
    """
    voer een numerieke Forward Euler methode uit om de plaats, snelheid en de versnelling van het deeltje te bepalen voor elk tijdstip in het

    :param y0: Startpositie
    :param v0: Startsnelheid
    :param a0: Startversnelling
    :param t: Tijd-array

    :type y0: float
    :type v0: float
    :type a0: float
    :type t: np.ndarray

    :return: positie, snelheid, versnelling
    """
    global b

    plaats = np.zeros(len(t))
    snelheid = np.zeros(len(t))
    acceleration = np.zeros(len(t))

    plaats[0] = y0
    snelheid[0] = v0
    acceleration[0] = a0

    for n in range(len(t) - 1):
        acceleration[n + 1] = versnelling(plaats[n + 1])
        snelheid[n + 1] = snelheid[n] + acceleration[n] * dt
        plaats[n + 1] = plaats[n] + snelheid[n] * dt
        if n == 90:  # voor b)
            b = f_totaal(plaats[n])

    return plaats, snelheid, acceleration


y_num, v_num, a_num = numeriek(y0, v0, a0, time)

print(f'a) {y_num[-1]}')
print(f'b) {b}')
