# -*- coding: utf-8 -*-
"""MATH4143-A1-1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aKQgOwrBNBOyE0jd9p6iamjsRk4VSw7s

Nitesh Bansal

219106814

Assignment 1- MATH 4143
"""

#Black scholes model imported from the lecture notes
import numpy as np
from numpy import sqrt, log, exp
from scipy.special import ndtr

def BS_call(S,T,r,sigma,K):
    d1=(log(S/K)+(r+0.5*sigma**2)*T)/(sigma*sqrt(T))
    d2=d1-sigma*sqrt(T)
    C=ndtr(d1)*S-ndtr(d2)*K*exp(-r*T)
    return C

K = 100
r = 0.05
sigma = 0.25

#instance of bs as f
def f(s,t):
    return BS_call(s,t,r,sigma,K)

#defining time points and stock price points
time_points = np.arange(0.1, 1.1, 0.1)
stock_prices = np.arange(90, 111, 1)

#finite differences
delta_t = 0.01
delta_s = 1

#defininf an zero array of errors to match the lengths of time poitns and stockprices
relative_errors = np.zeros((len(time_points), len(stock_prices)))

#iteration to compute all the points
for i, t in enumerate(time_points):
    for j, s in enumerate(stock_prices):
        #computing ft, fs, and fss for each
        f_t = (f(s, t + delta_t) - f(s, t)) / delta_t
        f_s = (f(s + delta_s, t) - f(s, t)) / delta_s
        f_ss = (f(s + delta_s, t) - 2 * f(s, t) + f(s - delta_s, t)) / (delta_s ** 2)

        #left hand side
        lhs = f_t

        #right-hand side
        rhs = r * s * f_s + 0.5 * sigma ** 2 * s ** 2 * f_ss - r * f(s, t)

        # Calculate the relative error
        #accounting for zero rhs
        if rhs != 0:
            relative_errors[i, j] = np.abs(lhs / rhs - 1)
        else:
            relative_errors[i, j] = 0

#printing the matrix
print("Relative Error Matrix:")
print(relative_errors)

#printing the maximum error
print(f"Maximum relative error: {np.max(relative_errors)}")

