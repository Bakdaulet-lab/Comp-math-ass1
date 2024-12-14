# Define the function g(x) for the iteration method
def g(x):
    return (x**2 + 5) / 6

# True roots of the equation for error comparison
true_roots = [1, 5]  # Factorized form is (x-1)(x-5)=0

# Iteration Method
def iteration_method(x0, true_root, max_iterations=10):
    iterations = []
    for i in range(max_iterations):
        x_next = g(x0)
        abs_error = abs(x_next - true_root)
        iterations.append((i + 1, x0, x_next, abs_error))
        x0 = x_next
    return iterations

# Parameters
initial_value = 0.5
true_root = 1  # Choose the root to compare with
max_iterations = 10

# Perform iterations
iteration_results = iteration_method(initial_value, true_root, max_iterations)

# Display results in a table
print("Iteration Table:")
print("Iter | Current Value | Next Value | Absolute Error")
for iter_num, current, next_val, abs_err in iteration_results:
    print(f"{iter_num:4} | {current:14.8f} | {next_val:12.8f} | {abs_err:14.8e}")

# Extract data for plotting
iteration_numbers = [result[0] for result in iteration_results]
absolute_errors = [result[3] for result in iteration_results]

# Plot the absolute error convergence
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
plt.plot(iteration_numbers, absolute_errors, marker='o')
plt.yscale('log')  # Logarithmic scale for clarity
plt.xlabel("Iteration Number")
plt.ylabel("Absolute Error (log scale)")
plt.title("Convergence of Iteration Method")
plt.grid()
plt.show()

