# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 14:17:05 2017

@author: 大帆
"""

import numpy as np

def LU_solution(A,Y):
    W=np.zeros(A.shape)
    W=W.astype('float')
    for i in range(A.shape[0]):
        W[i]=A[i]/A[i].max()
    h=[]
    W=np.c_[W,np.arange(A.shape[0])]
    for i in range(W.shape[0]):
        id_max=np.argmax(W[i:,i])
        h.append(W[id_max+i,-1])
        t=W[i].copy()
        W[i]=W[id_max+i]
        W[id_max+i]=t
    del W
    h=[int(i) for i in h]
    A=A[h]
    Y=Y[h]
    def LU(A,Y):
        W=np.c_[A,Y]
        W=W.astype('float')
        L=np.zeros(A.shape)
        for i,_ in enumerate(range(A.shape[0])):
            L[i,i]=1
            for m in range(i+1,A.shape[0]):
                chu=W[m,i]/W[i,i]
                L[m,i]=chu
                W[m]=W[m]-W[i]*chu
        U=W[:,:-1]
        return L,U
    L,U=LU(A,Y)
    D=np.zeros(A.shape[0])
    for i in range(A.shape[0]):
        sum1=0
        for j in range(i):
            sum1+=D[j]*L[i,j]
        D[i]=(Y[i]-sum1)/L[i,i]
    X=np.zeros(A.shape[0])
    for i in range(A.shape[0])[::-1]:
        sum1=0
        for j in range(i+1,A.shape[0]):
            sum1+=X[j]*U[i,j]
        X[i]=(D[i]-sum1)/U[i,i]
    return X


A=[[2.0,100],
   [1,1]]
Y=[100,2]
A=np.array(A)
Y=np.array(Y).reshape([-1,1])
print("LU分解求解多元线性方程组:")
print(LU_solution(A,Y))


A=[[1,1,1],
   [2,1,3],
   [5,3,4]]
Y=[6,13,23]
A=np.array(A)
Y=np.array(Y).reshape([-1,1])
print("LU分解求解多元线性方程组:")
print(LU_solution(A,Y))