# encoding=utf-8
"""
=====
Ingewikkeld veersysteem.
=====
Author: Alex Remstedt
Date: 14/06/2021

obj 1
=====

:ans:
"""
# imports
import numpy as np
from numpy.linalg import norm

# object (= circular)
mass = 7  # kg
r = np.array([1, 2, 0])
centre = np.array([7, -7, 0])


# spring 1 (BC)
k = 6  # N/m
l1 = np.array([2, 2, 0])  # m


def gravity(m, **kwargs) -> np.ndarray[float]:
    """Calculate the gravitational force of an object.
    
    :param float m: the mass of the object in kg
    :return: gravitational force
    """
    if kwargs['vector']:
        return np.array([0, -m * 9.81, 0])
    return -m * 9.81


def spring_force(u):
    f = k * u
    return f


def _main():
    return f"""
{gravity(10, vector=True)=}

"""


if __name__ == "__main__":
    print(_main())
