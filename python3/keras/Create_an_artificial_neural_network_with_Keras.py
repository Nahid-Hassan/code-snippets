import keras
from keras import backend as K
from keras.models import Sequential
from keras.layers import Activation
from keras.layers.core import Dense
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy

model = Sequential([
    Dense(16, input_shape=(1,6), activation='relu'),
    Dense(32, activation='relu'),
    Dense(2, activation='softmax')
])
print(model.summary())
'''
Output:
Instructions for updating:
Colocations handled automatically by placer.
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense_1 (Dense)              (None, 1, 16)             112       
_________________________________________________________________
dense_2 (Dense)              (None, 1, 32)             544       
_________________________________________________________________
dense_3 (Dense)              (None, 1, 2)              66        
=================================================================
Total params: 722
Trainable params: 722
Non-trainable params: 0
_________________________________________________________________
'''