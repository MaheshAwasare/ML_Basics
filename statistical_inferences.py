# -*- coding: utf-8 -*-
"""Statistical_inferences.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bTrcqqs9K2Ovv6K2CMPZI-WTEuzE_kc1
"""

import numpy as np
from scipy import stats

# Simulate heights of students in the population (assuming normal distribution)
np.random.seed(42)
population_heights = np.random.normal(loc=170, scale=5, size=1000)

# Take a random sample from the population
sample_heights = np.random.choice(population_heights, size=50, replace=False)

print(f"Sample Heights: {sample_heights}")

# Point Estimation: Estimate the population mean (parameter) using the sample mean (statistic)
sample_mean = np.mean(sample_heights)
print(f"Sample Mean: {sample_mean}")

# Interval Estimation: Calculate a 95% confidence interval for the population mean
confidence_interval = stats.t.interval(0.95, len(sample_heights)-1, loc=sample_mean, scale=stats.sem(sample_heights))
print(f"95% Confidence Interval: {confidence_interval}")

