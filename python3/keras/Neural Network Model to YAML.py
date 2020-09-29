# The MNIST dataset comes preloaded in Keras, in the form of a set of four Numpy arrays.

# from keras.datasets import mnist(National Institude of Standerds and Technology)
from keras.datasets import mnist
from keras import models
from keras import layers 
from keras.utils import to_categorical
import os
import tensorflow as tf
from tensorflow import keras

# load mnist data using load_data() method
# train_images and train_labels form the training set, the data that the model will
# learn from. The model will then be tested on the test set, test_images and test_labels .
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

#--------------------------------------------------------------------------------------
# To know about MNIST data set(How does look mnist train_images, train Lables)
# https://github.com/Nahid-Hassan/Keras/blob/master/mnist%20dataset%20observation.py
#---------------------------------------------------------------------------------------

# To build network
network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
network.add(layers.Dense(10, activation='softmax'))

# To compilation step
network.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])
#Prepairing the image data(training data)
train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

# We also need to categorically encode the labels
# Prepairing the labels
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# Now we are ready to train the network, which in keras is done via call to the network 'fit' method
network.fit(train_images, train_labels, epochs=5, batch_size=128)

# Let's check that the model performs well on the test set, too
test_loss, test_acc = network.evaluate(test_images,test_labels)
print('test_acc: ', test_acc)  # test_acc:  0.9793

# serialize network to YAML
network_yaml = network.to_yaml()
with open('network.yaml','w') as yaml_file:
    yaml_file.write(network_yaml)

# Serialize weights to HDF5
network.save_weights('model.h5')
print('save network to disk')