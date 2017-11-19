# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 11:50:13 2017

@author: 大帆
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x+1)*(x-4)*(x-5)*(x+3)*(x-2)
    
def f1(x):
    return x**5-7*x**4-3*x**3+79*x**2-46*x-120

a=[1,-7,-3,79,-46,-120]
aa=[1,-3.5,2.75,2.125,-3.875,1.25]

def Beers(a,r=-1,s=-1):
    for g in range(50):
        b=[]
        for i,v in enumerate(a):
            if i==0:
                b.append(v)
            elif i==1:
                b.append(v+r*b[-1])
            else:
                b.append(v+r*b[-1]+s*b[-2])
        
        b0=b[-1]
        b1=b[-2]
        c=[]
        for i,v in enumerate(b):
            if i==0:
                c.append(v)
            elif i==1:
                c.append(v+r*c[-1])
            else:
                c.append(v+r*c[-1]+s*c[-2])
        
        c1=c[-2]
        c2=c[-3]
        c3=c[-4]
        rs=np.matrix([[c2,c3],[c1,c2]]).I*\
                     np.matrix([[-b1],[-b0]])
        dr=rs[0]
        ds=rs[1]
        if (abs(dr/r)<0.01)and(abs(ds/s)<0.01):
            break
        r=r+dr
        s=s+ds
        r=r.min()
        s=s.min()
    return((r+(r**2+4*s)**0.5)/2,\
            (r-(r**2+4*s)**0.5)/2)
        

x1,x2=Beers(a,2,15)
print(x1,x2)

plt.figure()
x_range=np.arange(-3.1,5.3,0.1)
plt.plot(x_range,f1(x_range),'r',alpha=0.5)
plt.hlines(0,plt.xlim()[0],plt.xlim()[1])
plt.scatter([x1,x2],[0,0])
plt.show()

plt.figure()
x1,x2=Beers(a,-4.1,-3.2)
print(x1,x2)
x_range=np.arange(-3.1,5.3,0.1)
plt.plot(x_range,f1(x_range),'r',alpha=0.5)
plt.hlines(0,plt.xlim()[0],plt.xlim()[1])
plt.scatter([x1,x2],[0,0])
plt.show()

plt.figure()
x1,x2=Beers(a,6.1,-8.2)
print(x1,x2)
x_range=np.arange(-3.1,5.3,0.1)
plt.plot(x_range,f1(x_range),'r',alpha=0.5)
plt.hlines(0,plt.xlim()[0],plt.xlim()[1])
plt.scatter([x1,x2],[0,0])
plt.show()

plt.figure()
x1,x2=Beers(a,3,4)
print(x1,x2)
x_range=np.arange(-3.1,5.3,0.1)
plt.plot(x_range,f1(x_range),'r',alpha=0.5)
plt.hlines(0,plt.xlim()[0],plt.xlim()[1])
plt.scatter([x1,x2],[0,0])
plt.show()

plt.figure()
x1,x2=Beers(a,1,2)
print(x1,x2)
x_range=np.arange(-3.1,5.3,0.1)
plt.plot(x_range,f1(x_range),'r',alpha=0.5)
plt.hlines(0,plt.xlim()[0],plt.xlim()[1])
plt.scatter([x1,x2],[0,0])
plt.show()