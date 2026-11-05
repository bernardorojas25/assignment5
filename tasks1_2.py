import numpy as np
import matplotlib.pyplot as plt


A=10 #V/m
a=2 #2m
k=0.4 #1/m

def E(x):
    return A*np.cos(((np.pi*x)/a))*np.exp(-k*x)

def dE_ana(x):
    return A * np.exp(-k*x) * (-(np.pi/a)*np.sin((np.pi*x)/a) - 
                               k*np.cos((np.pi*x)/a))

dx= 0.1

"""
dx= 0.05
Forward: O(dx)
Central: O(dw^2)

Forward: 0.1/0.05 = 2 times more accurate
Central: 0.1^2/0.05^2 = 4 times more accurate
"""

x = np.arange(0,20-dx,dx)

analytic = dE_ana(x)

forward = (E(x + dx) - E(x))/ dx 

central = (E(x + dx) - E(x - dx)) / (2*dx)


plt.plot(x,E(x))
plt.xlabel("Position x (m)")
plt.ylabel("Electric Field E(x) (V/m)")
plt.title("Electric Field Along Waveguide")
plt.grid()
plt.show()

plt.figure()
plt.plot(x, analytic, label= "Analytic Derivative") 
plt.plot(x, forward, label= "Forward Diff.") 
plt.plot(x, central, label= "Central Diff.")
plt.title("Comparing Derivatives")
plt.xlabel("Position x (m)")
plt.ylabel("Electric Field E(x) (V/m)")
plt.legend()
plt.grid()
plt.show()

forward_error = np.abs(forward - analytic)
central_error = np.abs(central - analytic)

plt.figure()
plt.semilogy(x, forward_error, label="Forward Difference Error")
plt.semilogy(x, central_error, label="Central Difference Error")
plt.xlabel("Position x (m)")
plt.ylabel("Absolute Error log (V/m²)")
plt.title("Numerical Derivative Errors")
plt.legend()
plt.grid()
plt.show()
