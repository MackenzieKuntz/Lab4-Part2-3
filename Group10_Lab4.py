# Lab 4
import numpy as np
from matplotlib import pyplot as plt
import scipy.integrate as scint


# Part 2 - Mackenzie Kuntz
# Undamped and undriven pendulum problem for initial swing angles theta = 10,40, and 70 degrees
# Use equation for a simple pendulum
g = 9.81
l = 9.81

def deriv_theta(time, theta):
    return (theta[1], (-g/l)*np.sin(theta[0]))

# Initial values
theta10 = [10*np.pi/180,0]
theta40 = [40*np.pi/180,0]
theta70 = [70*np.pi/180,0]

def amp_min_max(t,theta):
    return theta[0]

# Solve
time = np.linspace(0,10,100)
soln10 = scint.solve_ivp(deriv_theta, (0,100), theta10, t_eval=time, events= amp_min_max)
soln40 = scint.solve_ivp(deriv_theta, (0,100), theta40, t_eval=time, events= amp_min_max)
soln70 = scint.solve_ivp(deriv_theta, (0,100), theta70, t_eval=time, events= amp_min_max)

# Plot
fig = plt.figure()
ax = fig.add_subplot()
t70 = ax.plot(soln70.t, soln70.y[1], label = 'Initial \u03B8 = 70\u00B0')
t40 = ax.plot(soln40.t, soln40.y[1], label = "Initial \u03B8 = 40\u00B0")
t10 = ax.plot(soln10.t,soln10.y[1], label = "Initial \u03B8 = 10\u00B0")
ax.set_xlabel("Time (t)")
ax.set_ylabel("Swing Amplitude (\u03B8)")
plt.title("Swing Amplitude by Initial Conditions")
plt.legend(loc = 'upper right')



# Part 3 - Mackenzie Kuntz
# Determine period
interval_10 = soln10.t_events[0]
period_10 = 2*(interval_10[1:] - interval_10[0:-1])
avg_period_10 = period_10.mean()
std_period_10 = period_10.std()
print(avg_period_10)
interval_40 = soln40.t_events[0]
period_40 = 2*(interval_40[1:] - interval_40[0:-1])
avg_period_40 = period_40.mean()
std_period_40 = period_40.std()
print(avg_period_40)
interval_70 = soln70.t_events[0]
period_70 = 2*(interval_70[1:] - interval_70[0:-1])
avg_period_70 = period_70.mean()
std_period_70 = period_70.std()
print(avg_period_70)
fig2 = plt.figure()
ax2 = fig2.add_subplot()

# Create an array for x and y values to compare exact and average periods
exact_period10 = exact_period(9.81,10)
exact_period40 = exact_period(9.81,40)
exact_period70 = exact_period(9.81,70)
exact_period = [exact_period10,exact_period40, exact_period70]
avg_period = [avg_period_10,avg_period_40,avg_period_70]

period = plt.scatter(exact_period, avg_period)
ax2.set_xlabel("T(exact)")
ax2.set_ylabel("T(average)")
plt.title("Period Estimate Compared to Exact Period")
plt.errorbar(exact_period , avg_period, yerr = [std_period_10,std_period_40,std_period_70])
plt.show()


