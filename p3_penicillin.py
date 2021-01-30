#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BE523 Biosystems Analysis & Design
HW3 - Problem 3. Exercise 2 Penicillin in intestine and plasma
https://mathinsight.org/penicillin_clearance_model_exercises 

Created on Sat Jan 23 21:29:34 2021
@author: eduardo
"""
import numpy as np
import matplotlib.pyplot as plt

dt = 5  # time interval, minutes
steps = 21
t = np.linspace(0, 100, steps)  # intervals of time

# Initialize the arrays
intestine = np.zeros(steps)  # amount of penicillin in intestine
plasma = np.zeros(steps)  # amount of penicillin in plasma
intestine[0] = 500  # initial amoung of penicillin, in mg

# Compute the amount of penicillin in each time step
for i in range(1, steps):
    intestine[i] = intestine[i-1] - intestine[i-1]*0.1
    plasma[i] = plasma[i-1] + intestine[i-1]*0.1 - plasma[i-1]*0.15

# Create a figure
plt.figure(1)
plt.plot(t*dt, intestine, 'b-', t*dt, plasma, 'r--')
plt.legend(['intestine', 'plasma'], loc='best')
plt.xlabel('Time (min)')
plt.ylabel('Penicillin (mg)')
plt.savefig('p3_intestine.png', dpi=300, bbox_inches='tight')