# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 15:00:11 2017

@author: 大帆
"""

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']   
plt.rcParams['font.family']='sans-serif' 
plt.rcParams['axes.unicode_minus'] = False


def cubic_spline_interpolation(x,y):
    N=len(x)
    X=np.zeros([4*(N-1)-2,4*(N-1)])
    Y=np.zeros([4*(N-1)-2,1])
    j=0
    for i in range(N-2):
    #    print(y[i+1])
    #    print(x[i+1])
        Y[2*i]=y[i+1]
        Y[i*2+1]=y[i+1]
        for _ in range(2):
            X[2*i+_,4*j]=x[i+1]**3
            X[2*i+_,4*j+1]=x[i+1]**2
            X[2*i+_,4*j+2]=x[i+1]
            X[2*i+_,4*j+3]=1
            if _ ==0:
                j=(j+1)%(N-1)
        pass
    
    j=2*(N-1)-2
    X[j,0]=x[0]**3
    X[j,1]=x[0]**2
    X[j,2]=x[0]
    X[j,3]=1
    Y[j]=y[0]
    
    X[j+1,-4]=x[-1]**3
    X[j+1,-3]=x[-1]**2
    X[j+1,-2]=x[-1]
    X[j+1,-1]=1
    Y[j+1]=y[-1]
    
    h=2*(N-1)
    j=0
    
    for i in range(N-2):
        X[i+h,4*j+0]=x[i+1]**2*3
        X[i+h,4*j+1]= x[i+1]*2
        X[i+h,4*j+2]= 1
        X[i+h,4*j+3]= 0
        X[i+h,4*j+4]=-x[i+1]**2*3
        X[i+h,4*j+5]= -x[i+1]*2
        X[i+h,4*j+6]= -1
        j+=1
    
    j=0
    h=2*(N-1)+N-2
    for i in range(N-2):
        X[i+h,4*j+0]=6*x[i+1]
        X[i+h,4*j+1]=2
        X[i+h,4*j+4]=-6*x[i+1]
        X[i+h,4*j+5]=-2
        j+=1
        
    
    X=np.mat(np.c_[X[:,1:-4],X[:,-3:]])
    
    Y=np.mat(Y)
    a0=0
    w=X.I*Y
    an=0
    def pre(xx):
        for i in range(N-1):
            if x[i]<=xx and xx-x[i+1]<=0.001:
                if i==0:
                    return a0*xx**3+w[0]*xx**2+w[1]*xx+w[2]
                elif i==N-2:
                    return an*xx**3+w[-3]*xx**2+w[-2]*xx+w[-1]
                else:
                    return w[i*4-1]*xx**3+w[i*4]*xx**2+w[i*4+1]*xx+w[i*4+2]
        
                break
            else:
                pass
    def res(x):
        if type(x)==int:
            return pre(x)
        else:
            x=np.array(x)
            return np.apply_along_axis(pre,1,x.reshape([-1,1]))
    return res

x=np.array([3,4.5,7,9])
y=np.array([2.5,1,2.5,0.5])
f=plt.figure()
one=plt.plot(x,y)
xx=np.arange(3,9.1,0.2)
#调用三次样条函数
yy=cubic_spline_interpolation(x,y)(xx)
three=plt.plot(xx,yy)
plt.legend(one+three,['线性样条','三次样条'])
plt.show()


x=np.arange(10)-5
y=1/(1+np.exp(-x))
xx=np.arange(x.min(),x.max()+0.1,0.2)
#调用三次样条函数
yy=cubic_spline_interpolation(x,y)(xx)
f=plt.figure()
one=plt.plot(x,y)
three=plt.plot(xx,yy)
plt.legend([one[0],three[0]],['线性样条','三次样条'])
plt.show()