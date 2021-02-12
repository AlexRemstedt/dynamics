"""
Author: Alex Remstedt
"""
# Imports:
from matplotlib import pyplot as plt
import numpy as np

# Variables
dt = 0.1  # [s] grootte van tijdstappen
t0 = 0  # [s] Starttijd van simulatie
t1 = 10  # [s] Eindtijd van sim
x0 = 1.3  # [m] beginpositie
v0 = 5.5  # [m/s] beginsnelheid

x = np.linspace(t0, t1, 1 + round((t1-t0)/dt))


def analytisch(x, v, a, t):
	"""

	:param x:
	:param v:
	:param a:
	:param t:
	:return:
	"""
	pass
