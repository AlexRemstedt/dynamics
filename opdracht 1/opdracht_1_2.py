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
x0 = 1.3  # [m] beginpositie
v0 = 40  # [m/s] beginsnelheid
a0 = -9.81  # [m/s^2] beginacceleratie

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
	acceleratie[0:] = start_acceleratie

	for t in range(len(tijd) - 1):
		d_t = tijd[t + 1] - tijd[t]
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
	v_num = v + a * t
	position = x + v_num * t
	return position


n = numeriek(x0, v0, 0, time)
n -= analytisch(x0, v0, 0, time)

print(numeriek(x0, v0, a0, time)[-1])
print(n[-1])

# Plots
fig, ax = plt.subplots(1, 2)
ax[0].plot(time, numeriek(x0, v0, a0, time))  # Plot de numerieke resultaten
ax[0].plot(time, analytisch(x0, v0, a0, time), 'y--')  # Plot analytische resultaten als gele stippellijn
ax[1].plot(time, n)  # Plot het verschil
plt.show()
