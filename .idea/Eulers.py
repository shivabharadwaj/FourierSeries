import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt
from math import sin, cos

def f1(s,i):
    return -.6*s*i+.1*(1-s-i)

def f2(s,i):
    return 0.6*s*i-.34*i


def eulers_method(f1,f2,t0,y0,y1,tEnd,n):
    delta = (tEnd-t0) /n
    arr = np.zeros((n+1, 2))
    arr1 = np.zeros((n+1,2))
    arr[0][0]=t0
    arr[0][1]=y0
    arr1[0][0]=t0
    arr1[0][1]=y1
    for i in range (1,len(arr)):
        arr[i][0]=arr[i-1][0]+delta
        arr1[i][0]=arr1[i-1][0]+delta
        arr[i][1] = arr[i - 1][1] + delta * f1(arr[i - 1][1],arr1[i - 1][1])
        arr1[i][1] = arr1[i - 1][1] + delta * f2(arr[i - 1][1], arr1[i - 1][1])
    print(arr)
    print(arr1)
    t=[]
    y=[]
    t1=[]
    y1=[]
    for i in range (len(arr)):
       t.append(arr[i][0])
       y.append(arr[i][1])
       t1.append(arr1[i][0])
       y1.append(arr1[i][1])
    plt.plot(y,y1)
    plt.show()
    plt.plot(t,y)
    plt.plot(t,y1)
    plt.show()
    print()
    print("The approximate output value is: ", arr[n][1])

print(eulers_method(f1,f2,0,.9,.1,100,1000))

