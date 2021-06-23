# encoding=utf-8
"""
==========================
Massa-veersysteem op wiel
==========================
Author: Alex Remstedt
Date: 23/06/2021

obj 1
=====
Give the relation between u and dy.
:answer: spring_displacement
"""
# imports
import numpy as np

# time
t0 = 0

# mass
m = 20  # kg
g = 9.81  # m/s/s
r1 = .19  # m

# spring
k = 600  # N/m
r2 = .06  # m

# cylinder
M = 45  # kg
k_G = .134  # m


def spring_displacement(dy) -> float:
    """Calculate the displacement u of a spring as a function of dy.

    :param float dy: Difference in height (y).
    :return: displacement of the spring.
    """
    u = r2 / r1  * dy
    return u