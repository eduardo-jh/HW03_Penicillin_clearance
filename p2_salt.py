#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BE523 Biosystems Analysis & Design
HW3 - Problem 2. Exercise 1 The salt problem
https://mathinsight.org/penicillin_clearance_model_exercises 

Created on Sat Jan 23 21:29:34 2021
@author: eduardo
"""
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm  # allows linear regression without intercept

S_0 = 2  # initial concentration of salt in mg/mL
r = -0.05  # rate of change in concentration (50 mL of 1000 mL)
steps = 20
dt = 1

t = np.linspace(0, (steps)*dt, steps+1)
dS = np.zeros(len(t))

# The model has the form S(t+1) = S[0]*(r+1)^t
S = S_0 * (r + 1)**t

# NOTE: this code generates values for S using the exponential solution form
# and then performs a linear regression from the same data!

# This time the for-loop is different because we are working with a decrement
for i in range(0, len(dS)-1):
    dS[i] = S[i+1] - S[i]  # compute the increment between time steps

# Perform a linear regression with B and dB, then plot (dB vs B)
model = sm.OLS(dS, S)  # No intercept by default, force through the origin
results = model.fit()
slope = results.params[0]  # grow rate of population
print("slope=", slope)

# Figure 1, plotting dB vs B
plt.figure(1)
plt.plot(S, dS, 'kx', S, slope*S, 'b-')
plt.legend(['data', 'linear regression $R^2$=%.2f' % results.rsquared], loc='best')
plt.xlabel('S')
plt.ylabel('dS')
plt.savefig('p_salt2_linear.png', dpi=300, bbox_inches='tight')

# Generate an exponential equation ('exact solution')
tdouble = np.log(2)/np.log(1+slope)*dt
print('tdouble =', tdouble)
K = np.log(2)/tdouble
Sexp = S[0] * np.exp(K*t)

# Make 'predictions' using the analytical solution to the linear dynamical system,
# (also an exponential equation) in the form B(t) = B[0]*R^t with R>1
# we don't need to know the previous value, each calculation is only dependant of the time 't'
Smodel = S[0]*pow(slope+1, t/dt)
print("At the end of %d steps the amount of salt is: %.3f" % (steps, Smodel[-1]))

# Figure 2, plotting S (from data and model) vs t
plt.figure(2)
plt.plot(t, S, 'bx', t, Smodel, 'r-', t, Sexp, 'k+')
plt.legend(['data',
            'numerical S=%g$\cdot$(%.4f+1)$^t$' % (S[0], slope),
            'exact S=%g$\cdot$exp(%.4f$\cdot$t)' % (S[0], K)],
            loc='best')
plt.xlabel('Time (minutes)')
plt.ylabel('Salt concentration')
plt.savefig('p2_salt2_%dsteps.png' % steps, dpi=300, bbox_inches='tight')
