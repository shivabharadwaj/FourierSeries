from scipy import integrate
import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos


def p(x):
    if -np.pi <= x < 0:
        return 0
    if 0 <= x <= np.pi:
        return 1


def fourier(f, n):
    a = []
    b = []
    time = np.linspace(-np.pi, np.pi, 100)
    a0 = (integrate.quad(f, -np.pi, np.pi)[0])/(2*np.pi)
    for i in range(n + 1):
        fc = lambda x: f(x) * cos((i+1) * x)
        fs = lambda x: f(x) * sin((i+1) * x)
        a.append((1 / np.pi) * integrate.quad(fc, -np.pi, np.pi)[0])
        b.append((1 / np.pi) * integrate.quad(fs, -np.pi, np.pi)[0])
    func = [np.array([a[k]*np.cos((k+1)*x) + b[k]*np.sin((k+1)*x) for k in range(0, len(a))]).sum() + a0 for x in time]
    plt.plot(time, func)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Fourier Approximation")
    plt.show()
    levels = []
    plt.plot([0, 0], [0, (2**.5 * a0)**2])
    for i in range(0, n+1):
        levels.append(a[i]**2 + b[i]**2)
        plt.plot([i+1, i+1], [0, levels[i]])
    plt.xlabel("k")
    plt.ylabel("A k^2")
    plt.title("Energy Spectrum Plot")
    plt.show()

g = lambda x: x**2
fourier(p, 5)