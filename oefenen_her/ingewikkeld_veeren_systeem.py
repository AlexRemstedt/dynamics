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

def gravity(m, **kwargs):
    if kwargs['vector']:
        return np.array([0, -m * 9.81, 0])
    return -m * 9.81

def spring_force():
    return None

def _main():
    return f"""
{gravity(10, vector=True)=}

"""


if __name__ == "__main__":
    print(_main())