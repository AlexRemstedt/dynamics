"""
Alex Remstedt
06/03/2021

Week 4 opdracht 2 - Toevoegen van de vloer
https://secure.ans-delft.nl/universities/1/courses/63457/assignments/213009/quiz/show/38932273
"""
# Imports
import numpy as np
from matplotlib import pyplot as plt


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


def f_floor(y):
    """
    Bereken de kracht waarmee een bal terugstuitert

    :param y: Height
    :return: stuiterkracht
    """
    k_floor = 1100  # N/m
    f = -k_floor * y
    return np.maximum(f, 0)


def f_totaal(y):
    """
    Tel de verschillende krachten die op het deeltje werken bij elkaar op

    :param y: Verplaatsing [m]

    :type y: float

    :return: Totale kracht
    """
    f = f_zwaartekracht() + f_floor(y)
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


def e_kin(v):
    """
    Calculate the kinetic energy

    :param v: velocity

    :return: kinetic energy
    """
    return 0.5 * m * v ** 2


def e_pot(h):
    """
    Calculate the potential energy

    :param h: height

    :return: potential energy
    """
    return m * g * h


def numeriek(y0=0, v0=0, a0=0, t=None):
    """
    voer een numerieke Forward Euler methode uit om de plaats, snelheid en de versnelling van het deeltje te bepalen
    voor elk tijdstip.

    :param y0: Startpositie
    :param v0: Startsnelheid
    :param a0: Startversnelling
    :param t: Tijd

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
        acceleration[n] = versnelling(plaats[n])
        snelheid[n + 1] = snelheid[n] + acceleration[n] * dt
        plaats[n + 1] = plaats[n] + snelheid[n] * dt

    return plaats, snelheid, acceleration


y_num, v_num, a_num = numeriek(y0, v0, a0, time)

# a)
plt.plot(time, y_num)
plt.plot(time, v_num)
plt.plot(time, a_num)
# plt.show()

c = np.interp(x=np.min(y_num), xp=y_num, fp=v_num)
print(c)

print(f'b) {np.min(y_num)}')
