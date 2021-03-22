"""
Alex Remstedt
19/03/2021

Week 6 opdracht 1 - [Mini-Hovercraft]
https://secure.ans-delft.nl/universities/1/courses/63457/assignments/225494/quiz/show/40967093
"""
# imports
import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt
from converter import deg_to_rad, to_accent

# vars
m = 500  # kg
i = 310  # kg m^2
r_fext = np.array([0, -.9])  # m --> r'
f_ext = np.array([1500, 0])  # N

# time
t0 = 0  # s
t1 = 44  # s
dt = 0.001  # s
time = np.linspace(t0, t1, round(1 + (t1 - t0) / dt))  # s

# initial values
theta0 = 0  # rad
omega0 = 0  # rad/s
x0 = 0  # m
v0 = 0  # m/s


def moment(f, r):
    """
    Calculate force moment

    :param f: force
    :param r: arm

    :return: force moment
    """
    return np.cross(r, f)


def ang_kinematics(state, t):
    """
    Calculate angular derivatives

    :param state: [angle, angular velocity]
    :param t: time array

    :type state: list
    :type t: np.ndarray

    :return:
    """
    theta = state[0]
    omega = state[1]
    alpha = moment() / i
    return omega, alpha