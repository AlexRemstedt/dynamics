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
"""
# Imports
import numpy as np


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
        if equation == None:
            raise Error
        if equation == 1:
            return 11  # [N]
        elif equation == 2:
            return None  # TODO: insert equation
        else:
            raise AttributeError

    def numeric_analysis(self):
        """
        # TODO
        :return:
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

    # Easy methods (front-end
    def numeric_position(self):
        return self.numeric_analysis()[0]

    def numeric_velocity(self):
        return self.numeric_analysis()[1]

    def numeric_acceleration(self):
        return self.numeric_analysis()[2]


opdracht1 = Kinetics(v0=4.5,
                     mass=105,
                     time=[0, 154.3],
                     dt=0.1)

print(opdracht1.numeric_velocity()[-1])
print(opdracht1.numeric_position()[-1])
