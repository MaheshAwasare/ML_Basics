# -*- coding: utf-8 -*-
"""Copy of Principal Component Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1chXrZUVyDyLmk_nOgbozMUvIxlsRyzTY
"""

import numpy as np

# Original data
data = np.array([
    [1, 2, 3],
    [2, 4, 6],
    [3, 6, 9],
    [4, 8, 12]
])

# Center the data
mean = np.mean(data, axis=0)
centered_data = data - mean

# Calculate the covariance matrix
covariance_matrix = np.cov(centered_data.T)

# Calculate the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
print("eigenvectors:")
print(eigenvectors)
print("eigenvalues:")
print(eigenvalues)
# Sort the eigenvalues and eigenvectors in descending order
sorted_indices = np.argsort(eigenvalues)[::-1]
sorted_eigenvalues = eigenvalues[sorted_indices]
sorted_eigenvectors = eigenvectors[:, sorted_indices]
print("sorted_eigenvectors:")
print(sorted_eigenvectors)
print("sorted_eigenvalues:")
print(sorted_eigenvalues)
# Select the first principal component
first_principal_component = sorted_eigenvectors[:, 0]

# Project the data onto the first principal component
projected_data = centered_data.dot(first_principal_component)

# Dimensionality reduced data
dimensionality_reduced_data = projected_data.reshape(-1, 1)

print("Dimensionality reduced data:")
print(dimensionality_reduced_data)