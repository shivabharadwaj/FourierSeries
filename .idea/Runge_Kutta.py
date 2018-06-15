import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt
from math import sin, cos

def f1(t):
    return 3*cos(3*t)



def runge_Kutta(f1,t0,y0,tEnd,n):
    delta = (tEnd-t0) /n
    arr = np.zeros((n+1, 2))
    arr[0][0]=t0
    arr[0][1]=y0
    for i in range (1,len(arr)):
        arr[i][0]=arr[i-1][0]+delta
        k1=f(arr[i-1][1])
        k2=f(arr[i-1][1]+.5*delta)
        k3=f(arr[i-1][1]+.5*delta)
        k4=f(arr[i-1]+delta)
        arr[i][1] = arr[i - 1][1] + delta * ((k1+k2+k3+k4)/6)
    print(arr)
    t=[]
    y=[]
    for i in range (len(arr)):
       t.append(arr[i][0])
       y.append(arr[i][1])
    plt.plot(t,y)
    plt.show()
    print("The approximate output value is: ", arr[n][1])

print(eulers_method(f1,0,1,100,100))

