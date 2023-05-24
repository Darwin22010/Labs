import cmath
import copy
import math

import matplotlib.pyplot as plt
import numpy as np


def n(j,xc,x):
    n = 1
    for i in range(j):
        n *= (xc-x[i])

    return n
 
def newton(x,y,xx):
    n = len(x)
    a = y.copy()
    for j in range(1,n):
        for i in range(n-1,j-1,-1):
            a[i] = (a[i]-a[i-1])/(x[i]-x[i-j])
    p = a[n-1]
    for k in range(1,n):
        p = a[n-k-1] + (xx - x[n-k-1])*p
    return p

   
def main():
		
    print("task a)")
    x = [0,  math.pi/6, math.pi*2/6, math.pi*3/6]
    y = [math.cos(k) for k in x]
    xnew = np.linspace(min(x),max(x),100)
    ynew = [newton(x,y,i) for i in xnew]
    plt.plot(x,y,'o',xnew,ynew)
    plt.grid(True)
    plt.show()
    print("error:")
    print(abs(newton(x,y,math.pi/4) - math.cos(math.pi/4)))
    
    print("task b)")
    x = [0,  math.pi/6, math.pi*5/12, math.pi/2]
    y = [math.cos(k) for k in x]
    
    xnew = np.linspace(min(x),max(x),100)
    ynew = [newton(x,y,i) for i in xnew]
    plt.plot(x,y,'o',xnew,ynew)
    plt.grid(True)
    plt.show()
    print("error:")
    print(abs(newton(x,y,math.pi/4) - math.cos(math.pi/4)))


if __name__ == '__main__':
		main()