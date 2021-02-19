"""
General Info:
    Alex Remstedt
    https://secure.ans-delft.nl/universities/1/courses/63457/assignments/144684/quiz/show/37991335
    Week 2 - Opdracht 1 - Schroefloze boot
\
Opdracht beschrijving:
    Gebruik één van de bestanden uit de vorige Python opdracht om een simulatie van een boot te maken.
    Net als in die opdracht zullen wij de kracht geven als functie van de tijd en zal jij een numerieke en een
    analytische oplossing bepalen van de beweging als functie van de tijd.
\
    Een schroefloze boot begint met een initiële snelheid van 4.5 m/s en versnelt eenparig. De aandrijfkracht is 11 N,
    en de massa van de boot is 105 kg. Simuleer het pad dat de boot aflegt. Gebruik tijdstappen van 0.1s en een totale
    simulatietijd van 200s.
\
Vragen:
    a) Wat is de versnelling van de boot in [m/s^2]
    b) Wat is het numerieke resultaat voor de snelheid van de boot na t = 154.3 seconden?
    c) Wat is het analytische resultaat voor de positie van de boot na 154.3 seconden?
    d) Vergelijk de analytische en de numerieke oplossingen van de positie van de boot na 154.3 seconden. Wat is de absolute grootte van de fout?
    e) Maak een plot met de snelheid op de verticale as en de positie op de horizontale as. Hoe ziet deze plot eruit?
"""
# Imports
import numpy as np
from matplotlib import pyplot as plt


class Kinetics(object):
    def __init__(self, x0=0, v0=0, a0=0, mass=0, time=None, dt=0.1):
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
            time = [0, 0]
        self.startPosition = x0
        self.startSpeed = v0
        self.startAcceleration = a0
        self.mass = mass
        self.timeList = time
        self.timeStep = dt
        self.time = np.linspace(time[0], time[-1], 1 + round((time[-1] - time[0]) / dt))

    # Usefull methods (back-end)
    @staticmethod
    def force(equation=None, time=None):
        """
        Calculate the force where time is a parameter.

        :param equation: Equation chooser.
        :type equation: int
        :param time: (optional) The time at which the force must be calculated.
        :type time: float
        :return: The force at given time in [N] as float.
        """
        if equation is None:
            raise TypeError
        elif equation == 1:
            return 11  # [N]
        elif equation == 2:
            return None  # TODO: insert equation

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
                acceleration[n] = self.force(1, self.time[n]) / self.mass
            else:
                acceleration[n] = self.force(2, self.time[n]) / self.mass
            velocity[n + 1] = velocity[n] + acceleration[n] * self.timeStep
            position[n + 1] = position[n] + velocity[n] * self.timeStep

        return position, velocity, acceleration

    def analytic_analysis(self):
        """
        Calculate position, velocity and acceleration by method of analytical integration by hand.

        :return: position, velocity, acceleration
        """
        # Position
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


opdracht1 = Kinetics(v0=4.5,
                     mass=105,
                     time=[0, 154.3],
                     dt=0.1)
# Answers
print(f'a: {opdracht1.analytic_acceleration()[-1]}')
print(f'b: {opdracht1.numeric_velocity()[-1]}')
print(f'c: {opdracht1.analytic_position()[-1]}')
print(f'd: {abs(opdracht1.numeric_position()[-1] - opdracht1.analytic_position()[-1])}')

fig, ax = plt.subplots(1)
plt.plot(opdracht1.numeric_position(), opdracht1.numeric_velocity())  # e
plt.show()
