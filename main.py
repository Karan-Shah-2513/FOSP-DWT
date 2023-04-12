import pywt
import numpy as np
import scipy.io.wavfile as wav

# Load speech signal from a WAV file
sample_rate, signal = wav.read("speech.wav")

# Define wavelet function and level of decomposition
wavelet = 'db4'
level = 3

# Perform DWT
coeffs = pywt.wavedec(signal, wavelet, mode='symmetric', level=level)

# Reconstruct signal from DWT coefficients
reconstructed_signal = pywt.waverec(coeffs, wavelet, mode='symmetric')

# Save reconstructed signal to a WAV file
wav.write("reconstructed_speech.wav", sample_rate,
          np.asarray(reconstructed_signal, dtype=np.int16))
