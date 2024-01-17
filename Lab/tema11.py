import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from scipy.optimize import minimize

#a
normal = np.load('sample_Normal.npy')
plt.figure(figsize=(8, 6))
plt.hist(normal, bins=30, density=True, color='blue', alpha=0.7)
plt.title('Histograma Datelor')
plt.xlabel('Valoarea Datelor')
plt.ylabel('Frecvența Normalizată')
plt.show()

#b
def log_likelihood(theta, data):

    mu, sigma = theta
    log_likelihood_values = np.sum(norm.logpdf(data, loc=mu, scale=sigma)) 
    return log_likelihood_values

theta1_range = np.linspace(-1, 1, 100)
theta2_range = np.linspace(0, 0.1, 100)
theta1, theta2 = np.meshgrid(theta1_range, theta2_range)
log_likelihood_values = np.zeros_like(theta1)

for i in range(theta1.shape[0]):
    for j in range(theta1.shape[1]):
        log_likelihood_values[i, j] = log_likelihood([theta1[i, j], theta2[i, j]], normal)

plt.figure(figsize=(8, 6))
plt.contourf(theta1, theta2, log_likelihood_values, levels=30, cmap='viridis')
plt.colorbar()
plt.title('Log-verosimilitate')
plt.xlabel('θ1')
plt.ylabel('θ2')
plt.show()

#c
initial_guess = [0, 0.05] 
result = minimize(lambda theta: -log_likelihood(theta, normal), initial_guess, bounds=[(-1, 1), (0, 0.1)])
estimated_theta = result.x

#d
plt.figure(figsize=(8, 6))
plt.contourf(theta1, theta2, log_likelihood_values, levels=30, cmap='viridis')
plt.colorbar()
plt.scatter(estimated_theta[0], estimated_theta[1], color='red', marker='x', label='Estimat')
plt.title('Log-verosimilitate cu Punctul Estimat')
plt.xlabel('θ1')
plt.ylabel('θ2')
plt.legend()
plt.show()

print(f'Estimarea θ: {estimated_theta}')
