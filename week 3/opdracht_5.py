"""
Alex Remstedt
01/03/2020

Opdracht 5 Week 4 - Energie
https://secure.ans-delft.nl/universities/1/courses/63457/assignments/200359/quiz/show/38474119
"""

# Imports
import numpy as np
import matplotlib.pyplot as plt

# Vars
m = 15          # kg
k = 90          # N/m
g = 9.81        # m/s^2
dt = 0.001      # s
t0 = 0          # s
t1 = 10         # s
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


def numeriek(t, begin_y, begin_v):
    """

    :param t: tijd
    :param begin_y: begin positie
    :param begin_v: begin snelheid
    :type t: float
    :type begin_y: float
    :type begin_v: float
    :return: numeric integration of the position and the veloctiy
    """
    y_num = np.full(len(t), begin_y)
    v_num = np.full(len(t), begin_v)
    for n in range(len(t) - 1):
        dt = t[n + 1] - t[n]
        snelheid, versnelling = afgeleiden([y_num[n], v_num[n]], t[n])
        y_num[n + 1] = y_num[n] + snelheid * dt
        v_num[n + 1] = v_num[n] + versnelling * dt
    return y_num, v_num


y_num, v_num = numeriek(tijd, y0, v0)

# Antwoorden
# a)
plt.plot(tijd, ekin(v_num))
print(f'a) {ekin(v_num)[-1]}')

# b)
plt.plot(tijd, epot(y_num))
plt.show()
print(f'b) {epot(y_num)[0] - epot(y_num[-1])}')
