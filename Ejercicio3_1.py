import numpy as np
from matplotlib import pyplot as plt

def funcion(x):
    c = 10-20*(np.exp(-0.2*x)-np.exp(-0.75*x))-5
    return c

def derivada(x):
    c = (4*np.exp((3/4)*x)-15*np.exp((1/5)*x))/np.exp((19/20)*x)
    return c



def newton(xi, maxiteraciones, cota):
    error = 1
    i = 1
    print("Metodo de newton")
    while error > cota:
        xr = xi - (funcion(xi)/derivada(xi))
        error = np.abs((xr-xi)/xr)
        xi = xr
        i+=1
        print("Raiz:",xr," Error:", error)

newton(0.1,20,0.1)

vectorx = np.arange(0.01,1,0.01)

plt.plot(vectorx,funcion(vectorx))
plt.grid("x")
plt.grid("y")
plt.show()