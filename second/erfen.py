
import numpy as np
f=lambda x:2**x-4
f1=lambda x:np.log10(x)
f2=lambda x:x**0.5-1

def two_cen(head,end,fun):
    cen=(head+end)/2
    while True:
        if fun(cen)*fun(head)<0:
            end=cen
        elif fun(cen)*fun(head)>0:
            head=cen
        else:
            return cen
        least_cen=cen
        cen=(head+end)/2
        try:
            if abs((cen-least_cen)/cen)<0.00005:
                return cen
        except ZeroDivisionError as e:
            pass
    pass

print(two_cen(-5,5,f))

print(two_cen(0.5,5,f1))