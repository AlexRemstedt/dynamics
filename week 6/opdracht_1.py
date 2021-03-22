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
f_ext = np.array([1500, 0])  # N


def to_accent(coordinate, theta):
    return np.array([np.cos(theta) * coordinate[0], np.sin(theta) * coordinate[1]])


def from_accent(coordinates, theta):
    return np.array([np.arccos(theta) * coordinates[0], np.arcsin(theta) * coordinates[1]])


def moment():



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