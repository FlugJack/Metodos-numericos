import numpy as np
from matplotlib import pyplot as plt


def funcion(x):
    return np.tan(x)-0.1*x


def funcion2(x):
    return (np.power((1/np.cos(x)), 2)-0.1)



def newton(xi, maxiteraciones, cota):
    error = 1
    i = 1
    print("Metodo de newton")
    while error > cota:
        xr = xi - (funcion(xi)/funcion2(xi))
        
        error = np.abs((xr-xi)/xr)
        xi = xr
        i += 1
        print("Raiz:", xr, " Error:", error)


newton(np.pi, 10, 0.0001)


vectorx = np.arange(3, 4, 0.001)

plt.plot(vectorx, funcion(vectorx))
plt.grid("x")
plt.grid("y")
plt.show()
