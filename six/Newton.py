# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 21:27:55 2017

@author: 大帆
"""

import numpy as np
import matplotlib.pylab as plt

X=[1,2,3,4,5,7,8,9]
y=[np.log(x) for x in X]

def Newton(X,y):
    W=np.zeros([len(X),len(X)+1])
    W[:,0]=X
    W[:,1]=y
    for i in range(W.shape[1]-2):
        for j in range(i,W.shape[0]-1):
            W[j+1,i+2]=(W[j+1,i+1]-W[j,i+1])/(W[j+1,0]-W[j-i,0])
    
    def f(x):
        res=W[0,1]
        c=1
        for i in range(1,W.shape[0]):
            a=W[i,i+1]
            c*=(x-X[i-1])
#            for j in range(i):
#                a=(x-X[j])*a
#            res+=a
            res+=a*c
        return res
    return f
    
    
f=Newton(X,y)
plt.scatter(X,y)
x=np.arange(1,9,0.1)
plt.plot(x,f(x))
plt.show()


plt.figure()
X=[1,2,3,4,5,7,8,9]
y=[x**2 for x in X]
f=Newton(X,y)
plt.scatter(X,y)
x=np.arange(1,9,0.1)
plt.plot(x,f(x))