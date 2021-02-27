"""
Alex Remstedt
26/02/2021

Week 3 - Opdracht 1: Massa-Veer Systeem
https://secure.ans-delft.nl/universities/1/courses/63457/assignments/200359/quiz/show/38474115
"""
# Imports
import numpy as np
import matplotlib.pyplot as plt

# Vars
m = 9  # kg
k = 146  # N/m
g = 9.81  # m/s^2
dt = 0.001  # s
t0 = 0  # s
t1 = 10  # s
y0 = 0.6  # m
v0 = 0.7  # m/s

# maak de lijsten aan
t = np.linspace(t0, t1, round(1 + (t1 - t0) / (dt)))


def afgeleiden(state, t):
    """
    Afgeleiden calculates the derivatives.

    :param state: A list containing [position, speed]
    :type state: list
    :param t: time
    :type t: float
    :return: list with velocity and acceleration
    """
    y = state[0]
    v = state[1]
    a = g
    return [v, a]


def numeriek(t, begin_y, begin_v):
    """

    :param t:
    :param begin_y:
    :param begin_v:
    :return:
    """
    y_num = np.full(len(t), begin_y)
    v_num = np.full(len(t), begin_v)
    for n in range(len(t) - 1):
        dt = t[n + 1] - t[n]
        snelheid, versnelling = afgeleiden([y_num[n], v_num[n]], t[n])
        y_num[n + 1] = y_num[n] + snelheid * dt
        v_num[n + 1] = v_num[n] + versnelling * dt
    return y_num, v_num


y_numerical, v_numerical = numeriek(t, y0, v0)

# Prints
print(y_numerical[-1])

# Plots
fig, ax = plt.subplots(1, 2, figsize=(8, 3))
ax[0].plot(t, y_numerical)
ax[1].plot(t, v_numerical)
ax[0].set_xlabel('tijd [s]')
ax[1].set_xlabel('tijd [s]')
ax[0].set_ylabel('positie [s]')
ax[1].set_ylabel('snelheid [m/s]')
plt.show()
