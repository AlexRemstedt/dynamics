"""
Alex Remstedt
Kinematics
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
    def formula_picker(self):
        """
        Choose a formula.

        :return: corresponding formula.
        """
        if self.formula is None:
            return 0
        elif self.formula == 1:
            return ForceFormulas.formula_1()

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
                acceleration[n] = self.formula_picker() / self.mass
            else:
                acceleration[n] = self.formula_picker() / self.mass
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


class ForceFormulas(Kinematics):
    def __init__(self, time):
        super().__init__(time)

    @staticmethod
    def formula_1():
        """
        Calculate the force where time is a parameter.

        In formula_1 (not a reference to the autosport)

        :return: The force at given time in [N] as float.
        """
        return 11
