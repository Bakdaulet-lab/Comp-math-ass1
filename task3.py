import numpy as np
import matplotlib.pyplot as plt

# Define the function and its derivative
def f(x):
    return x**2 - 3*x + 2

def f_prime(x):
    return 2*x - 3

# Newton-Raphson Method
def newton_raphson(x0, tolerance=1e-6, max_iterations=100):
    iterations = []
    errors_absolute = []
    errors_relative = []
    
    x = x0
    for i in range(max_iterations):
        f_val = f(x)
        f_prime_val = f_prime(x)
        if f_prime_val == 0:
            print("Derivative is zero. Method fails.")
            break
        
        x_next = x - f_val / f_prime_val
        abs_error = abs(x_next - x)
        rel_error = abs_error / abs(x_next) if x_next != 0 else float('inf')
        
        # Store iteration data
        iterations.append((i + 1, x, abs_error, rel_error))
        errors_absolute.append(abs_error)
        
        # Check for convergence
        if abs_error < tolerance:
            break
        x = x_next
    
    return x, iterations, errors_absolute

# Parameters
initial_guess = 2.5
tolerance = 1e-6

# Run the Newton-Raphson method
root, iteration_data, absolute_errors = newton_raphson(initial_guess, tolerance)

# Display results in a table
print("Iteration Table:")
print("Iter | Current Guess | Absolute Error | Relative Error")
for iter_num, guess, abs_err, rel_err in iteration_data:
    print(f"{iter_num:4} | {guess:14.8f} | {abs_err:14.8e} | {rel_err:14.8e}")

# Plot convergence graph
plt.figure(figsize=(8, 5))
plt.plot(range(1, len(absolute_errors) + 1), absolute_errors, marker='o')
plt.yscale('log')  # Logarithmic scale for clarity
plt.xlabel("Iteration Number")
plt.ylabel("Absolute Error (log scale)")
plt.title("Convergence of Newton-Raphson Method")
plt.grid()
plt.show()

# Final result
print(f"The root found is approximately: {root:.8f}")
