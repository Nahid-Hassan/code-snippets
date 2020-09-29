'''
    Vector length formula for three-dimensional vector
    --------------------------------------------------
    In the case of the spatial problem the length of the vector a = {ax ; ay ; az} 
    can be found using the   following formula:

    |a| = √ax2 + ay2 + az2

    Examples of plane tasks
    Example 1. Find the length of the vector a = {2; 4}.
    Solution: |a| = √2^2 + 4^2 = √4 + 16 = √20 = 2√5.

    Example 2. Find the length of the vector a = {3; -4}.
    Solution: |a| = √3^2 + (-4)^2 = √9 + 16 = √25 = 5.

    Examples of spatial tasks
    Example 3. Find the length of the vector a = {2; 4; 4}.
    Solution: |a| = √2^2 + 4^2 + 4^2 = √4 + 16 + 16 = √36 = 6.

    Example 4. Find the length of the vector a = {-1; 0; -3}.
    Solution: |a| = √(-1)^2 + 0^2 + (-3)^2 = √1 + 0 + 9 = √10.
'''

import numpy as np

a = np.array([2,4,4]) # 3 dimension

total = 0

for i in range(len(a)):
    total += a[i] ** 2

print(np.sqrt(total))
# or
print(np.linalg.norm(a))

a = np.array([-1, 0, -3, -4, 10])

total = 0

for i in range(len(a)):
    total += a[i] ** 2

print(np.sqrt(total))
#or
print(np.linalg.norm(a))