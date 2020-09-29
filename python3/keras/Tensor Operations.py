# Referenec Book: Deep Learning with Python 

import numpy as np 

# 2.3.1 Element-wise operations
x = np.array([[1, 2, 3],
              [0, -1, 3]])
y = np.array([[-1, 2, 0],
              [0, -1, 3]])

z = x + y
z = np.maximum(z, 0)
print(z)

# 2.3.2 Broadcasting
'''
When possible, and if there’s no ambiguity, the smaller tensor will be broadcasted to
match the shape of the larger tensor. Broadcasting consists of two steps:
    1. Axes (called broadcast axes) are added to the smaller tensor to match the ndim of
       the larger tensor.
    2. The smaller tensor is repeated alongside these new axes to match the full shape
       of the larger tensor.
'''
x = np.random.random((1,3,4,3))
y = np.random.random((4,3))
z = np.maximum(x, y)
print(z)
'''
[[[[0.61973766 0.66481166 0.81795199] 
   [0.86333686 0.14431782 0.4936027 ]
   [0.65448209 0.85841484 0.9671061 ]
   [0.92107294 0.92064691 0.96485797]]

  [[0.36866181 0.33668766 0.81795199]
   [0.86333686 0.10121043 0.65585511]
   [0.53269415 0.5442037  0.33534223]
   [0.42725368 0.35350347 0.96485797]]

  [[0.67249464 0.4645158  0.81795199]
   [0.86333686 0.30171043 0.73432242]
   [0.53269415 0.40951789 0.42569725]
   [0.4497047  0.63681454 0.96485797]]]]
'''

# 2.3.3 Tensor dot
x = np.array([[1, 2, 3],
              [0, -1, 3]])
y = np.array([[-1, 2, 0],
              [0, -1, 3]])

# z = np.dot(x, y)
# print(z)
# ValueError: shapes (2,3) and (2,3) not aligned: 3 (dim 1) != 2 (dim 0)

# 2.3.4 Tensor reshaping

y = y.reshape(3,2)
z = np.dot(x, y)
print(z)
'''
[[-4 11]
 [-3  9]]
'''
x = np.array([[0., 1.],
              [2., 3.],
              [4., 5.]])

print(x.shape)
x = x.reshape((6,1))
print(x)
'''
[[0.]
 [1.]
 [2.]
 [3.]
 [4.]
 [5.]]
'''
print(x.shape)  # (6, 1)

# 2.3.5 Geometric interpretation of tensor operations
'''
 In general, elementary geometric operations such as affine transformations, rotations,
 scaling, and so on can be expressed as tensor operations. For instance, a rotation of a
 2D vector by an angle theta can be achieved via a dot product with a 2 × 2 matrix
 R = [u, v] , where u and v are both vectors of the plane: u = [cos(theta),
 sin(theta)] and v = [-sin(theta), cos(theta)] .
'''

# 2.3.6 A geometric interpretation of deep learning
'''
 You just learned that neural networks consist entirely of chains of tensor operations and
 that all of these tensor operations are just geometric transformations of the input data.
 It follows that you can interpret a neural network as a very complex geometric transfor-
 mation in a high-dimensional space, implemented via a long series of simple steps.
    In 3D , the following mental image may prove useful. Imagine two sheets of colored
 paper: one red and one blue. Put one on top of the other. Now crumple them
 together into a small ball. That crumpled paper ball is your input data, and each sheet
 of paper is a class of data in a classification problem. What a neural network (or any
 other machine-learning model) is meant to do is figure out a transformation of the
 paper ball that would uncrumple it, so as to make the two classes cleanly separable
 again. With deep learning, this would be implemented as a series of simple transfor-
 mations of the 3D space, such as those you could apply on the paper ball with your fin-
 gers, one movement at a time.

    Uncrumpling paper balls is what machine learning is about: finding neat representa-
 tions for complex, highly folded data manifolds. At this point, you should have a
 pretty good intuition as to why deep learning excels at this: it takes the approach of
 incrementally decomposing a complicated geometric transformation into a long
 chain of elementary ones, which is pretty much the strategy a human would follow to
 uncrumple a paper ball. Each layer in a deep network applies a transformation that
 disentangles the data a little—and a deep stack of layers makes tractable an extremely
 complicated disentanglement process.
'''
