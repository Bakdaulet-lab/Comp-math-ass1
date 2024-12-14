import numpy as np
from scipy.optimize import fsolve

# Define the function f(x)
def f(x):
    return np.exp(x) - 2*x - 3

# Bisection method implementation
def bisection_method(func, a, b, tol=1e-6, max_iter=100):
    if func(a) * func(b) >= 0:
        raise ValueError("The function must have opposite signs at a and b.")

    iteration = 0
    while (b - a) / 2 > tol and iteration < max_iter:
        c = (a + b) / 2
        if func(c) == 0:  # Exact root found
            break
        elif func(a) * func(c) < 0:
            b = c
        else:
            a = c
        iteration += 1

    return (a + b) / 2, iteration

# Secant method implementation
def secant_method(func, x0, x1, tol=1e-6, max_iter=100):
    iteration = 0
    while abs(x1 - x0) > tol and iteration < max_iter:
        f_x0, f_x1 = func(x0), func(x1)
        if f_x1 - f_x0 == 0:  # Avoid division by zero
            raise ValueError("Zero denominator encountered in Secant method.")

        x_temp = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        x0, x1 = x1, x_temp
        iteration += 1

    return x1, iteration

# True root for comparison
true_root = fsolve(f, 1)[0]

# Find root using Bisection method
root_bisection, iterations_bisection = bisection_method(f, 0, 2)
relative_error_bisection = abs((root_bisection - true_root) / true_root)

# Find root using Secant method
root_secant, iterations_secant = secant_method(f, 0, 2)
relative_error_secant = abs((root_secant - true_root) / true_root)

# Print results
print("Exact root (fsolve):", true_root)
print("\nBisection Method:")
print("Root:", root_bisection)
print("Iterations:", iterations_bisection)
print("Relative Error:", relative_error_bisection)

print("\nSecant Method:")
print("Root:", root_secant)
print("Iterations:", iterations_secant)
print("Relative Error:", relative_error_secant)

# Efficiency explanation
efficiency_explanation = """
The Secant method is generally more efficient than the Bisection method in terms of iterations
required to achieve the same level of accuracy. This is because the Secant method uses a more
sophisticated approach to approximate the root by leveraging the slope of the function,
whereas the Bisection method only narrows the interval containing the root. However, the
Secant method may fail if the denominator becomes zero, while the Bisection method is more
robust since it guarantees convergence as long as the initial interval contains the root.
"""
print(efficiency_explanation)
