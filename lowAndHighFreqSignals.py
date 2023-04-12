import pywt
import soundfile as sf

# Load the audio signal
audio_file = 'speech.wav'
signal, sr = sf.read(audio_file)

# Choose a wavelet family and level of decomposition
wavelet = 'db1'
level = 5

# Perform the discrete wavelet transform
coeffs = pywt.wavedec(signal, wavelet, level=level)

# Extract the approximation and detail coefficients
cA = coeffs[0]
cD = coeffs[1:]

# Reconstruct the low-frequency and high-frequency signals
low_freq_signal = pywt.waverec([cA] + [None] * level, wavelet)
high_freq_signal = pywt.waverec([None] * level + cD, wavelet)

# Save the low-frequency and high-frequency signals as WAV files
sf.write('low_freq_signal.wav', low_freq_signal, sr)
sf.write('high_freq_signal.wav', high_freq_signal, sr)
