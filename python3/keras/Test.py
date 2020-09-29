import numpy as np 
import pandas as pd
from keras.models import Sequential
from keras.utils import np_utils
from keras.layers.core import Dense, Activation, Dropout

train = pd.read_csv('/media/nahid/New Volume/GitHub/Keras/train.csv')
labels = train.ix[:, 0].values.astype('int32')  # ix is deprecated.(অসমর্থিত)
x_train = (train.ix[:,1:].values).astype('float32') # ix is deprecated.

# lab = train.iloc[:, 0].values.astype('int32')
# print(lab)

x_test = pd.read_csv('/media/nahid/New Volume/GitHub/Keras/test.csv')

# convert list of labels to binary class matrix
y_train = np_utils.to_categorical(labels)

print(labels.shape)  # (42000,)
print(y_train.shape)  # (42000, 10)

# pre-processing: divide by max and substract mean
scale = np.max(x_train)
x_train /= scale
x_test /= scale

# Compute the standard deviation along the specified axis.
mean = np.std(x_train)
x_train -= mean
x_test -= mean

# optional test
print('scale = ',scale,'mean = ',mean)

input_dim = x_train.shape[1]
nb_classes = y_train.shape[1]

# optional test
x, y = x_train.shape
print('x = ',x, 'y = ', y)  #x = 42000 y = 784
x, y = y_train.shape
print('x = ', x, 'y = ', y)  # x = 42000 y = 10

print(input_dim, ' ', nb_classes) # input_dim = 784, nb_classes = 10
print(x_train.shape, ' ', y_train.shape)  # (42000, 784)   (42000, 10)

# Here's a Deep Dumb MLP (DDMLP)
# Dropout consists in randomly setting a fraction rate of input units to 0 at each
# update during training time, which helps prevent overfitting.
# softmax and relu activation: http://sefiks.com/wp-content/uploads/2017/08/relu-and-softplus.png?w=600
# some other activation function: https://cdn-images-1.medium.com/max/1600/1*p_hyqAtyI8pbt2kEl6siOQ.png

model= Sequential()
model.add(Dense(128, input_dim=input_dim))
model.add(Activation('relu')) 
model.add(Dropout(0.15))
model.add(Dense(128))
model.add(Activation('relu'))
model.add(Dropout(0.15))
model.add(Dense(nb_classes))
model.add(Activation('softmax'))

