# encoding=utf-8
"""
==========================
Massa-veersysteem op wiel
==========================
Author: Alex Remstedt
Date: 23/06/2021

obj 1
=====
What is the angular speed of the coil?
:answer: angular_velocity(.85)
"""
# imports
import numpy as np

# time
t0 = 0

# mass
m = 20  # kg
g = 9.81  # m/s/s
r1 = .19  # m

# spring
k = 600  # N/m
r2 = .06  # m

# coil
big_m = 45  # kg
k_G = .134  # m


def spring_displacement(dy) -> float:
    """Calculate the displacement u of a spring as a function of dy.

    :param float dy: Difference in height (y).
    :return: Displacement of the spring.
    """
    u = r2 / r1 * dy
    return u


def angular_velocity(dy) -> float:
    """Calculate the angular velocity of the coil

    :param float dy: Difference in height (y).
    :return: Angular speed of the coil. 
    """
    v_mass = m * g * dy
    v_spring_2 = k * (r2 / r1 * dy) ** 2
    t_mass_2 = m * r1 ** 2
    t_coil_2 = big_m * k_G ** 2
    return ((2 * v_mass - v_spring_2) / (t_mass_2 + t_coil_2)) ** (1/2)


def main() -> str:
    """Main prints."""
    return f"""
{angular_velocity(.85)=}
    """


if __name__ == "__main__":
    print(main())
