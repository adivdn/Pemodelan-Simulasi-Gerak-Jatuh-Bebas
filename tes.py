# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 21:45:47 2020

@author: ADIV
"""

import matplotlib.pyplot as plt
import numpy
import math

arrayOftime1 = []
arrayOftime2 = []
arrayOfAnalitik = []
arrayOfNumerik = []


high = float(input('Masukkan Ketinggian : '))
timedelta = float(input('Masukkan TimeDelta : '))

g = 9.8
time = float(math.sqrt(2*high/g))

g = g * -1
height = high

speedNumerik = 0
heightNumerik = high
for x in numpy.arange(0, time+timedelta, timedelta):

    speedNumerik = speedNumerik + (g * timedelta)
    heightNumerik = heightNumerik + (speedNumerik * timedelta)
    arrayOfNumerik.append(heightNumerik)
    arrayOftime1.append(x)
    if heightNumerik < 0:
        print(x)
        
    
for t in numpy.arange(0,time+timedelta,timedelta):
    
    height = high + (0.5 * g * t * t)
    arrayOftime2.append(t)
    arrayOfAnalitik.append(height)
    

print(time)
plt.xlabel('Time')
plt.ylabel('Height')
plt.plot(arrayOftime1, arrayOfAnalitik, 'r-o')
plt.plot(arrayOftime2, arrayOfNumerik,'b')
plt.legend(['Analitik','Numerik'], loc = 'upper right')
plt.ylim(0,high)
plt.show()

1301183484