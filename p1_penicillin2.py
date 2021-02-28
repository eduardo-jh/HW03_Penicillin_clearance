#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BE523 Biosystems Analysis & Design
HW3 - Problem 1. Constructing a mathematical model for penicillin clearance
https://mathinsight.org/penicillin_clearance_model

Created on Sat Jan 23 21:29:34 2021
@author: eduardo
"""
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm  # allows linear regression without intercept

# The penicillin concentration that will be used to find the model
P = np.array([200, 152, 118, 93, 74])
steps = len(P)
dt = 5  # time interval
t = np.linspace(0, (steps-1)*dt, steps)  # actual time vector
dP = np.zeros(steps)

# Get the decrement of penicilin in every time interval
for i in range(0, steps-1):
    dP[i] = P[i+1] - P[i]

print('P=', P, '\ndP=', dP)

# Plot penicillin concentration change (dP) versus penicilline concentration (P)
# Perform a linear regression with P and dP, the slope of the line will give us
# the constant rate of penicillin clearance in every time step (approx. 20%)
# If the model is correct, the points should lie on a line that goes through
# the origin, no intercept is desired
model = sm.OLS(dP, P)  # No intercept by default
results = model.fit()
slope = results.params[0]
print("slope=", slope)

# # Figure 0, plotting P vs t, original data
# plt.figure(0)
# plt.title('Original data')
# plt.plot(t, P, 'kx')
# plt.legend(['data'], loc='best')
# plt.xlabel('t')
# plt.ylabel('P')

# Figure 1, plotting dP vs P
plt.figure(1)
plt.plot(P, dP, 'kx', P, slope*P, 'b-')
plt.legend(['data', 'linear regression $R^2$=%.2f' % results.rsquared], loc='best')
plt.xlabel('P')
plt.ylabel('dP')
# plt.savefig('p1_penicillin_linear2.png', dpi=300, bbox_inches='tight')  # Save figure 1

# Complete the model and make a prediction
# The model has the form B(t+1) = B[0]*(slope+1)^t
Pmodel = P[0]*(slope+1)**(t/dt)

# Figure 2, plotting P (from data and model) vs t
plt.figure(2)
plt.plot(t, P, 'kx', t, Pmodel, 'r-')
plt.legend(['data', 'model prediction'], loc='best')
plt.xlabel('t (min)')
plt.ylabel('Penicillin ($\mu$ g/ml)')
# plt.savefig('p1_penicillin_model2.png', dpi=300, bbox_inches='tight')  # Save figure 2