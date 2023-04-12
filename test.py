import pywt
import numpy as np
import soundfile as sf

level = 2

# Load input audio file
input_file = "speech.wav"
signal, sample_rate = sf.read(input_file)

# Define wavelet function and level of decomposition
wavelet = 'db1'
# level = 1

# Perform DWT
coeffs = pywt.wavedec(signal, wavelet, level=level)

# Set detail coefficients to zero
zero_coeffs = [coeffs[0]] + [np.zeros_like(coeff) for coeff in coeffs[1:]]
# print(zero_coeffs)

# Reconstruct signal from wavelet coefficients with zero detail coefficients
reconstructed_signal = pywt.waverec(zero_coeffs, wavelet)

# Save reconstructed audio as .wav file
output_file = "reconstructed_audio.wav"
sf.write(output_file, reconstructed_signal, sample_rate)

input_file = output_file
signal, sample_rate = sf.read(input_file)

# Define wavelet function and level of decomposition
wavelet = 'db1'
# level = 1

# Perform DWT
coeffs = pywt.wavedec(signal, wavelet, level=level)

# Set detail coefficients to zero
zero_coeffs = [coeffs[0]] + [np.zeros_like(coeff) for coeff in coeffs[1:]]
# print(zero_coeffs)

# Reconstruct signal from wavelet coefficients with zero detail coefficients
reconstructed_signal = pywt.waverec(zero_coeffs, wavelet)

# Save reconstructed audio as .wav file
output_file = "recon2.wav"
sf.write(output_file, reconstructed_signal, sample_rate)

input_file = output_file
signal, sample_rate = sf.read(input_file)

# Define wavelet function and level of decomposition
wavelet = 'db1'
# level = 1

# Perform DWT
coeffs = pywt.wavedec(signal, wavelet, level=level)

# Set detail coefficients to zero
zero_coeffs = [coeffs[0]] + [np.zeros_like(coeff) for coeff in coeffs[1:]]
# print(zero_coeffs)

# Reconstruct signal from wavelet coefficients with zero detail coefficients
reconstructed_signal = pywt.waverec(zero_coeffs, wavelet)

# Save reconstructed audio as .wav file
output_file = "recon3.wav"
sf.write(output_file, reconstructed_signal, sample_rate)

input_file = output_file
signal, sample_rate = sf.read(input_file)

# Define wavelet function and level of decomposition
wavelet = 'db1'
# level = 1

# Perform DWT
coeffs = pywt.wavedec(signal, wavelet, level=level)

# Set detail coefficients to zero
zero_coeffs = [coeffs[0]] + [np.zeros_like(coeff) for coeff in coeffs[1:]]
# print(zero_coeffs)

# Reconstruct signal from wavelet coefficients with zero detail coefficients
reconstructed_signal = pywt.waverec(zero_coeffs, wavelet)

# Save reconstructed audio as .wav file
output_file = "recon4.wav"
sf.write(output_file, reconstructed_signal, sample_rate)
