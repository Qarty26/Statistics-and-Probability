import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

data = np.load("sample_Gamma.npy")

# (a)
plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, density=True, alpha=0.7, color='red')
plt.title('Histograma datelor')
plt.show()

# (b) 
def gamma_log_likelihood(theta, data):
    alpha, beta = theta
    return -np.sum(np.log(np.random.gamma(alpha, 1/beta, len(data))))

initial_guess = [2, 1]
result = minimize(gamma_log_likelihood, initial_guess, args=(data,), method='L-BFGS-B')

theta_hat = result.x
print(f"Aproximare numerica pentru theta_hat: {theta_hat}")

# (c)
theta1_values = np.linspace(0, 10, 100)
theta2_values = np.linspace(0, 10, 100)

log_likelihood_values = np.zeros((len(theta1_values), len(theta2_values)))

for i, theta1 in enumerate(theta1_values):
    for j, theta2 in enumerate(theta2_values):
        log_likelihood_values[i, j] = -gamma_log_likelihood([theta1, theta2], data)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
theta1_mesh, theta2_mesh = np.meshgrid(theta1_values, theta2_values)

ax.plot_surface(theta1_mesh, theta2_mesh, log_likelihood_values.T, cmap='viridis')
ax.set_title('Graficul functiei log-verosimilitatii')
ax.set_xlabel('Theta1')
ax.set_ylabel('Theta2')
ax.set_zlabel('Log-verosimilitate')
plt.show()

# (d)
log_likelihood_hat = -result.fun

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(theta1_mesh, theta2_mesh, log_likelihood_values.T, cmap='viridis')
ax.scatter(theta_hat[0], theta_hat[1], log_likelihood_hat, marker='x', color='red', label=f'Theta_hat: {theta_hat}\nLog L(theta_hat): {log_likelihood_hat}')

ax.set_title('Graficul funcției log-verosimilității cu punctul theta_hat')
ax.set_xlabel('Theta1')
ax.set_ylabel('Theta2')
ax.set_zlabel('Log-verosimilitate')
ax.legend()
plt.show()