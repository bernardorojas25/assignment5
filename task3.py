import numpy as np
import matplotlib.pyplot as plt

#load data
data = np.loadtxt("fismflux20020824.dat", comments="#")

#extract 56th column
spectrum = data[:, 61]

x = np.arange(len(spectrum))

plt.plot(x, spectrum)
plt.xlabel("Index")
plt.ylabel("EUV Spectrum (W/m^2/nm)")
plt.grid()
plt.show()
