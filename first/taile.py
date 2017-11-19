from sympy import *
import matplotlib.pyplot as plt
import numpy as np

x=Symbol('x')

f=-0.1*x**4-0.15*x**3-0.5*x**2-0.25*x+1.2

def ff(x):
    return -0.1*x**4-0.15*x**3-0.5*x**2-0.25*x+1.2

a=np.linspace(-5,5,100)


c=input('please input 在哪里泰勒展开:')

t=f.series(x,int(c),5)

d=input('please input x:')
h=t.subs(x,int(d))
print(h)
g=ff(np.linspace(-5,5,100))
plt.plot(a,g)
plt.xlim((-5,5))
plt.ylim((g.min(),g.max()+(g.max()-g.min())*0.1))
plt.scatter(float(d),h)

# plt.text(float(d),h,'')
plt.vlines(int(d),plt.ylim()[0],h,linestyle="--",colors='r')
plt.plot([plt.xlim()[0],int(d)],[h,h],'r--')
plt.show()

