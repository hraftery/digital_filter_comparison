# To run using Cygwin:
# # python3.8
# >>> from filter_comparisons import *
# >>> plt.plot(x)
# >>> plt.show()

import random
import matplotlib.pyplot as plt
import math

class LowPassSinglePole:
    def __init__(self, decay):
        self.b = 1 - decay
        self.reset()
    def reset(self):
        self.y = 0
    def filter(self, x):
        self.y += self.b * (x - self.y)
        return self.y

class SlidingAverage:
    def __init__(self, windowSize):
        self.windowSize = windowSize
        self.buffer = []
        self.bufferSize = 0
    def filter(self, x):
        if len(self.buffer) == self.windowSize:
            self.buffer.pop(0) 
        
        self.buffer.append(x)
        return sum(self.buffer)/len(self.buffer)

filters = []
for i in range(1,10):
	filters.append(LowPassSinglePole(i/10))
filters.append(SlidingAverage(10))

LEN = 10000

#x = [0.0]
#for i in range(LEN):
#    x.append(x[i] + 2*random.random() - 1)

t = [ti/1000 for ti in range(10000)] # 10 seconds in ms increments
c = 500/10 # chirpyness is 500Hz in 10 seconds
x = [math.cos(2*math.pi*(ti*ti*c/2)) for ti in t] 

y = []
for f in range(10):
    y.append([])
    for i in range(LEN):
        y[f].append(filters[f].filter(x[i]))

#plt.plot(x)
#plt.plot(y[9])
#plt.show()