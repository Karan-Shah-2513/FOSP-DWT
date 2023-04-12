import pywt
import numpy as np
import scipy.io.wavfile as wav

# Read audio file
fs, audio = wav.read('speech.wav')

# Define initial frequency ranges
low_freq_range = [0, np.pi/2]
high_freq_range = [np.pi/2, np.pi]

# Define the number of iterations
iterations = 3

for i in range(iterations):
    # Perform DWT
    coeffs = pywt.dwt(audio, 'db2')
    cA, cD = coeffs

    # Get low-frequency signal and high-frequency signal
    low_freq_signal = pywt.idwt(cA, None, 'db2')
    high_freq_signal = pywt.idwt(None, cD, 'db2')

    # Change frequency range
    low_freq_range = [low_freq_range[0], low_freq_range[1]/2]
    high_freq_range = [high_freq_range[0]+(high_freq_range[1]-high_freq_range[0])/2,
                       high_freq_range[1]-(high_freq_range[1]-high_freq_range[0])/2]

    # Filter signals based on frequency ranges
    low_freq_signal = low_freq_signal[(low_freq_signal >= low_freq_range[0]) & (
        low_freq_signal <= low_freq_range[1])]
    high_freq_signal = high_freq_signal[(high_freq_signal >= high_freq_range[0]) & (
        high_freq_signal <= high_freq_range[1])]

    # Save low-frequency and high-frequency signals as WAV files
    wav.write(f"low_freq_signal_{i}.wav", fs, low_freq_signal)
    wav.write(f"high_freq_signal_{i}.wav", fs, high_freq_signal)

    # Set low-frequency signal as the input for the next round
    audio = low_freq_signal
