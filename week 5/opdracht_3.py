"""
Alex Remstedt
08/03/2021

Week 5 opdracht 3 - [Slinger 2: twee massa's]
https://secure.ans-delft.nl/universities/1/courses/63457/assignments/220711/quiz/show/39445239
"""
# imports
import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt

# variables
m = 1.6  # kg
r1 = .7  # m
r2 = r1 + 2  # m
g = 1.6  # m/s^2
theta_0 = -np.pi / 3  # rad
omega_0 = 0  # rad/s
dt = 0.001  # s
t0 = 0  # s
t1 = 7  # s
time = np.linspace(t0, t1, round(1 + (t1 - t0) / dt))


# functions

# angular functions
def kinematics(state, t):
    theta = state[0]
    omega = state[1]
    alpha = -g * theta * (r1 + r2) / (r1 ** 2 + r2 ** 2)
    return omega, alpha


res = odeint(kinematics, [theta_0, omega_0], time)

theta_vec = res[:, 0]
omega_vec = res[:, 1]

index = np.where(theta_vec > 0)[0]

# Answers
a_ans = m
b_ans = 2 * abs(time[index[0]] - time[index[-1]])
c_ans = 2 * abs(time[index[0]] - time[index[-1]])

plt.plot(time, theta_vec, 'r--')
plt.plot(time, omega_vec)
plt.show()

# answers
print(f"""
a) Wat is het traagheidsmoment: {a_ans}
b) De periode van de slinger: {b_ans}
c) {c_ans}
""")
