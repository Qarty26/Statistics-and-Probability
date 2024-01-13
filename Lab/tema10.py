import numpy as np
import matplotlib.pyplot as plt
from pydataset import data

#a
dataset_name = 'airquality'
df = data(dataset_name)
print(f"Setul de date '{dataset_name}':")
print(df.head())

#b
covariance_matrix = np.cov(df.values, rowvar=False)
correlation_matrix = np.corrcoef(df.values, rowvar=False)
print("\nMatricea de covarianță:")
print(covariance_matrix)
print("\nMatricea de corelație:")
print(correlation_matrix)

#c
dependent_variable = 'Ozone'
independent_variable = 'Temp'
df = df.dropna(subset=[dependent_variable, independent_variable])
X = df[independent_variable].values
y = df[dependent_variable].values
X_mean = np.mean(X)
y_mean = np.mean(y)
slope = np.sum((X - X_mean) * (y - y_mean)) / np.sum((X - X_mean) ** 2)
intercept = y_mean - slope * X_mean
print(f"\nCoeficienții regresiei liniare pentru '{dependent_variable}' în funcție de '{independent_variable}':")
print(f"Slope (Coeficientul de înclinare): {slope}")
print(f"Intercept (Termenul liber): {intercept}")

#d
plt.scatter(X, y, label='Date reale')
plt.plot(X, slope * X + intercept, color='red', label='Dreapta de regresie')
plt.xlabel(independent_variable)
plt.ylabel(dependent_variable)
plt.title(f'Regresia liniară între {dependent_variable} și {independent_variable}')
plt.legend()
plt.show()

#e
num_samples = len(X)
train_size = int(0.8 * num_samples)
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

slope_train = np.sum((X_train - np.mean(X_train)) * (y_train - np.mean(y_train))) / np.sum((X_train - np.mean(X_train)) ** 2)
intercept_train = np.mean(y_train) - slope_train * np.mean(X_train)
print(f"\nCoeficienții regresiei liniare pentru setul de date de antrenament:")
print(f"Slope (Coeficientul de înclinare): {slope_train}")
print(f"Intercept (Termenul liber): {intercept_train}")

y_pred_test = slope_train * X_test + intercept_train
comparison_data = list(zip(y_test, y_pred_test))
comparison_df = list(map(lambda x: {'Actual': x[0], 'Predicted': x[1]}, comparison_data))
print("\nComparare valorilor exacte cu predicția dată de regresia liniară:")
print(comparison_df)

mse = np.mean((y_test - y_pred_test) ** 2)
print(f"\nEroarea medie patratică (MSE): {mse}")