"""
Author: Alex Remstedt
"""
# Imports:
from matplotlib import pyplot as plt
import numpy as np

# Variables
dt = 0.1  # [s] grootte van tijdstappen
t0 = 0  # [s] Starttijd van simulatie
t1 = 6.1  # [s] Eindtijd van sim
x0 = 1.3  # [m] beginpositie (x-richting)
y0 = 0  # [m] Beginpositie (y-richting)
v0 = 40  # [m/s] beginsnelheid
a0 = -9.81  # [m/s^2] beginacceleratie

time = np.linspace(t0, t1, 1 + round((t1-t0)/dt))
print(len(time))


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
	acceleratie[0] = start_acceleratie

	for t in range(len(tijd) - 1):
		d_t = tijd[t + 1] - tijd[t]
		acceleratie[t + 1] = acceleratie[t]
		snelheid[t + 1] = snelheid[t] + acceleratie[t] * d_t
		positie[t + 1] = positie[t] + snelheid[t] * d_t

	return positie


def analytisch(x, v, a, t):
	"""

	:param x: beginpositie
	:param v: beginsnelheid
	:param a: beginversnelling
	:param t: tijd
	:return:
	"""
	x_an = np.zeros(len(t))

	for i in range(len(t)):
		x_an[i] = x + v * t[i] + 0.5 * a * t[i] ** 2
	return x_an


print(numeriek(y0, v0, a0, time)[-1])
print(abs(numeriek(y0, v0, a0, time)[-1]-analytisch(y0, v0, a0, time)[-1]))

# Plots
fig, ax = plt.subplots(1, 2)
ax[0].plot(time, numeriek(y0, v0, a0, time))  # Plot de numerieke resultaten
ax[0].plot(time, analytisch(y0, v0, a0, time), 'y--')  # Plot analytische resultaten als gele stippellijn
plt.show()
