

f=lambda x:2**x-4
f1=lambda x:x+1
f2=lambda x:x**0.5-1

def try_place(x0,x1,fun):
    xr=x1-fun(x1)*(x0-x1)/(fun(x0)-fun(x1))
    while True:
        if fun(xr)==0:
            return xr
        x0=xr
        least_xr=xr
        xr=x1-fun(x1)*(x0-x1)/(fun(x0)-fun(x1))
        try:
            if abs((xr-least_xr)/xr)<0.00005:
                return xr
        except ZeroDivisionError as e:
            pass
    pass

print(try_place(-1.5,1,f))

print(try_place(-5,5,f1))