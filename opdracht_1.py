"""
Author: Alex Remstedt
"""
# Imports:
from matplotlib import pyplot as plt
import numpy as np

# Variables
dt = 0.1  # [s] grootte van tijdstappen
t0 = 0  # [s] Starttijd van simulatie
t1 = 0.4  # [s] Eindtijd van sim
x0 = 1.3  # [m] beginpositie
v0 = 5.5  # [m/s] beginsnelheid

time = np.linspace(t0, t1, 1 + round((t1-t0)/dt))


def analytisch(x, v, a, t):
	"""

	:param x: beginpositie
	:param v: beginsnelheid
	:param a: beginversnelling
	:param t: tijd
	:return:
	"""
	position = x + v * t
	return position


print(analytisch(x0, v0, 0, 0.4))
