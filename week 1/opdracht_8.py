"""
	Author : Alex Remstedt
	Opdrachten: 8

	To Do:
		TODO: form analytical == numeric, but size !=.
"""
# === Imports ===
import numpy as np
from matplotlib import pyplot as plt

# === Variables ===
dt = 0.1  		# [s] grootte van tijdstappen
t_begin = 0  	# [s] Starttijd van simulatie
t1 = 10			# [s] time in between
t_end = 18.8  	# [s] Eindtijd van sim
x0 = 0  		# [m] beginpositie
v0 = 0  		# [m/s] beginsnelheid
a0 = -9.81  	# [m/s^2] beginacceleratie
m = 6.0  		# [kg] massa

time = np.linspace(t_begin, t_end, 1 + round((t_end - t_begin) / dt))  # time


# === Functions ===
def numeriek(start_positie, start_snelheid, tijd):
	"""
	:param start_positie: De start positie
	:type start_positie: float
	:param start_snelheid: De start snelheid
	:type start_snelheid: float
	:param tijd: Tijd (in vector vorm)
	:type tijd: np.ndarray
	:return: De posities op elk tijdstip in een np.array door middel van numerieke integratie
	"""
	# Function variables
	global dt, t1

	positie = np.zeros(len(tijd))
	snelheid = np.zeros(len(tijd))
	acceleratie = np.zeros(len(tijd))

	positie[0] = start_positie
	snelheid[0] = start_snelheid

	for t in range(len(tijd) - 1):
		if tijd[t] < t1:
			acceleratie[t] = versnelling(tijd[t])
		else:
			acceleratie[t] = 0
		snelheid[t + 1] = snelheid[t] + acceleratie[t] * dt
		positie[t + 1] = positie[t] + snelheid[t] * dt
	return positie


def analytisch(start_positie, start_snelheid, tijd):
	"""
	:param start_positie: beginpositie
	:type start_positie: float
	:param start_snelheid: beginsnelheid
	:type start_snelheid: float
	:param tijd: tijd
	:type tijd: numpy.array
	:return:
	"""
	global m, t1
	position = np.zeros(len(tijd))  # Position vector

	for t in range(len(tijd)):
		if tijd[t] < t1:
			acceleration_part = 3.5 * tijd[t] ** 3 / 6 / m
			position[t] = start_positie + start_snelheid * tijd[t] + acceleration_part
		else:
			position[t] = (3.5 * 1000 / 6 + tijd[t] ** 2 / 2 + 165 * tijd[t] - 1700) / m
	return position


def versnelling(t):
	"""
	:param t: tijd
	:type t: float
	:return: the acceleration at t
	"""
	global m
	f = 3.5 * t
	a = f/m
	return a


# === Prints ===
print(f'Positie voor t = {t_end} volgens numerieke integratie: {numeriek(x0, v0, time)[-1]}')
print(f'Positie voor t = {t_end} volgens analytische benadering: {analytisch(x0, v0, time)[-1]}')
print(f'Verschil voor t = {t_end} : {abs(numeriek(x0, v0, time)[-1]-analytisch(x0, v0, time)[-1])}')

# === Plots ===
fig, ax = plt.subplots(1, 2)
ax[0].plot(time, numeriek(x0, v0, time))  # Plot de numerieke resultaten
ax[0].plot(time, analytisch(x0, v0, time), 'y--')  # Plot analytische resultaten als gele stippellijn
ax[1].plot(time, abs(numeriek(x0, v0, time) - analytisch(x0, v0, time)))  # Plot het verschil

plt.show()
