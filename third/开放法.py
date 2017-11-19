# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt


f=lambda x:x**2-2*x
xi=lambda x:np.sqrt(2*x)
xrange=np.arange(0,5.2,0.1)

plt.figure()
plt.plot(xrange,f(xrange))
plt.hlines(0,0,plt.xlim()[1])
def plot(x,color='g'):
    plt.hlines(f(x),0,x,color,'--')
    plt.vlines(x,0,f(x),color,'--')
    
def Fixed_point(xstart,func):
    while True:
        plot(xstart)
        xiii=func(xstart)
        if abs((xiii-xstart)/xstart)<0.00005:
            return xiii
        xstart=xiii

print(Fixed_point(5,xi))
plt.show()


fd=lambda x:2*x-2
plt.figure()
plt.plot(xrange,f(xrange))
plt.hlines(0,0,plt.xlim()[1])
def Newton(xstart,func):
    while True:
        plot(xstart)
        xiii=xstart-f(xstart)/fd(xstart)
        if abs((xiii-xstart)/xstart)<0.00005:
            return xiii
        xstart=xiii
    pass

print(Newton(5,f))
plt.plot()

def plot2(x1,x2,func):
    xl=(func(x2)-func(x1))/(x2-x1)
    x=x1-func(x1)/xl
    plt.plot([x,x2],[0,func(x2)],'r--')
plt.show()

plt.figure()
plt.plot(xrange,f(xrange),'k')
plt.hlines(0,0,plt.xlim()[1])
def Secant(xstart1,xstart2,func):
    while True:
        plot(xstart1,'b')
        plot(xstart2,'b')
        plot2(xstart2,xstart1,func)
        xiii=xstart1-func(xstart1)*\
                (xstart2-xstart1)/(func(xstart2)-func(xstart1))
        if abs((xiii-xstart1)/xstart1)<0.00005:
            return xiii
        xstart1=xstart2
        xstart2=xiii
    pass

print(Secant(5,3,f))
plt.plot()


