import numpy as np
from random import randint
from sklearn.preprocessing import MinMaxScaler

train_labels = []
train_samples = []

'''
Example Data:
    * An experimental drug was tested on individual from 13 to 100
    * The trail had 2100 participents. Half < 65 and Half > 65
    * 95% participents 65+ is experianced side effects
    * 95% participents < 65 is experianced no side effects
'''

for i in range(1000):
    random_younger = randint(13,64)
    train_samples.append(random_younger)
    train_labels.append(0) #0 for no side effects
    
    random_older = randint(65,100)
    train_samples.append(random_older)
    train_labels.append(1) #1 for side effects

for i in range(50):
    random_younger = randint(13,64)
    train_samples.append(random_younger)
    train_labels.append(1) #0 for no side effects
    
    random_older = randint(65,100)
    train_samples.append(random_older)
    train_labels.append(0) #1 for side effects
'''
#print raw data
#print train_samples data
for i in train_samples:
    print(i, end = ', ')
print()
#print train_labels data
for i in train_labels:
    print(i, end = ', ')
print()
'''
train_labels = np.array(train_labels)
train_samples = np.array(train_samples)

scaler = MinMaxScaler(feature_range=(0,1))
scaled_trains_samples = scaler.fit_transform((train_samples).reshape(-1,1))

for i in scaled_trains_samples:
    print(i, end=', ')