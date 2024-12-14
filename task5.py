import matplotlib.pyplot as plt

# Define the function
def f(x):
    return x**2 - 2

# False Position Method
def false_position(a, b, tolerance=1e-6, max_iterations=100):
    if f(a) * f(b) >= 0:
        raise ValueError("The function must have opposite signs at a and b.")
    
    iterations = []
    errors_absolute = []
    errors_relative = []
    root = None
    
    for i in range(max_iterations):
        # Compute the root using the false position formula
        root = (a * f(b) - b * f(a)) / (f(b) - f(a))
        
        # Calculate errors
        abs_error = abs(f(root))
        rel_error = abs_error / abs(root) if root != 0 else float('inf')
        
        # Store iteration data
        iterations.append((i + 1, root, abs_error, rel_error))
        errors_absolute.append(abs_error)
        
        # Check for convergence
        if abs_error < tolerance:
            break
        
        # Update interval
        if f(a) * f(root) < 0:
            b = root
        else:
            a = root
    
    return root, iterations, errors_absolute

# Define interval and parameters
a, b = 1, 2
tolerance = 1e-6

# Run the False Position method
root, iteration_data, absolute_errors = false_position(a, b, tolerance)

# Display results in a table
print("Iteration Table:")
print("Iter | Root Approximation | Absolute Error | Relative Error")
for iter_num, approx_root, abs_err, rel_err in iteration_data:
    print(f"{iter_num:4} | {approx_root:18.8f} | {abs_err:14.8e} | {rel_err:14.8e}")

# Plot the convergence graph
plt.figure(figsize=(8, 5))
plt.plot(range(1, len(absolute_errors) + 1), absolute_errors, marker='o')
plt.yscale('log')  # Logarithmic scale for clarity
plt.xlabel("Iteration Number")
plt.ylabel("Absolute Error (log scale)")
plt.title("Convergence of False Position Method")
plt.grid()
plt.show()

# Final result
print(f"The root found is approximately: {root:.8f}")
