import numpy as np
import matplotlib.pyplot as plt

def pt1_impulse_response(K, T, t):
    return K * np.exp(-t / T) * (t >= 0)

def autocorrelation(signal, t):
    ac = np.convolve(signal, signal[::-1], mode='full')
    return ac[len(signal)-1:]

K = 3.0  # Proportionalitätskonstante
T = 2.0  # Zeitkonstante

t = np.linspace(0, 20, 2000)  # Zeitbereich für die Impulsantwort und Autokorrelation

impulse_response = pt1_impulse_response(K, T, t)
autocorr = autocorrelation(impulse_response, t)

# Erzeuge die gespiegelte Hälfte der Autokorrelationsfunktion
autocorr_reflected = autocorr[::-1]

# Kombiniere die gespiegelte Hälfte mit der ursprünglichen Hälfte
full_autocorr = np.concatenate((autocorr_reflected, autocorr))

# Erzeuge den entsprechenden Zeitbereich für die gespiegelte Autokorrelationsfunktion
t_full = np.linspace(-20, 20, len(full_autocorr))

#plt.plot(impulse_response, 'g')
plt.plot(t_full, full_autocorr)
plt.xlabel('Zeitversatz (tau)')
plt.ylabel('Autokorrelation')
plt.title('Autokorrelation eines PT1-Glieds')
plt.grid(True)
#plt.ylim(-0.5, 1.0)  # Begrenze die Y-Achsen-Ansicht
plt.show()
