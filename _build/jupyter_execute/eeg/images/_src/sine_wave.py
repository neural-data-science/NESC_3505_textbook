import numpy as np

import matplotlib.pyplot as plt



# Get x values of the sine wave
time = np.arange(0, 100, 0.1);
# Amplitude of the sine wave is sine of a variable like time
amplitude = np.sin(time/2)
# Plot a sine wave using time and amplitude obtained for the sine wave
fig = plt.figure(figsize=[20,5])
plt.plot(time, amplitude)
plt.axis('off')
plt.savefig('1D_sine_wave.png')
plt.show()


