import numpy as np

# Sample Data
X = np.array([1, 2, 3, 4, 5])
Y = np.array([2, 4, 5, 4, 6])

# Step 1: Calculate Means
mean_X = np.mean(X)
mean_Y = np.mean(Y)

# Step 2: Calculate Covariance
covariance = np.sum((X - mean_X) * (Y - mean_Y)) / (len(X) - 1)

# Step 3: Calculate Standard Deviations
std_X = np.std(X, ddof=1)  # ddof=1 for sample standard deviation
std_Y = np.std(Y, ddof=1)

# Step 4: Calculate Pearson's Correlation
pearson_corr = covariance / (std_X * std_Y)

# Display Results
print(f"Mean of X: {mean_X:.2f}")
print(f"Mean of Y: {mean_Y:.2f}")
print(f"Covariance: {covariance:.2f}")
print(f"Standard Deviation of X: {std_X:.2f}")
print(f"Standard Deviation of Y: {std_Y:.2f}")
print(f"Pearson Correlation Coefficient: {pearson_corr:.2f}")
