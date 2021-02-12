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
	global fig, ax

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

	return positie


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


n = numeriek(x0, v0, 0, time)
n -= analytisch(x0, v0, 0, time)

# Plots
fig, ax = plt.subplots(1, 2)
ax[0].plot(time, numeriek(x0, v0, 0, time))  # Plot de numerieke resultaten
ax[0].plot(time, analytisch(x0, v0, 0, time), 'y--')  # Plot analytische resultaten als gele stippellijn
ax[1].plot(time, n)  # Plot het verschil
plt.show()
