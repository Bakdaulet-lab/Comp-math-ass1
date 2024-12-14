import cmath

# Define the function
def f(x):
    return x**3 + x**2 + x + 1

# Muller's Method
def muller_method(x0, x1, x2, tolerance=1e-6, max_iterations=100):
    for i in range(max_iterations):
        # Calculate function values
        f0, f1, f2 = f(x0), f(x1), f(x2)
        
        # Calculate coefficients of the quadratic interpolation
        h1, h2 = x1 - x0, x2 - x1
        delta1, delta2 = (f1 - f0) / h1, (f2 - f1) / h2
        a = (delta2 - delta1) / (h2 + h1)
        b = a * h2 + delta2
        c = f2
        
        # Calculate the discriminant
        discriminant = cmath.sqrt(b**2 - 4*a*c)
        
        # Choose the denominator to avoid cancellation
        if abs(b + discriminant) > abs(b - discriminant):
            denominator = b + discriminant
        else:
            denominator = b - discriminant
        
        # Calculate the next approximation
        dx = -2 * c / denominator
        x3 = x2 + dx
        
        # Check for convergence
        if abs(dx) < tolerance:
            return x3, i + 1
        
        # Update points
        x0, x1, x2 = x1, x2, x3
    
    raise ValueError("Muller's method did not converge")

# Initial approximations
x0, x1, x2 = -1, 0, 1
tolerance = 1e-6

# Find the root
root, iterations = muller_method(x0, x1, x2, tolerance)

# Verify the result
f_root = f(root)
absolute_error = abs(f_root)

# Display results
print(f"Root found: {root}")
print(f"f(root): {f_root}")
print(f"Absolute error: {absolute_error:.8e}")
print(f"Iterations: {iterations}")
