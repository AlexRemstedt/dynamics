"""
Alex Remstedt
26/02/2021

Week 3 - Opdracht 1: Analytische Oplossingen
https://secure.ans-delft.nl/universities/1/courses/63457/assignments/200359/quiz/show/38474117
"""
# Imports
import numpy as np
import matplotlib.pyplot as plt

# Vars
m = 10  # kg
k = 110  # N/m
g = 0  # m/s^2
dt = 0.001  # s
t0 = 0  # s
t1 = 10  # s
y0 = 0.6  # m
v0 = 0.5  # m/s
omega_n = np.sqrt(k/m)

# maak de lijsten aan
t = np.linspace(t0, t1, round(1 + (t1 - t0) / (dt)))


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
    a = -omega_n ** 2 * y
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


y_num, v_num = numeriek(t, y0, v0)

# Prints
print(f"a: {omega_n/np.pi/2}")
print(f"b: {v0/omega_n}")
print(f"c: {y0}")

# Plots
fig, ax = plt.subplots(1, 2, figsize=(8, 3))
ax[0].plot(t, y_num)
ax[1].plot(t, v_num)
ax[0].set_xlabel('tijd [s]')
ax[1].set_xlabel('tijd [s]')
ax[0].set_ylabel('positie [s]')
ax[1].set_ylabel('snelheid [m/s]')
# plt.show()
