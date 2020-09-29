# Reference Book: Python Data Science Handbook (page:(51-58))
# Date(20 April, 2019) Time = 1:33 AM

import numpy as np

# big-O(N**2)


def selectionSort(x):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    return x

# big-O(N * N!)


def bogosort(x):
    while(np.any(x[:-1] > x[1:])):
        np.random.shuffle(x)
    return x


x = np.array([20, 10, 40, 30, 50])
selectionSort(x)
print(x)

y = np.array([20, 10, 40, 30, 50])
bogosort(y)
print(y)

# Fast Sorting in NumPy: np.sort and np.argsort
x = np.array([2, 1, 4, 3, 5])
print(np.sort(x))  # numpy sort
print(np.argsort(x)) # numpy arg sort

x.sort() #python builting sort
print(x[:])

#Sorting along rows or columns
rand = np.random.RandomState(42)
x = rand.randint(0,10,(4,6))
print(x)
'''
[[6 3 7 4 6 9]
 [2 6 7 4 3 7]
 [7 2 5 4 1 7]
 [5 1 4 0 9 5]]
'''
print(np.sort(x, axis=0)) #row based
'''
[[2 1 4 0 1 5]
 [5 2 5 4 3 7]
 [6 3 7 4 6 7]
 [7 6 7 4 9 9]]
'''
print(np.sort(x, axis=1)) #column based
'''
[[3 4 6 6 7 9]
 [2 3 4 6 7 7]
 [1 2 4 5 7 7]
 [0 1 4 5 5 9]]
'''
# Keep in mind that this treats each row or column as an independent array, and any
# relationships between the row or column values will be lost

#Partial Sorts: Partitioning
