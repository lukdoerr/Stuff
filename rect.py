import numpy as np
import matplotlib.pyplot as plt

# Definition der Rechtecksignale
def rectangle_wave(t, a, b, val):
    return np.where((t >= a) & (t <= b), val, 0)

# Zeitbereich
t = np.linspace(-10, 10, 1000)

# Signale definieren
x_t = rectangle_wave(t, 0, 3, 2)  # Rechtecksignal von 3 bis 6
y_t = rectangle_wave(t, 0, 1, 3)  # Rechtecksignal von 0 bis 3

# Faltung durchführen
z_t = np.convolve(x_t, y_t, mode='full') * (t[1] - t[0])  # Beachte die Abtastung

# Zeitbereich für das gefaltete Signal
t_conv = np.linspace(2*t[0], 2*t[-1], len(z_t))

# Plotte die beiden Signale x(t) und y(t)
plt.figure(figsize=(10, 4))
plt.plot(t, x_t, label='$x(t)$')
plt.plot(t, y_t, label='$y(t)$')
plt.xlabel('Zeit')
plt.ylabel('Amplitude')
plt.title('Rechtecksignale $x(t)$ und $y(t)$')
plt.grid(True)
plt.legend()

# Plotte das gefaltete Signal z(t)
plt.figure(figsize=(10, 4))
plt.plot(t_conv, z_t)
plt.xlabel('Zeit')
plt.ylabel('Amplitude')
plt.title('Gefaltetes Signal $z(t)$')
plt.grid(True)
plt.show()

