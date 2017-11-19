# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 15:00:11 2017

@author: 大帆
"""

import numpy as np
import matplotlib.pyplot as plt

N=4
x=np.array([3,4.5,7,9])

#y=1/(1+np.exp(-x))
y=np.array([2.5,1,2.5,0.5])

f=plt.figure()
plt.plot(x,y)
plt.show()


X=np.zeros([3*(N-1)-1,3*(N-1)])
Y=np.zeros([3*(N-1)-1,1])

j=0
for i in range(N-2):
#    print(y[i+1])
#    print(x[i+1])
    Y[2*i]=y[i+1]
    Y[i*2+1]=y[i+1]
    for _ in range(2):
        X[2*i+_,3*j]=x[i+1]**2
        X[2*i+_,3*j+1]=x[i+1]
        X[2*i+_,3*j+2]=1
        if _ ==0:
            j=(j+1)%(N-1)
    pass

j=2*(N-1)-2
X[j,0]=x[0]**2
X[j,1]=x[0]
X[j,2]=1
Y[j]=y[0]

X[j+1,-3]=x[-1]**2
X[j+1,-2]=x[-1]
X[j+1,-1]=1
Y[j+1]=y[-1]

h=2*(N-1)
j=0

for i in range(N-2):
    X[i+h,3*j+0]=x[i+1]*2
    X[i+h,3*j+1]=1
    X[i+h,3*j+2]=0
    X[i+h,3*j+3]=-x[i+1]*2
    X[i+h,3*j+4]=-1
    j+=1

X=np.mat(X[:,1:])
Y=np.mat(Y)

a0=0
w=X.I*Y

def pre(xx):
    for i in range(N-1):
        if x[i]<=xx and xx<=x[i+1]:
            if i==0:
                return a0*xx**2+w[0]*xx+w[1]
    
            else:
                return w[i*3-1]*xx**2+w[i*3]*xx+w[i*3+1]
    
            break
        else:
            pass
        
xx=np.arange(3,9,0.2)
yy=np.apply_along_axis(pre,1,xx)