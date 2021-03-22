"""
Alex Remstedt
19/03/2021

Week 6 opdracht 1 - [Mini-Hovercraft]
https://secure.ans-delft.nl/universities/1/courses/63457/assignments/225494/quiz/show/40967093
"""
# imports
import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt
from converter import deg_to_rad, to_accent

# vars
m = 500  # kg
i = 310  # kg m^2
r_fext = np.array([0, -.9])  # m --> r'
f_ext = np.array([1500, 0])  # N

# time
t0 = 0  # s
t1 = 44  # s
dt = 0.001  # s
time = np.linspace(t0, t1, round(1 + (t1 - t0) / dt))  # s

# initial values
theta0 = 0  # rad
omega0 = 0  # rad/s
x0 = 0  # m
v0 = 0  # m/s


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
    alpha = moment(to_accent(f_ext, theta), r_fext) / i
    return omega, alpha


# answers
ang_kin = odeint(ang_kinematics, [theta0, omega0], time)

theta_vec = ang_kin[:, 0]
omega_vec = ang_kin[:, 1]

# answers
if __name__ == "__main__":
    ans_a = moment(to_accent(f_ext, deg_to_rad(6)), r_fext)
    b = moment(to_accent(f_ext, deg_to_rad(24)), r_fext) / i
    [c, d] = f_ext / m
    [e, f] = f_ext / 2 / m * t1 ** 2
    g = theta_vec[-1]
    [h, i] = f_ext / m * t1
    j = omega_vec[-1]

    print(f"""
    a) {ans_a}
    b) {b}
    c) {c}
    d) {d}
    e) {e}
    f) {f}
    g) {g}
    h) {h}
    i) {i}
    j) {j}
    """)

    plt.plot(time, theta_vec)
    # plt.show()

