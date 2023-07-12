import numpy as np

#new exponential definition
def my_exp(x,u):
  #u: umbral
    if  x < u and x >= -u:
      return np.exp(x)
    elif x < -u:
      return np.exp(-u)
    else:
      return np.exp(u)

#new logarithm definition
def my_ln(x,u):
  #u: umbral
    if x < u:
      return np.log(u)
    else:
      return np.log(x)
