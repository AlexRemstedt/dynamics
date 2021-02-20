"""
Alex Remstedt
Kinematics
"""
# Imports
import numpy as np


class Kinematics(object):
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
            time = [0, 200]
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
            return None

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