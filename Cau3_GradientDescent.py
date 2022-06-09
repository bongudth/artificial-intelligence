from math import *

def grad(x):
    # return (4*exp(-x) - 8*exp(-2*x))
    # return (-2*exp(-2*x) + 24*exp(-3*x) - 64*exp(-4*x))
    return (2*exp(2*x) + 8*exp(-x) - 64*exp(-4*x))

def f(x):
    # return (1 - 2/(exp(x)))**2
    # return (exp(-x) - 4/(exp(2*x)))**2
    return (exp(x) - 4/(exp(2*x)))**2

def GradientDescent(eta, x0):
    x = [x0]
    for i in range(10000):
        x_new = x[-1] - eta*grad(x[-1])
        if abs(grad(x_new)) < 1e-3:
            break
        x.append(x_new)
    return (x)

x = GradientDescent(.001, 1)
print(f'Gia tri nho nhat cua f(x) la: {f(x[-1])} tai x = {x[-1]}')