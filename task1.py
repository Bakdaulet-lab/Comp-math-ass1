# Assignment 1 - Computational Mathematics
# Week 1 & 2
# Task 1: Graphical method and absolute error

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Define the function f(x)
def f(x):
    return x**3 - 2*x**2 - 5

# Define the range for x
x_range = np.linspace(1, 4, 500)

# Plot the function
plt.figure(figsize=(8, 6))
plt.plot(x_range, f(x_range), label="f(x) = x^3 - 2x^2 - 5", color="blue")
plt.axhline(0, color="black", linewidth=0.8, linestyle="--", label="y=0")
plt.title("Graph of f(x) = x^3 - 2x^2 - 5")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.legend()
plt.show()

# Approximate root from the graph (e.g., visually estimated near x = 2.5)
approx_root = 2.5

# Calculate f(x) at the approximate root
f_approx = f(approx_root)

# Find the true root using a numerical method (fsolve)
true_root = fsolve(f, approx_root)[0]

# Calculate the absolute error
absolute_error = abs(true_root - approx_root)

# Print results
print("Approximate root from the graph: x =", approx_root)
print("Value of f(x) at approximate root: f(approx_root) =", f_approx)
print("True root (numerical method): x =", true_root)
print("Absolute error: |true_root - approx_root| =", absolute_error)

# Explanation of graphical method's accuracy
explanation = """
The graphical method is only approximate because it relies on visual estimation,
which can be influenced by the resolution of the graph and the observer's accuracy.
While it gives a quick way to estimate the root, it does not provide the precision
of numerical methods like fsolve, which iteratively converge to the exact solution.
"""
print(explanation)
