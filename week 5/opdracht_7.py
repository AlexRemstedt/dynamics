"""
Alex Remstedt
13/03/2021

Week 5 opdracht 7 - [Slinger 5: vierkante plaat met gat]
https://secure.ans-delft.nl/universities/1/courses/63457/assignments/220711/quiz/show/39445243
"""
# imports
import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt

# variables
g = 1.6  # m/s^2
r = 1.7
theta_0 = -np.pi / 3  # rad
omega_0 = 0  # rad/s
dt = 0.001  # s
t0 = 0  # s
t1 = 7  # s
time = np.linspace(t0, t1, round(1 + (t1 - t0) / dt))

# structural properties of square
b = 3.4 / np.sqrt(2)  # m
r_circle = 0.6  # m
m_tot = 1.6  # kg

v_square = b ** 2
v_hole = np.pi * r_circle ** 2
rho = m_tot / (v_square - v_hole)

m_hole = rho * v_hole
m_square = rho * v_square

i_o = m_square * b ** 2 / 12 * 2 - m_hole * r_circle ** 2 / 2
i = i_o + m_tot * r ** 2


# functions
# angular functions
def kinematics(state, t):
    theta = state[0]
    omega = state[1]
    alpha = -g * np.sin(theta) * r * m_tot / i
    return omega, alpha


def lin_kinematics(state, t):
    theta = state[0]
    omega = state[1]
    alpha = -g * theta * r * m_tot / i
    return omega, alpha


res = odeint(kinematics, [theta_0, omega_0], time)
lin_res = odeint(lin_kinematics, [theta_0, omega_0], time)

theta_vec = res[:, 0]
omega_vec = res[:, 1]

l_theta_vec = lin_res[:, 0]
l_omega_vec = lin_res[:, 1]

index = np.where(theta_vec > 0)[0]
lin_index = np.where(l_theta_vec > 0)[0]


# Answers
a_ans = i_o
b_ans = 2 * abs(time[index[0]] - time[index[-1]])
c_ans = 2 * abs(time[lin_index[0]] - time[lin_index[-1]])

plt.plot(time, theta_vec, 'r--')
plt.plot(time, omega_vec)
plt.grid()
plt.savefig('week 5/img/opdracht_4.png')

# answers
print(f"""
a) Wat is het traagheidsmoment: {a_ans} kg m^2
b) De periode van de slinger: {b_ans} s
c) De gelineariseerde periode van de slinger: {c_ans} s
""")