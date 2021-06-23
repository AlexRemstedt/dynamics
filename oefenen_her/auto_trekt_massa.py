# encoding=utf-8
"""
=========================
Een auto trekt een massa
=========================
Author: Alex Remstedt
Date: 23/06/2021

obj 1
=====
Find the moment the block starts moving.
:answer: startmoving(car_force_0)

obj 2
=====
Find the speed of the block at t = 3.1 s
:answer: speed()
"""

# time
t0 = 0
t2 = 3.1  # endtime

# block
mass = 25  # kg
g = 9.81  # m/s/s
static_friction = .47
kinetic_friction = .32

# car
car_force_0 = 13.91


def force_car_integrated(t, start_force=car_force_0, tau=1, beta=2.5):
    force = start_force / tau ** beta / (beta + 1) * t ** (beta + 1)
    return force


def force_friction_integrated(t):
    force = kinetic_friction * mass * g * t
    return force


def start_moving(start_force, tau=1, beta=2.5) -> float:
    """Calculate the time when block starts moving.

    :param float start_force: Force at t = 0 s.
    :param float tau: factor 
    :param float beta: factor
    :return: Time at which the block starts moving.
    """
    force = static_friction * mass * g
    t = (force * tau ** beta / start_force) ** (1 / beta)
    return t


def speed():
    """Determine the absolute speed at a given time.

    :param
    """
    t1 = start_moving(car_force_0)
    v = (force_car_integrated(t2) - 
         force_car_integrated(t1) -
         force_friction_integrated(t2) + force_friction_integrated(t1)) / mass
    return v
    


def main():
    return f""" 
{start_moving(car_force_0)=}
{speed()=}
"""


if __name__ == "__main__":
    print(main())
