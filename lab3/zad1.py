import numpy as np
import math
from matplotlib import pyplot as plt


def f(x):
    return 1 / (1 + x**2)

def newton(s,k):
    l = np.prod([s - i for i in range(k)])
    m = math.factorial(k)
    return l / m

class interpolation_newton:
    def __init__(self, points_x, func):
        self.points = points_x
        self.func = func
        self.n = len(points_x)
        self.delta_process()
    def delta_process(self):
        self.delta = [[0 for _ in range(self.n)] for _ in range(self.n)]
        for i in range(self.n):
            self.delta[0][i] = self.func(self.points[i])
        for i in range(1, self.n):
            for j in range(self.n - 1):
                self.delta[i][j] = self.delta[i - 1][j + 1] - self.delta[i-1][j]
    def polynomial(self, x):
        result = 0
        h = self.points[1] - self.points[0]
        s = (x - self.points[0]) / h
        for k in range(self.n):
            result += newton(s, k) * self.delta[k][0]
        return result
    def plot(self, axs):
        x = np.linspace(-5, 5, 10000)
        y = [f(i) for i in x]
        yp = [self.polynomial(i) for i in x]

        axs[0].plot(x,y,'b')
        axs[0].plot(x, yp, 'y')
        x = np.linspace(a,b,30)
        err = [abs(self.func(i) - self.polynomial(i)) for i in x]
        axs[1].plot(x, err, 'r')
a, b = -5, 5
N = 15
points = np.linspace(a,b, N+1)

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)
Pn_a = interpolation(points, f)

Pn_a.plot((ax1, ax3))

base = [np.cos(np.pi*(2*k - 1)/(2*(N + 1))) for k in range(1, N +2)]
points_b = [0.5*(a + b) + 0.5*(b - a)*point for point in base]
points_b.reverse()
Pn_b = interpolation(points_b, f)

Pn_b.plot((ax2,ax4))

plt.show()






        
