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
t0 = 0          # s
t1 = 1          # s
dt = 0.001      # s


# Functions
def f_zwaartekracht():
    """
    Bereken de zwaartekracht die werkt op het deeltje.

    :return: zwaartekracht
    """
    return m * g


def f_totaal(y):
    """
    Tel de verschillende krachten die op het deeltje werken bij elkaar op

    :param y: Verplaatsing [m]
    :type y:
    :return: Totale kracht
    """
    f = None
    return f


def versnelling(y):
    """
    Bereken de versnelling van het deeltje op basis van de krachten die erop werken

    :param y: verplaatsing
    :type y:
    :return: De acceleratie
    """
    a = None
    return a


def numeriek(y0, v0, a0, t):
    """
    voer een numerieke Forward Euler methode uit om de plaats, snelheid en de versnelling van het deeltje te bepalen voor elk tijdstip in het

    :param y0:
    :param v0:
    :param a0:
    :param t:

    :type y0:
    :type v0:
    :type a0:
    :type t:

    :return:
    """
    y = None
    v = None
    a = None
    return y, v, a
