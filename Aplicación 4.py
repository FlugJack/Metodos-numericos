import numpy as np
from matplotlib import pyplot as plt


def fx(x):
    return (1041/x)*(1-np.power(1+x, -360))-135000


def fx2(x):
    return ((1041/np.power(x+1, 360))+((374760*0.01)/np.power(x+1, 361))-1041)/np.power(0.01, 2)


def newton(xi, maxiteraciones, cota):
    error = 1
    i = 1
    print("i | xi | fxi |fdxi | xr | error")
    while error > cota:
        xr = xi - (funcion(xi)/derivada(xi))
        error = np.abs((xr-xi)/xr)
        xi = xr
        i += 1
        print("Raiz:", xr, " Error:", error)


newton(0.1, 20, 0.01)

vectorx = np.arange(0.01, 1, 0.01)

plt.plot(vectorx, fx(vectorx))
plt.grid("x")
plt.grid("y")
plt.show()
