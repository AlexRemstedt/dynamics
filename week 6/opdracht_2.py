# encoding: utf-8
# author: Alex Remstedt
# date: 22/03/2021
"""
Week 6 opdracht 2 - Mini hovercraft
https://secure.ans-delft.nl/universities/1/courses/63457/assignments/225494/quiz/show/40967094
"""
# imports
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from converter import from_accent, deg_to_rad

# constants
m = 500  # kg
i = 310  # kg m^2
radius = np.array([0, -.9])
force = np.array([1500, 0])

# time
t0 = 0  # s
t1 = 28  # s
dt = .001  # s
time = np.linspace(t0, t1, round(1 + (t1 - t0) / dt))  # s

# initial values
theta_0 = 0
omega_0 = 0
x0 = np.array([0, 0])
v0 = np.array([0, 0])


# functions
def moment(f, r):
    """
    Calculate force moment

    :param f: force
    :param r: arm

    :return: force moment
    """
    return np.cross(r, f)


def ang_kinematics(state, t):
    """
    Calculate angular derivatives

    :param state: [angle, angular velocity]
    :param t: time array

    :type state: list
    :type t: np.ndarray

    :return:
    """
    theta = state[0]
    omega = state[1]
    alpha = moment(force, radius) / i
    return omega, alpha


def lin_kinematics(theta):
    """
    calculate the linear kinematics

    :param theta: angles in radians

    :type theta: np.ndarray

    :return: tuple of position and velocity vectors in x and y direction.
    :rtype: tuple
    """
    v = []
    s = []

    v.append(v0)
    s.append(x0)
    for n in range(len(theta) - 1):
        a = np.array([force[0] * np.cos(theta[n]) / m, force[0] * np.sin(theta[n]) / m])
        v.append(v[-1] + a * dt)
        s.append(s[-1] + v[-2] * dt)
    return s, v


ang_kin = odeint(ang_kinematics, [theta_0, omega_0], time)

theta_vec = ang_kin[:, 0]
omega_vec = ang_kin[:, 1]


def main(pplot=False):
    # answers
    a_ans = moment(force, radius)
    b_ans = moment(force, radius) / i
    [c_ans, d_ans] = from_accent(force / m, deg_to_rad(41))
    [e_ans, f_ans] = lin_kinematics(theta_vec)[1][0]
    g_ans = theta_vec[-1]
    [h_ans, i_ans] = lin_kinematics(theta_vec)[1][-1]
    j_ans = omega_vec[-1]

    # print
    print(f"""
    a) {a_ans}
    b) {b_ans}
    c) {c_ans}
    d) {d_ans}
    e) {e_ans}
    f) {f_ans}
    g) {g_ans}
    h) {h_ans}
    i) {i_ans}
    j) {j_ans}
    """)


# answers
if __name__ == "__main__":
    main()
