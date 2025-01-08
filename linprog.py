from scipy.optimize import linprog

# Coefficients for the objective function (maximize profit)
c = [-40, -30]  # Negative for maximization

# Coefficients for the inequality constraints
A = [
    [3, 2],  # 3x1 + 2x2 <= 100 (Labor)
    [1, 2]   # x1 + 2x2 <= 80 (Material)
]

b = [100, 80]  # RHS of constraints

# Bounds for decision variables (x1, x2 must be non-negative)
x_bounds = [(0, None), (0, None)]

# Solve the linear program
result = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method='highs')

# Print results
if result.success:
    print("Optimal solution found!")
    print(f"x1 (Product A): {result.x[0]:.2f} units")
    print(f"x2 (Product B): {result.x[1]:.2f} units")
    print(f"Total profit: £{-result.fun:.2f}")
else:
    print("No feasible solution found.")
