#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Define the objective function coefficients (maximize profit, so negate for linprog)
c = [-3, -4]

# Define the inequality constraint matrix (left-hand side coefficients)
A = [
    [2, 3],  # Machine time constraint
    [1, 2]   # Raw material constraint
]

# Define the inequality constraint vector (right-hand side values)
b = [12, 8]

# Bounds for the variables (non-negativity constraints)
x_bounds = (0, None)  # x1 >= 0
y_bounds = (0, None)  # x2 >= 0

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Plot the constraints
x = np.linspace(0, 7, 400)
y1 = (12 - 2 * x) / 3  # Machine time constraint
y2 = (8 - x) / 2       # Raw material constraint

# Feasible region boundaries
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label="2x + 3y ≤ 12")
plt.plot(x, y2, label="x + 2y ≤ 8")

# Shading the feasible region
plt.fill_between(x, np.minimum(y1, y2), 0, where=(y1 > 0) & (y2 > 0), color="lightgray", alpha=0.5)

# Identify corner points (intersections and axis-bound points)
points = [
    (0, 0),  # Origin
    (0, 4),  # Intersection with y-axis (x + 2y = 8)
    (6, 0),  # Intersection with x-axis (2x + 3y = 12)
    (3, 2)   # Intersection of the two lines
]

# Plot the corner points
for point in points:
    plt.plot(*point, 'ro')
    plt.text(point[0] + 0.2, point[1], f"({point[0]}, {point[1]})")

# Plot details
plt.xlim(0, 7)
plt.ylim(0, 5)
plt.axhline(0, color="black",linewidth=0.5)
plt.axvline(0, color="black",linewidth=0.5)
plt.title("Feasible Region and Constraints")
plt.xlabel("Product A (x)")
plt.ylabel("Product B (y)")
plt.legend()
plt.grid()

# Show the plot
plt.show()

# Print the optimal solution
optimal_solution = result.x
optimal_value = -result.fun  # Since we negated the profit for maximization
print("Optimal Solution (Product A, Product B):", optimal_solution)
print("Maximum Profit:", optimal_value)


# In[6]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Define the objective function coefficients (minimize cost)
c = [2, 5]  # Costs for products X and Y

# Define the inequality constraint matrix (left-hand side coefficients)
A = [
    [1, 2],  # Labor constraint
    [2, 1]   # Material constraint
]

# Define the inequality constraint vector (right-hand side values)
b = [6, 5]

# Bounds for the variables (non-negativity constraints)
x_bounds = (0, None)  # x1 >= 0
y_bounds = (0, None)  # x2 >= 0

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Plot the constraints
x = np.linspace(0, 7, 400)
y1 = (6 - x) / 2  # Labor constraint
y2 = (5 - 2 * x)  # Material constraint

# Feasible region boundaries
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label="x + 2y ≤ 6")
plt.plot(x, y2, label="2x + y ≤ 5")

# Shading the feasible region
plt.fill_between(x, np.minimum(y1, y2), 0, where=(y1 > 0) & (y2 > 0), color="lightgray", alpha=0.5)

# Identify corner points (intersections and axis-bound points)
points = [
    (0, 0),  # Origin
    (0, 2.5),  # Intersection with y-axis (x + 2y = 6)
    (2.5, 0),  # Intersection with x-axis (2x + y = 5)
    (1, 2)     # Intersection of the two lines
]

# Plot the corner points
for point in points:
    plt.plot(*point, 'ro')
    plt.text(point[0] + 0.2, point[1], f"({point[0]}, {point[1]})")

# Plot details
plt.xlim(0, 3)
plt.ylim(0, 3)
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.title("Feasible Region and Constraints")
plt.xlabel("Product X (x)")
plt.ylabel("Product Y (y)")
plt.legend()
plt.grid()

# Show the plot
plt.show()

# Print the optimal solution
optimal_solution = result.x
optimal_value = result.fun  # Direct since we are minimizing
print("Optimal Solution (Product X, Product Y):", optimal_solution)
print("Minimum Total Cost:", optimal_value)


# In[7]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Define the objective function coefficients (maximize profit, so negate for linprog)
c = [-5, -4]  # Profits for products A and B

# Define the inequality constraint matrix (left-hand side coefficients)
A = [
    [2, 1],  # Labor constraint
    [3, 2],  # Material constraint
    [1, 2]   # Machine time constraint
]

# Define the inequality constraint vector (right-hand side values)
b = [20, 30, 18]

# Bounds for the variables (non-negativity constraints)
x_bounds = (0, None)  # x1 >= 0 (Product A)
y_bounds = (0, None)  # x2 >= 0 (Product B)

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Plot the constraints
x = np.linspace(0, 15, 400)
y1 = (20 - 2 * x)  # Labor constraint
y2 = (30 - 3 * x) / 2  # Material constraint
y3 = (18 - x) / 2  # Machine time constraint

# Feasible region boundaries
plt.figure(figsize=(10, 7))
plt.plot(x, y1, label="2x + y ≤ 20")
plt.plot(x, y2, label="3x + 2y ≤ 30")
plt.plot(x, y3, label="x + 2y ≤ 18")

# Shading the feasible region
plt.fill_between(x, np.minimum(np.minimum(y1, y2), y3), 0, where=(y1 > 0) & (y2 > 0) & (y3 > 0), color="lightgray", alpha=0.5)

# Identify corner points (intersections and axis-bound points)
points = [
    (0, 0),  # Origin
    (0, 10),  # Intersection with y-axis (3x + 2y = 30)
    (9, 0),  # Intersection with x-axis (x + 2y = 18)
    (6, 4),  # Intersection of (3x + 2y = 30) and (x + 2y = 18)
    (5, 5)   # Intersection of (2x + y = 20) and (3x + 2y = 30)
]

# Plot the corner points
for point in points:
    plt.plot(*point, 'ro')
    plt.text(point[0] + 0.2, point[1], f"({point[0]}, {point[1]})")

# Plot details
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.title("Feasible Region and Constraints")
plt.xlabel("Product A (x)")
plt.ylabel("Product B (y)")
plt.legend()
plt.grid()

# Show the plot
plt.show()

# Print the optimal solution
optimal_solution = result.x
optimal_value = -result.fun  # Since we negated the profit for maximization
optimal_solution, optimal_value


# In[8]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Define the objective function coefficients (maximize revenue, so negate for linprog)
c = [-4, -5]  # Revenue for products A and B

# Define the inequality constraint matrix (left-hand side coefficients)
A = [
    [1, 2],  # Advertising budget constraint
    [1, 2]   # Production capacity constraint
]

# Define the inequality constraint vector (right-hand side values)
b = [20, 15]

# Bounds for the variables (non-negativity constraints)
x_bounds = (0, None)  # x1 >= 0 (Product A)
y_bounds = (0, None)  # x2 >= 0 (Product B)

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Plot the constraints
x = np.linspace(0, 15, 400)
y1 = (20 - x) / 2  # Advertising budget constraint
y2 = (15 - x) / 2  # Production capacity constraint

# Feasible region boundaries
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label="x + 2y ≤ 20")
plt.plot(x, y2, label="x + 2y ≤ 15")

# Shading the feasible region
plt.fill_between(x, np.minimum(y1, y2), 0, where=(y1 > 0) & (y2 > 0), color="lightgray", alpha=0.5)

# Identify corner points (intersections and axis-bound points)
points = [
    (0, 0),  # Origin
    (0, 10),  # Intersection with y-axis (x + 2y = 20)
    (15, 0),  # Intersection with x-axis (x + 2y = 15)
    (5, 7.5)  # Intersection of the two lines
]

# Plot the corner points
for point in points:
    plt.plot(*point, 'ro')
    plt.text(point[0] + 0.2, point[1], f"({point[0]}, {point[1]})")

# Plot details
plt.xlim(0, 15)
plt.ylim(0, 10)
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.title("Feasible Region and Constraints")
plt.xlabel("Product A (x)")
plt.ylabel("Product B (y)")
plt.legend()
plt.grid()

# Show the plot
plt.show()

# Print the optimal solution
optimal_solution = result.x
optimal_value = -result.fun  # Since we negated the revenue for maximization
optimal_solution, optimal_value


# In[9]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Define the objective function coefficients (maximize profit, so negate for linprog)
c = [-8, -7]  # Profit for projects P1 and P2

# Define the inequality constraint matrix (left-hand side coefficients)
A = [
    [3, 4],  # Labor constraint
    [2, 1]   # Capital constraint
]

# Define the inequality constraint vector (right-hand side values)
b = [12, 6]

# Bounds for the variables (non-negativity constraints)
x_bounds = (0, None)  # x1 >= 0 (Project P1)
y_bounds = (0, None)  # x2 >= 0 (Project P2)

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Plot the constraints
x = np.linspace(0, 10, 400)
y1 = (12 - 3 * x) / 4  # Labor constraint
y2 = (6 - 2 * x)  # Capital constraint

# Feasible region boundaries
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label="3x + 4y ≤ 12")
plt.plot(x, y2, label="2x + y ≤ 6")

# Shading the feasible region
plt.fill_between(x, np.minimum(y1, y2), 0, where=(y1 > 0) & (y2 > 0), color="lightgray", alpha=0.5)

# Identify corner points (intersections and axis-bound points)
points = [
    (0, 0),  # Origin
    (0, 6),  # Intersection with y-axis (2x + y = 6)
    (4, 0),  # Intersection with x-axis (3x + 4y = 12)
    (2, 2)   # Intersection of the two lines
]

# Plot the corner points
for point in points:
    plt.plot(*point, 'ro')
    plt.text(point[0] + 0.2, point[1], f"({point[0]}, {point[1]})")

# Plot details
plt.xlim(0, 5)
plt.ylim(0, 5)
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.title("Feasible Region and Constraints")
plt.xlabel("Project P1 (x)")
plt.ylabel("Project P2 (y)")
plt.legend()
plt.grid()

# Show the plot
plt.show()

# Print the optimal solution
optimal_solution = result.x
optimal_value = -result.fun  # Since we negated the profit for maximization
optimal_solution, optimal_value


# In[10]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Define the objective function coefficients (maximize profit, so negate for linprog)
c = [-5, -3]  # Profit for chocolate cakes and vanilla cakes

# Define the inequality constraint matrix (left-hand side coefficients)
A = [
    [1, 2],  # Baking time constraint
    [3, 2]   # Flour constraint
]

# Define the inequality constraint vector (right-hand side values)
b = [8, 12]

# Bounds for the variables (non-negativity constraints)
x_bounds = (0, None)  # x1 >= 0 (Chocolate cakes)
y_bounds = (0, None)  # x2 >= 0 (Vanilla cakes)

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Plot the constraints
x = np.linspace(0, 10, 400)
y1 = (8 - x) / 2  # Baking time constraint
y2 = (12 - 3 * x) / 2  # Flour constraint

# Feasible region boundaries
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label="x + 2y ≤ 8")
plt.plot(x, y2, label="3x + 2y ≤ 12")

# Shading the feasible region
plt.fill_between(x, np.minimum(y1, y2), 0, where=(y1 > 0) & (y2 > 0), color="lightgray", alpha=0.5)

# Identify corner points (intersections and axis-bound points)
points = [
    (0, 0),  # Origin
    (0, 6),  # Intersection with y-axis (3x + 2y = 12)
    (4, 0),  # Intersection with x-axis (x + 2y = 8)
    (2, 3)   # Intersection of the two lines
]

# Plot the corner points
for point in points:
    plt.plot(*point, 'ro')
    plt.text(point[0] + 0.2, point[1], f"({point[0]}, {point[1]})")

# Plot details
plt.xlim(0, 5)
plt.ylim(0, 6)
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.title("Feasible Region and Constraints")
plt.xlabel("Chocolate Cake (x)")
plt.ylabel("Vanilla Cake (y)")
plt.legend()
plt.grid()

# Show the plot
plt.show()

# Print the optimal solution
optimal_solution = result.x
optimal_value = -result.fun  # Since we negated the profit for maximization
optimal_solution, optimal_value


# In[11]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Define the objective function coefficients (minimize cost)
c = [6, 7]  # Costs for vehicles X and Y

# Define the inequality constraint matrix (left-hand side coefficients)
A = [
    [3, 4],  # Fuel constraint
    [2, 1]   # Driver time constraint
]

# Define the inequality constraint vector (right-hand side values)
b = [18, 10]

# Bounds for the variables (non-negativity constraints)
x_bounds = (0, None)  # x1 >= 0 (Vehicle X)
y_bounds = (0, None)  # x2 >= 0 (Vehicle Y)

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Plot the constraints
x = np.linspace(0, 10, 400)
y1 = (18 - 3 * x) / 4  # Fuel constraint
y2 = (10 - 2 * x)  # Driver time constraint

# Feasible region boundaries
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label="3x + 4y ≤ 18")
plt.plot(x, y2, label="2x + y ≤ 10")

# Shading the feasible region
plt.fill_between(x, np.minimum(y1, y2), 0, where=(y1 > 0) & (y2 > 0), color="lightgray", alpha=0.5)

# Identify corner points (intersections and axis-bound points)
points = [
    (0, 0),  # Origin
    (0, 4.5),  # Intersection with y-axis (2x + y = 10)
    (6, 0),  # Intersection with x-axis (3x + 4y = 18)
    (2, 3)   # Intersection of the two lines
]

# Plot the corner points
for point in points:
    plt.plot(*point, 'ro')
    plt.text(point[0] + 0.2, point[1], f"({point[0]}, {point[1]})")

# Plot details
plt.xlim(0, 7)
plt.ylim(0, 5)
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.title("Feasible Region and Constraints")
plt.xlabel("Vehicle X (x)")
plt.ylabel("Vehicle Y (y)")
plt.legend()
plt.grid()

# Show the plot
plt.show()

# Print the optimal solution
optimal_solution = result.x
optimal_value = result.fun  # Since we are minimizing the cost
optimal_solution, optimal_value


# In[12]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Define the objective function coefficients (maximize revenue, so negate for linprog)
c = [-10, -12]  # Revenue for products P1 and P2

# Define the inequality constraint matrix (left-hand side coefficients)
A = [
    [4, 3],  # Labor constraint
    [1, 2],  # Raw material constraint
    [3, 2]   # Machine time constraint
]

# Define the inequality constraint vector (right-hand side values)
b = [30, 18, 24]

# Bounds for the variables (non-negativity constraints)
x_bounds = (0, None)  # x1 >= 0 (Product P1)
y_bounds = (0, None)  # x2 >= 0 (Product P2)

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Plot the constraints
x = np.linspace(0, 10, 400)
y1 = (30 - 4 * x) / 3  # Labor constraint
y2 = (18 - x) / 2  # Raw material constraint
y3 = (24 - 3 * x) / 2  # Machine time constraint

# Feasible region boundaries
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label="4x + 3y ≤ 30")
plt.plot(x, y2, label="x + 2y ≤ 18")
plt.plot(x, y3, label="3x + 2y ≤ 24")

# Shading the feasible region
plt.fill_between(x, np.minimum(np.minimum(y1, y2), y3), 0, where=(y1 > 0) & (y2 > 0) & (y3 > 0), color="lightgray", alpha=0.5)

# Identify corner points (intersections and axis-bound points)
points = [
    (0, 0),  # Origin
    (0, 9),  # Intersection with y-axis (x + 2y = 18)
    (6, 0),  # Intersection with x-axis (3x + 2y = 24)
    (3, 6),  # Intersection of (4x + 3y = 30) and (x + 2y = 18)
    (4.5, 3)  # Intersection of (4x + 3y = 30) and (3x + 2y = 24)
]

# Plot the corner points
for point in points:
    plt.plot(*point, 'ro')
    plt.text(point[0] + 0.2, point[1], f"({point[0]}, {point[1]})")

# Plot details
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.title("Feasible Region and Constraints")
plt.xlabel("Product P1 (x)")
plt.ylabel("Product P2 (y)")
plt.legend()
plt.grid()

# Show the plot
plt.show()

# Print the optimal solution
optimal_solution = result.x
optimal_value = -result.fun  # Since we negated the profit for maximization
optimal_solution, optimal_value


# In[13]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Define the objective function coefficients (maximize reach, so negate for linprog)
c = [-500000, -400000]  # Reach for campaigns A and B

# Define the inequality constraint matrix (left-hand side coefficients)
A = [
    [4000, 3000],  # Television constraint
    [2000, 2500],  # Print media constraint
    [1000, 1500]   # Social media constraint
]

# Define the inequality constraint vector (right-hand side values)
b = [5000, 4500, 3000]

# Bounds for the variables (non-negativity constraints)
x_bounds = (0, None)  # x1 >= 0 (Campaign A)
y_bounds = (0, None)  # x2 >= 0 (Campaign B)

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Plot the constraints
x = np.linspace(0, 2, 400)
y1 = (5000 - 4000 * x) / 3000  # Television constraint
y2 = (4500 - 2000 * x) / 2500  # Print media constraint
y3 = (3000 - 1000 * x) / 1500  # Social media constraint

# Feasible region boundaries
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label="4000x + 3000y ≤ 5000")
plt.plot(x, y2, label="2000x + 2500y ≤ 4500")
plt.plot(x, y3, label="1000x + 1500y ≤ 3000")

# Shading the feasible region
plt.fill_between(x, np.minimum(np.minimum(y1, y2), y3), 0, where=(y1 > 0) & (y2 > 0) & (y3 > 0), color="lightgray", alpha=0.5)

# Identify corner points (intersections and axis-bound points)
points = [
    (0, 0),  # Origin
    (0, 1),  # Intersection with y-axis (2000x + 2500y = 4500)
    (1, 0),  # Intersection with x-axis (4000x + 3000y = 5000)
    (0.5, 1)  # Intersection of the two lines
]

# Plot the corner points
for point in points:
    plt.plot(*point, 'ro')
    plt.text(point[0] + 0.05, point[1], f"({point[0]}, {point[1]})")

# Plot details
plt.xlim(0, 1.5)
plt.ylim(0, 1.5)
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.title("Feasible Region and Constraints")
plt.xlabel("Campaign A (x)")
plt.ylabel("Campaign B (y)")
plt.legend()
plt.grid()

# Show the plot
plt.show()

# Print the optimal solution
optimal_solution = result.x
optimal_value = -result.fun  # Since we negated the reach for maximization
optimal_solution, optimal_value


# In[14]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Define the objective function coefficients (maximize revenue, so negate for linprog)
c = [-6, -5]  # Revenue for meals A and B

# Define the inequality constraint matrix (left-hand side coefficients)
A = [
    [2, 4],  # Meat constraint
    [3, 2],  # Vegetables constraint
    [1, 2]   # Rice constraint
]

# Define the inequality constraint vector (right-hand side values)
b = [30, 24, 20]

# Bounds for the variables (non-negativity constraints)
x_bounds = (0, None)  # x1 >= 0 (Meal A)
y_bounds = (0, None)  # x2 >= 0 (Meal B)

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Plot the constraints
x = np.linspace(0, 15, 400)
y1 = (30 - 2 * x) / 4  # Meat constraint
y2 = (24 - 3 * x) / 2  # Vegetables constraint
y3 = (20 - x) / 2  # Rice constraint

# Feasible region boundaries
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label="2x + 4y ≤ 30")
plt.plot(x, y2, label="3x + 2y ≤ 24")
plt.plot(x, y3, label="x + 2y ≤ 20")

# Shading the feasible region
plt.fill_between(x, np.minimum(np.minimum(y1, y2), y3), 0, where=(y1 > 0) & (y2 > 0) & (y3 > 0), color="lightgray", alpha=0.5)

# Identify corner points (intersections and axis-bound points)
points = [
    (0, 0),  # Origin
    (0, 7),  # Intersection with y-axis (3x + 2y = 24)
    (12, 0),  # Intersection with x-axis (2x + 4y = 30)
    (6, 6)   # Intersection of the three lines
]

# Plot the corner points
for point in points:
    plt.plot(*point, 'ro')
    plt.text(point[0] + 0.2, point[1], f"({point[0]}, {point[1]})")

# Plot details
plt.xlim(0, 15)
plt.ylim(0, 15)
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.title("Feasible Region and Constraints")
plt.xlabel("Meal A (x)")
plt.ylabel("Meal B (y)")
plt.legend()
plt.grid()

# Show the plot
plt.show()

# Print the optimal solution
optimal_solution = result.x
optimal_value = -result.fun  # Since we negated the revenue for maximization
optimal_solution, optimal_value


# In[ ]:




