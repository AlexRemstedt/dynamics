# encoding=utf-8
# author: AlexRemstedt
# creation date: 14/04/2021
"""
answers question asked in week 7 assignment 1: rollend wagentje - voorbereiding
    https://secure.ans-delft.nl/universities/1/courses/63457/assignments/230492/quiz/show/43676046
"""
# imports
import numpy as np
import math
# import converter  # import deg_to_rad

# time
t0 = 0  # s [begintime]
t1 = 10   # s [endtime]
dt = .001  # s [timestep]
time = np.linspace(t0, t1, round(1 + (t1 - t0) / dt))  # s [timevector]

# initial values
length = 1.6  # m [length of pendulum]
s_A0 = np.array([8, 0, 0])  # m [initial position of A]
theta_0 = np.array([0, 0, 115 * math.pi / 180])  # rad [initial angle]
omega_0 = np.array([0, 0, -3.6])  # rad/s [initial angle velocity]
v_A0 = np.array([23, 0, 0])  # m/s [inital linear velocity of A]


def relative_position_b(theta) -> np.ndarray:
    """
    Calculate relative position of b.

    :param theta: angle in randians
    :type theta: np.ndarray
    :return:
    """
    rel_x = length * np.cos(theta[-1])
    rel_y = length * np.sin(theta[-1])
    return np.array([rel_x, rel_y])


def main():
    prints = f"""
{relative_position_b(theta_0)}
"""
    return prints


if __name__ == '__main__':
    print(main())