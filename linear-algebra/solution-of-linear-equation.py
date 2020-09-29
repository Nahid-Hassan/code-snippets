# import linear matrix equation solving method or function
from numpy.linalg import solve
from numpy import array
from numpy import allclose
from numpy import dot

"""
    Solve(a, b): Take two arguments a = Co-efficient matrix
                                    b = dependent variable values

    Return: Solution of the system ax = b, returned shape is 
            identical to b

    Raises: LinAlgError: if a is a singular or not square 

    ** Broadcasting rules apply.
    ** a must be square and of full-rank, i.e., all rows (or, equivalently, columns) must be           linearly independent; if either is not true, use lstsq for the least-squares best “solution”    of the system/equation.
"""

# Solve the system of equations 3 * x0 + x1 = 9 and x0 + 2 * x1 = 8
a = array([[3, 1], [1, 2]])
b = array([9, 8])

x = solve(a, b)

print(x)

# Check the solution is okay or not!!!!!
flag = allclose(dot(a, x), b)

if flag:
    print("Solution is correct.")
else:
    print("Solution is not correct.")



# Ref: https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.solve.html
