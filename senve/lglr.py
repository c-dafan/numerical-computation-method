# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 21:12:09 2017

@author: 大帆
"""

import numpy as np
import matplotlib.pyplot as plt


def lglr(X,y):
    """
    ### X格式要求
        传入的X为numpy.ndarray格式
    """
    aa=X.reshape([-1,1])-X
    fenmu=[]
    for i in range(aa.shape[1]):
        fenmu.append(aa[i][aa[i]!=0].prod())
    def result(x):
        """
        ### x格式要求
        x可以是int型，也可以为数组或者numpy.ndarray
        """
        if type(x)==int:
            x=[x]
        re=[]
        for xx in x:
            res=0
            for i in range(aa.shape[1]):
                ca=(xx-X)
                res+=np.r_[ca[:i],ca[i+1:]].prod()/fenmu[i]*y[i]
            re.append(res)
        return np.array(re)
    return result

    
X=np.arange(1,8)
y=np.log2(X)
lg=lglr(X,y)
x=np.arange(X.min(),X.max()+0.1,0.1)
yy=lg(x)
plt.scatter(X,y)
plt.plot(x,yy)
plt.show()


X=np.arange(1,12)
y=-(X-3)**2+20
lg=lglr(X,y)
x=np.arange(X.min(),X.max()+0.1,0.1)
yy=lg(x)
plt.scatter(X,y)
plt.plot(x,yy)
plt.show()

