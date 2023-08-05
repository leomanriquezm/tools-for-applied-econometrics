import numpy as np
from scipy.optimize import minimize

# Simulated data
np.random.seed(12345)
n = 1000
k = 2
X = np.hstack((np.ones((n, 1)), np.random.randn(n, k)))
true_coeffs = np.random.normal(1, 1, k)
y = X.dot(true_coeffs) + np.random.randn(n)

# Likelihood function
def ols_likelihood(params, data):
    beta = params
    X = data['X']
    y = data['y']
    
    predicted = X.dot(beta)
    residuals = y - predicted
    
    log_likelihood = np.sum(np.log(np.exp(-0.5 * ((residuals - 0) / 1)**2) / np.sqrt(2 * np.pi)))
    return -log_likelihood

# Initial point
initial_params = np.ones(X.shape[1])
# Data for likelihood function
data = {'X': X, 'y': y}

# Solving
result = minimize(ols_likelihood, initial_params, args=(data,), method='BFGS')
print(result.x)
