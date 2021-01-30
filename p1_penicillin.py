#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BE523 Biosystems Analysis & Design
HW3 - Problem 1. Constructing a mathematical model for penicillin clearance

Created on Sat Jan 23 21:29:34 2021
@author: eduardo
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# The penicillin concentration that will be used to find the model
P = np.array([200, 152, 118, 93, 74])
steps = len(P)
dt = 5  # time interval
t = np.linspace(0, (steps-1)*dt, steps)  # actual time vector
dP = np.zeros(steps)

# Get the decrement of penicilin in every time interval
for i in range(0, steps-1):
    dP[i] = P[i+1] - P[i]
    
# Plot penicillin concentration change (dP) versus penicilline concentration (Pplot)
# If the model is correct, the points should lie on a line that goes
# through the origin, so add the point (0,0) to the array
Pplot = P[:]
Pplot = np.append(Pplot, 0)
dP = np.append(dP, 0)

# Perform a linear regression with the data, the slope of the line will give us
# the constant rate of penicillin clearance in every time step (approx. 20%)
slope, intercept, r_value, p_value, std_err = stats.linregress(Pplot, dP)
print('P=', P, '\nPplot=', Pplot, '\ndP=', dP)
print("slope=", slope, "intercept=", intercept)

# # Figure 0, plotting P vs t, original data
# plt.figure(0)
# plt.title('Original data')
# plt.plot(t, P, 'kx')
# plt.legend(['data'], loc='best')
# plt.xlabel('t')
# plt.ylabel('P')

# Figure 1, plotting dP vs P
plt.figure(1)
plt.plot(Pplot, dP, 'kx', Pplot, slope*Pplot + intercept, 'b-')
plt.legend(['data', 'linear regression ($R^2$=%.2f)' % r_value**2], loc='best')
plt.xlabel('P')
plt.ylabel('dP')
# plt.savefig('p1_penicillin_linear.png', dpi=300)  # Save figure 1

# Complete the model and make a prediction
# The model has the form B(t+1) = B[0]*(slope+1)^t
Pmodel = P[0]*(slope+1)**(t/dt)

# Figure 2, plotting P (from data and model) vs t
plt.figure(2)
plt.plot(t, P, 'kx', t, Pmodel, 'r-')
plt.legend(['data', 'model prediction'], loc='best')
plt.xlabel('t (min)')
plt.ylabel('Penicillin ($\mu$ g/ml)')
# plt.savefig('p1_penicillin_model.png', dpi=300)  # Save figure 2