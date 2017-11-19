import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

f=lambda x:-0.1*x**4-0.15*x**3-0.5*x**2-0.25*x+1.2

def fo_df(x,h):
    plt.plot([x-h,x],[f(x-h),f(x)],'r--',label='前')
    return (f(x)-f(x-h))/h

def back_df(x,h):
    plt.plot([x,x+h],[f(x),f(x+h)],'k--',label='后')
    return (f(x+h)-f(x))/h

def cen_df(x,h):
    a=(f(x-h)+f(x+h))/2
    plt.plot([x-h,x+h],[f(x-h)+f(x)-a,f(x+h)+f(x)-a],'g--',label='中')
    return (f(x+h)-f(x-h))/(2*h)


xx=np.linspace(-0.5,1.5,20)
yy=f(xx)
plt.plot(xx,yy)
print('前',fo_df(0.5,0.5))
print('后',back_df(0.5,0.5))
print('中',cen_df(0.5,0.5))
plt.legend(loc='best')
plt.show()

xx=np.linspace(-1,1,20)
yy=f(xx)
plt.plot(xx,yy)
print('前',fo_df(0.5,0.25))
print('后',back_df(0.5,0.25))
print('中',cen_df(0.5,0.25))
plt.legend(loc='best')
plt.show()