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

'''
Using TensorFlow backend.
WARNING:tensorflow:From /home/nahid/anaconda3/lib/python3.7/site-packages/tensorflow/python/framework/op_def_library.py:263: colocate_with (from tensorflow.python.framework.ops) is deprecated and will be removed in a future version.
Instructions for updating:
Colocations handled automatically by placer.
WARNING:tensorflow:From /home/nahid/anaconda3/lib/python3.7/site-packages/tensorflow/python/ops/math_ops.py:3066: to_int32 (from tensorflow.python.ops.math_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.cast instead.
Epoch 1/5
2019-04-23 02:47:28.100669: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX AVX2 FMA
2019-04-23 02:47:28.126491: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 2400000000 Hz
2019-04-23 02:47:28.126780: I tensorflow/compiler/xla/service/service.cc:150] XLA service 0x55dd7cb7df20 executing computations on platform Host. Devices:
2019-04-23 02:47:28.126805: I tensorflow/compiler/xla/service/service.cc:158]   StreamExecutor device (0): <undefined>, <undefined>
OMP: Info #212: KMP_AFFINITY: decoding x2APIC ids.
OMP: Info #210: KMP_AFFINITY: Affinity capable, using global cpuid leaf 11 info
OMP: Info #154: KMP_AFFINITY: Initial OS proc set respected: 0-3
OMP: Info #156: KMP_AFFINITY: 4 available OS procs
OMP: Info #157: KMP_AFFINITY: Uniform topology
OMP: Info #179: KMP_AFFINITY: 1 packages x 2 cores/pkg x 2 threads/core (2 total cores)
OMP: Info #214: KMP_AFFINITY: OS proc to physical thread map:
OMP: Info #171: KMP_AFFINITY: OS proc 0 maps to package 0 core 0 thread 0 
OMP: Info #171: KMP_AFFINITY: OS proc 2 maps to package 0 core 0 thread 1 
OMP: Info #171: KMP_AFFINITY: OS proc 1 maps to package 0 core 1 thread 0 
OMP: Info #171: KMP_AFFINITY: OS proc 3 maps to package 0 core 1 thread 1 
OMP: Info #250: KMP_AFFINITY: pid 18150 tid 18150 thread 0 bound to OS proc set 0
2019-04-23 02:47:28.127104: I tensorflow/core/common_runtime/process_util.cc:71] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.
OMP: Info #250: KMP_AFFINITY: pid 18150 tid 18175 thread 1 bound to OS proc set 1
OMP: Info #250: KMP_AFFINITY: pid 18150 tid 18192 thread 2 bound to OS proc set 2
OMP: Info #250: KMP_AFFINITY: pid 18150 tid 18193 thread 3 bound to OS proc set 3
OMP: Info #250: KMP_AFFINITY: pid 18150 tid 18194 thread 4 bound to OS proc set 0
OMP: Info #250: KMP_AFFINITY: pid 18150 tid 18174 thread 5 bound to OS proc set 1
OMP: Info #250: KMP_AFFINITY: pid 18150 tid 18195 thread 6 bound to OS proc set 2
60000/60000 [==============================] - 5s 79us/step - loss: 0.2607 - acc: 0.9237
Epoch 2/5
60000/60000 [==============================] - 5s 78us/step - loss: 0.1078 - acc: 0.9683
Epoch 3/5
60000/60000 [==============================] - 4s 72us/step - loss: 0.0716 - acc: 0.9782
Epoch 4/5
60000/60000 [==============================] - 4s 71us/step - loss: 0.0524 - acc: 0.9844
Epoch 5/5
60000/60000 [==============================] - 4s 71us/step - loss: 0.0398 - acc: 0.9879
'''

# Let's check that the model performs well on the test set, too
test_loss, test_acc = network.evaluate(test_images,test_labels)
print('test_acc: ', test_acc)  # test_acc:  0.9793
'''
 32/10000 [..............................] - ETA: 28sOMP: Info #250: KMP_AFFINITY: pid 18150 tid 18205 thread 7 bound to OS proc set 3
OMP: Info #250: KMP_AFFINITY: pid 18150 tid 18206 thread 8 bound to OS proc set 0
10000/10000 [==============================] - 1s 55us/step
test_acc:  0.9793
'''

network.save('my_model.h5')