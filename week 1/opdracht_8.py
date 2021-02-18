# -*- Coding: utf-8 -*-
"""
Author : Alex Remstedt  \n
Opdrachten: 8
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
	Numerieke integratie:
	De functie numeriek integreert numeriek over tijd. Om de acceleratie te bepalen neemt hij voor 0 < t < 10 deze van
	versnelling().

	:param start_positie: 	De start positie
	:type start_positie: 	float
	:param start_snelheid: 	De start snelheid
	:type start_snelheid: 	float
	:param tijd: 			Tijd (in vector vorm)
	:type tijd: 			np.ndarray
	:return: 				De posities op elk tijdstip in een np.array door middel van numerieke integratie
	"""
	# Function variables
	global dt, t1, m

	positie = np.zeros(len(tijd))
	snelheid = np.zeros(len(tijd))
	acceleratie = np.zeros(len(tijd))

	positie[0] = start_positie
	snelheid[0] = start_snelheid

	for t in range(len(tijd) - 1):
		if tijd[t] <= t1:
			acceleratie[t] = versnelling(tijd[t])
		else:
			acceleratie[t] = 0.25 * tijd[t] ** 3 / m
		snelheid[t + 1] = snelheid[t] + acceleratie[t] * dt
		positie[t + 1] = positie[t] + snelheid[t] * dt
	return positie, snelheid


def analytisch(start_positie, start_snelheid, tijd):
	"""
	Bij analystisch wordt de positie van een object bepaald met behulp van een van te vorne geintegreerde formule op
	analytische wijze.

	D_t = [0, 10]
		a(t) = 3.5 t / m  							[m/s^2] \n
		v(t) = 1.75 t^2 / m  						[m/s]	\n
		s(t) = 0.5833.. t^3 / m 					[m]		\n

	D_t = [10, 20]
		a(t) = 0.25 t^3 / m							[m/s^2] \n
		v(t) = (0.0625 t^4 - 450) / m				[m/s]	\n
		s(t) = (0.0125 t^5 - 450 t + 11500/3) / m	[m]		\n

	:param start_positie: 	beginpositie
	:type start_positie: 	float
	:param start_snelheid: 	beginsnelheid
	:type start_snelheid: 	float
	:param tijd: 			een lijst met verschillende tijden
	:type tijd: 			np.ndarray

	:return: 				Positie van object over tijd in een np.ndarray
	"""
	global m, t1
	position = np.zeros(len(tijd))  # Position vector

	for t in range(len(tijd)):
		if tijd[t] <= t1:
			acceleration_part = 3.5 * tijd[t] ** 3 / 6 / m
			position[t] = start_positie + start_snelheid * tijd[t] + acceleration_part
		else:
			position[t] = (11500/3 + (tijd[t] ** 5)/80 - 450*tijd[t]) / m
	return position


def versnelling(t):
	"""
	:param t: 	tijd
	:type t: 	float
	:return: 	the acceleration at t
	"""
	global m
	f = 3.5 * t
	a = f/m
	return a


# === Prints ===
print(f'Positie voor t = {t_end} volgens numerieke integratie: {numeriek(x0, v0, time)[0][-1]}')
print(f'Positie voor t = {t_end} volgens analytische benadering: {analytisch(x0, v0, time)[-1]}')
print(f'Verschil voor t = {t_end} : {abs(numeriek(x0, v0, time)[0][-1]-analytisch(x0, v0, time)[-1])}')

# === Plots ===
fig, ax = plt.subplots(1, 2)
ax[0].plot(time, numeriek(x0, v0, time)[0])  # Plot de numerieke resultaten
ax[0].plot(time, analytisch(x0, v0, time), 'y--')  # Plot analytische resultaten als gele stippellijn
ax[1].plot(time, abs(numeriek(x0, v0, time)[0] - analytisch(x0, v0, time)))  # Plot het verschil

plt.show()
