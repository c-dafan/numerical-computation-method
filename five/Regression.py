# -*- coding: utf-8 -*-


import numpy as np
from sklearn.base import RegressorMixin
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']   
plt.rcParams['font.family']='sans-serif' 
plt.rcParams['axes.unicode_minus'] = False

'''Regression支持线性回归与多项式回归及多变量回归，degree为多项式的次数，
调用fit方法，计算得到各变量的系数
调用predict方法，计算结果
调用score方法，计算r方分数
'''
class Regression(RegressorMixin):
    def __init__(self,degree=1):#degree为多项式的次数
        self.degree=degree
        pass
    def fit(self,X,y):
        if type(X)!=np.ndarray:
            X=np.array(X)
        if type(y)!=np.ndarray:
            y=np.array(y)
        if len(X.shape)==1:
            X=X.reshape([-1,1])
        self.pol=PolynomialFeatures(degree=self.degree)
        X=self.pol.fit_transform(X)
        self.W=self.CreateWmat(X,y)
    def CreateWmat(self,X,y):
        mat=[]
        for i in range(X.shape[1]):
            row=[]
            for j in range(X.shape[1]):
                row.append((X[:,i]*X[:,j]).sum())
            mat.append(row)
        mat=np.mat(mat)
        y_list=[]
        for i in range(X.shape[1]):
            y_list.append((X[:,i]*y).sum())
        y_list=np.mat(y_list).reshape([-1,1])
        return mat.I*y_list
    def predict(self,X):
        if type(X)!=np.ndarray:
            X=np.array(X)
        if len(X.shape)==1:
            X=X.reshape([-1,1])
        X=self.pol.transform(X)
        X=np.mat(X)
        return X*self.W

def plot(X,y,regression):
    true,=plt.plot(X,y,c='b')
    y_pre=regression.predict(np.arange(min(X),max(X),0.1))
    predict,=plt.plot(np.arange(min(X),max(X),0.1),y_pre,c='r')
    plt.legend([true,predict],["原始数据","预测结果"])
    plt.show()

X=[0,0.2,0.4,0.6,0.8]
y=[0.9,1.9,2.8,3.3,4.2]
regression=Regression(1)
regression.fit(X,y)
y_pre=regression.predict(X)
print('result:',y_pre)
print('r2_score:',regression.score(X,y))
plot(X,y,regression)
  
#二次
  
X=[0,1,2,3,4,5]
y=[2.1,7.7,13.6,27.2,40.9,61.1]
regression=Regression(2)
regression.fit(X,y)
y_pre=regression.predict(X)
print('result:',y_pre)
print('r2_score:',regression.score(X,y))
plot(X,y,regression)


X=[1,2,3,4,6,7,8]
y=[2,3,6,7,5,3,2]
regression=Regression(2)
regression.fit(X,y)
y_pre=regression.predict(X)
print('result:',y_pre)
print('r2_score:',regression.score(X,y))
plot(X,y,regression)