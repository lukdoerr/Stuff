import numpy as np
import matplotlib.pyplot as plt

def moving_average(signal, window_size):
    window = np.ones(window_size) / window_size

    print(len(window))

    return np.convolve(signal, window, mode='valid')

def pt1_impulse_response(K, T, t):
    return K * np.exp(-t / T) * (t >= 0)

def autocorrelation(signal, t):
    ac = np.convolve(signal, signal[::-1], mode='full')
    return ac[len(signal)-1:]

def dirac_impulse(t, t0, amplitude=1.0):
    return amplitude * (t == t0)

K = 3.0  # Proportionalitätskonstante
T = 2.0  # Zeitkonstante

t = np.linspace(0, 0.1, 10)  # Zeitbereich für die Impulsantwort und Autokorrelation

# Diskrete Annäherung des Dirac-Impulses bei t=2
dirac = dirac_impulse(t, 0, amplitude=3.0) 
d = dirac_impulse(t, 0, 3.0)
mv = moving_average(1, 3)
mv1 = moving_average(1,3)

mv_1 = mv * 3



impulse_response = pt1_impulse_response(K, T, t)
autocorr = autocorrelation(impulse_response, t)

# Erzeuge die gespiegelte Hälfte der Autokorrelationsfunktion
autocorr_reflected = autocorr[::-1]

# Kombiniere die gespiegelte Hälfte mit der ursprünglichen Hälfte
full_autocorr = np.concatenate((autocorr_reflected, autocorr))

# Erzeuge den entsprechenden Zeitbereich für die gespiegelte Autokorrelationsfunktion
t_full = np.linspace(-20, 20, len(full_autocorr))

convolved_signal = np.convolve(mv,mv_1, mode='full')
cs = autocorrelation(mv_1, t)

plt.plot(mv, 'c')
#plt.plot(cs, 'y')
plt.plot(convolved_signal)
plt.plot(mv_1, 'g')
plt.xlabel('Zeitversatz (tau)')
plt.ylabel('Autokorrelation')
plt.title('Autokorrelation eines PT1-Glieds')
plt.grid(True)
#plt.ylim(-0.5, 1.0)  # Begrenze die Y-Achsen-Ansicht
plt.show()
