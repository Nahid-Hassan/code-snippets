import numpy as np

"""
# Equation
	3x - 2y = 7
	2x - 2y = 2
--------------
We know, Ax = b, where A => co-efficient matrix
											 b => constant-vector
											 x => unknowns
"""
A = np.array([[3, -2], [2, -2]])
b = np.array([7, 2])

solution_vector = np.linalg.solve(A, b)
print(solution_vector)

