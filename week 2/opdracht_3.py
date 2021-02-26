# -*- Coding: UTF-8 -*-
"""
General Info:
    Alex Remstedt
    https://secure.ans-delft.nl/universities/1/courses/63457/assignments/144684/quiz/show/37991336
    Week 2 - Opdracht 3 - Een Grotere Boot
\
Opdracht bescrijving:
    Laten we nu naar een andere (grotere) boot kijken. Deze versnelt niet, maar heeft een initiële snelheid en zal
    afremmen door de weerstand van het water. Deze boot komt ook voor in een vak van Maritieme Techniek, en daarom
    laten we ook zien hoe het blokdiagram van dat vak aansluit bij de numerieke integratie die we hier doen.
\
    In de rechter figuur zie je een blokdiagram. In dit diagram staan de dynamische vergelijkingen van de boot
    schematisch weergegeven. De vergelijkingen kunnen hier eenvoudig uitgehaald worden:

    1) Linksboven: Som van de krachten De neerwaartse pijl die uit het +-teken komt heeft de totale som van de krachten
        op de boot F_prop - F_ship, waar F_ship eigenlijk de weerstandskracht op het ship betekent. De vergelijking
        die hier weergegeven is is:

    2) Rechtsboven: Snelheidsafhankelijke weerstandskracht Het blok “Ship Resistance” kan simpelweg een
        vermenigvuldigingsfactor zijn waarbij de uitgaande pijl F_ship gelijk is aan de inkomende pijl (snelheid v_s)
        maal een constante weerstandsfactor. Als dit het geval zou zijn noemen we dit “Lineaire demping”. In de opgave
        vandaag zal de weerstand echter niet-linear afhangen van de snelheid. Dit is niet te zien in het blokkenschema,
        maar de formule is als volgt: F_ship = 1000 * v_s^3

    3) Links midden: De wet van Newton Het blok links in het midden kan ook gezien worden als een soort
        vermenigvuldiging. Letterlijk staat er "neem de inkomende pijl (som van de krachten), vermenigvuldig dit met 1/m
        en integreer dit over de tijd om de uitgaande pijl te krijgen (v_s). De vergelijkingen hiervoor zijn dus:
        a = 1/m * F_tot en v_s = integrate(a*dt)
\
    Deze set vergelijkingen is bijna exact hetzelfde als wat we in de vorige vragen hebben gebruikt. Het enige verschil
    is dat de kracht nu een functie is van de snelheid, wat dan weer een effect heeft op de versnelling en de snelheid.
    Dit is een “closed loop” zoals te zien in de figuur.
\
    Gebruik de volgende initiële toestand en parameters:

    x0      |       0       [m]     \n
    v0      |       10      [m/s]   \n
    m       |       100000  [kg]    \n
    F_prop  |       0       [N]     \n

Vragen:
    a)

"""
# Imports
import numpy as np


class Kinematics(object):
    def __init__(self, x0=0, v0=0, a0=0, mass=0, time=None, dt=0.1, formula=None):
        """
        __init__ function

        :param x0: start positie
        :type x0: float
        :param v0: start snelheid
        :type v0: float
        :param a0: Start versnelling
        :type a0: float
        :param mass: massa
        :type mass: float
        :param time: tijden in de simulatie
        :type time: list
        :param dt: tijdstap van de simulatie
        :type dt: float
        """
        if time is None:
            time = [0, 400]
        self.startPosition = x0
        self.startSpeed = v0
        self.startAcceleration = a0
        self.mass = mass
        self.timeList = time
        self.timeStep = dt
        self.time = np.linspace(time[0], time[-1], 1 + round((time[-1] - time[0]) / dt))
        self.formula = formula

    # Usefull methods (back-end)

    def numeric_analysis(self):
        """
        Calculate position, velocity and acceleration by method of numerical integration

        :return: position, velocity, acceleration
        """
        position = np.zeros(len(self.time))
        velocity = np.zeros(len(self.time))
        acceleration = np.zeros(len(self.time))

        position[0] = self.startPosition
        velocity[0] = self.startSpeed
        acceleration[0] = self.startAcceleration

        for n in range(len(self.time) - 1):
            if self.time[n] <= self.timeList[1]:
                acceleration[n] = -100 * velocity[n] ** 3 / self.mass
            velocity[n + 1] = velocity[n] + acceleration[n] * self.timeStep
            position[n + 1] = position[n] + velocity[n] * self.timeStep

        return position, velocity, acceleration

    def analytic_analysis(self):
        """
        Calculate position, velocity and acceleration by method of analytical integration by hand.

        :return: position, velocity, acceleration
        """
        # Empty vectors
        position = np.zeros(len(self.time))
        velocity = np.zeros(len(self.time))
        acceleration = np.zeros(len(self.time))

        position[0] = self.startPosition
        velocity[0] = self.startSpeed
        acceleration[0] = self.startAcceleration

        for n in range(len(self.time)):
            if self.time[n] <= self.timeList[1]:
                acceleration[n] = 11 / self.mass
                velocity[n] = 11 * self.time[n] / self.mass + self.startSpeed
                position[n] = self.time[n] ** 2 * 11 / 2 / self.mass + \
                              self.startSpeed * self.time[n] + self.startPosition
            else:
                pass
        return position, velocity, acceleration

    # Easy methods (front-end
    def analytic_position(self):
        """
        Return the analytic position from analytic_analysis().

        :return: Position be analytic integration
        """
        return self.analytic_analysis()[0]

    def analytic_velocity(self):
        """
        Return the analytic velocity from analytic_analysis().

        :return: Velocity be analytic integration
        """
        return self.analytic_analysis()[1]

    def analytic_acceleration(self):
        """
        Return the analytic acceleration from analytic_analysis().

        :return: Acceleration be analytic integration
        """
        return self.analytic_analysis()[2]

    def numeric_position(self):
        """
        Return the numerical position from numeric_analysis().

        :return: Position by numerical integration
        """
        return self.numeric_analysis()[0]

    def numeric_velocity(self):
        """
        Return the numerical velocity from numeric_analysis().

        :return: Velocity by numerical integration
        """
        return self.numeric_analysis()[1]

    def numeric_acceleration(self):
        """
        Return the numerical acceleration from numeric_analysis().

        :return: Acceleration by numerical integration
        """
        return self.numeric_analysis()[2]


opdracht3 = Kinematics(v0=10.0, time=[0, 20], mass=100_000)

print(f'a: {opdracht3.numeric_velocity()[-1]}')
# opdracht3.time = [0, ]
print(f'b: {np.interp(x=8, xp=opdracht3.time, fp=opdracht3.numeric_position())}')
