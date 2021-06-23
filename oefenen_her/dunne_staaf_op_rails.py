# encoding=utf-8
"""
======================
Dunne staaf op rails.
======================
Author: Alex Remstedt
Date: 23/06/2021

obj 1
=====
What is the speed of b at t1
:ans: speed_of_b()

obj 2
=====
What is the angular velocity of the rod after collision?
:ans: angular_velocity(-72.483)
"""
import numpy as np
from numpy.linalg import norm

# rod
omega_0 = np.array([0, 0, 3])  # rad/s
mass = 29  # kg

# point a
r_a = np.array([0, 0, 0])  # m
v_a = np.array([10, 0, 0])  # m/s

# point b
r_b = np.array([-6, -7, 0])  # m


def speed_of_b() -> float:
    """Calculate the speed of b

    :return: Norm of the velocity of b.
    """
    r_btova = r_b - r_a
    v_b = v_a + np.cross(omega_0, r_btova)
    return norm(v_b)

def angular_velocity(i_x) -> float:
    """Calculate the angular velocity of b.
    
    :return: the angular velocity in m/s 
    """
    return norm(omega_0) + r_b[1] * i_x * 6 / mass / norm(r_b) ** 2

def _main():
    return f"""
{speed_of_b()=}
{angular_velocity(-72.483)=}
"""

if __name__ == "__main__":
    print(_main())
