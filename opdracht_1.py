"""
Author: Alex Remstedt
"""
# Imports:
from matplotlib import pyplot as plt
import numpy as np

# Variables
dt = 0.1  # [s] grootte van tijdstappen
t0 = 0  # [s] Starttijd van simulatie
t1 = 5.4  # [s] Eindtijd van sim
x0 = 1.3  # [m] beginpositie
v0 = 5.5  # [m/s] beginsnelheid

time = np.linspace(t0, t1, 1 + round((t1-t0)/dt))


def numeriek(start_positie, start_snelheid, start_acceleratie, tijd):
	"""

	:param start_positie:
	:param start_snelheid:
	:param start_acceleratie:
	:param tijd:
	:return:
	"""
	# Function variables
	positie = np.zeros(len(tijd))
	snelheid = np.zeros(len(tijd))
	acceleratie = np.zeros(len(tijd))

	positie[0] = start_positie
	snelheid[0] = start_snelheid
	acceleratie += start_acceleratie

	for t in range(len(tijd) - 1):
		dt = tijd[t + 1] - tijd[t]
		snelheid[t + 1] = snelheid[t] + acceleratie[t] * dt
		positie[t + 1] = positie[t] + snelheid[t] * dt

	return f'positie: {positie[-1]} \n snelheid: {snelheid[-1]} \n acceleratie: {acceleratie[-1]}'


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

