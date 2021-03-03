"""
Alex Remstedt
01/03/2020

Opdracht 6 Week 4 - Energie Vervolg
https://secure.ans-delft.nl/universities/1/courses/63457/assignments/200359/quiz/show/38474120
"""

# Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Vars
m = 15          # kg
k = 90          # N/m
g = 9.81        # m/s^2
dt = 0.001      # s
t0 = 0          # s
t1 = 11         # s
y0 = 0.7        # m
v0 = 0.6        # m/s
omega_n = np.sqrt(k/m)

# Tijdlijsten
tijd = np.linspace(t0, t1, round(1 + (t1 - t0) / dt))


def ekin(v):
    """
    Kinetic Energy

    :param v: velocity
    :type v: np.ndarray
    :return: Kinetic energy
    """
    return .5 * m * v ** 2


def epot(h):
    """
    Potential Energy

    :param h: height
    :type h: np.ndarray
    :return:
    """
    grav = m * g * h
    spring = -.5 * k * h ** 2
    return grav + spring


def afgeleiden(state, t):
    """
    Afgeleiden calculates the derivatives

    :param state: A list containing [position, speed]
    :type state: list
    :param t: time
    :type t: float
    :return: list with velocity and acceleration
    """
    y = state[0]
    v = state[1]
    a = -omega_n ** 2 * y + g
    return [v, a]


resultaat = odeint(afgeleiden, [y0, v0], tijd)

y_num = resultaat[:, 0]
v_num = resultaat[:, 1]


# Antwoorden
# b)
print(f'b) {y_num[-1]}')