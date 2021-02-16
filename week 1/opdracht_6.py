"""
	Author : Alex Remstedt
	Opdrachten 6, 7
"""
# === Imports ===
import numpy as np
from matplotlib import pyplot as plt

# === Variables ===
dt = 0.1  	# [s] grootte van tijdstappen
t0 = 0  	# [s] Starttijd van simulatie
t1 = 10  	# [s] Eindtijd van sim
x0 = 0  	# [m] beginpositie
v0 = 0  	# [m/s] beginsnelheid
a0 = -9.81  # [m/s^2] beginacceleratie
m = 7.0  	# [kg] massa

time = np.linspace(t0, t1, 1 + round((t1 - t0) / dt))  # time


# === Functions ===
def numeriek(start_positie, start_snelheid, tijd):
	"""

	:param start_positie: De start positie
	:param start_snelheid: De start snelheid
	:param tijd: Tijd (in vector vorm)
	:return: De posities op elk tijdstip in een np.array
	"""
	# Function variables
	positie = np.zeros(len(tijd))
	snelheid = np.zeros(len(tijd))
	acceleratie = versnelling(tijd)

	positie[0] = start_positie
	snelheid[0] = start_snelheid

	for t in range(len(tijd) - 1):
		d_t = tijd[t + 1] - tijd[t]
		snelheid[t + 1] = snelheid[t] + acceleratie[t] * d_t
		positie[t + 1] = positie[t] + snelheid[t] * d_t
	return positie


def analytisch(start_positie, start_snelheid, tijd):
	"""
	a = cos(t)/m ==> v = v0 + sin(t)/m ==> s = s0 + v0*t - (cos(t) - 1)/m
	:param start_positie: beginpositie
	:param start_snelheid: beginsnelheid
	:param tijd: tijd
	:return:
	"""
	global m
	position = np.zeros(len(tijd))  # Position vector

	for t in range(len(tijd)):
		position[t] = start_positie + start_snelheid * tijd[t] - np.cos(tijd[t])/m + 1/m
	return position


def versnelling(t):
	"""

	:param t: tijd
	:return:
	"""
	global m
	f = np.cos(t)
	a = f / m
	return a


# === Returns ===
# n = numeriek(x0, v0, 0, time)
# n -= analytisch(x0, v0, 0, time)

# === Prints ===
print(f'Positie voor t = {6.1} volgens numerieke integratie: {numeriek(x0, v0, time)[61]}')
print(f'Positie voor t = {6.1} volgens analytische benadering: {analytisch(x0, v0, time)[61]}')
print(f'Verschil voor t = 6.1 : {abs(numeriek(x0, v0, time)[61]-analytisch(x0, v0, time)[61])}')

# === Plots ===
fig, ax = plt.subplots(1, 2)
ax[0].plot(time, numeriek(x0, v0, time))  # Plot de numerieke resultaten
ax[0].plot(time, analytisch(x0, v0, time), 'y--')  # Plot analytische resultaten als gele stippellijn
ax[1].plot(time, abs(numeriek(x0, v0, time) - analytisch(x0, v0, time)))  # Plot het verschil

plt.show()
