import matplotlib
import pyworld
import librosa
import librosa.display
from IPython.display import Audio
import numpy as np
from matplotlib import pyplot as plt
import math
# plt.style.use('seaborn-white')
# plt.style.use('seaborn')
# 波形图
x, fs = librosa.load("D:\snoring-dataset\Snoring Dataset\音频数据/0-non-snoring sounds/000869.wav", sr=16000) #librosa load输出的waveform 是 float32
x = x.astype(np.double) # 格式转换

fftlen = pyworld.get_cheaptrick_fft_size(fs)#自动计算适合的fftlen
# 波形图
# plt.figure(figsize=(26,13),dpi=32)
# # plt.figure()
# librosa.display.waveplot(x, sr=fs,x_axis=None,)
# # plt.savefig('D:\snoring-dataset\Snoring Dataset/000000-0.png')
# plt.show()
# Audio(x, rate=fs)
# 生成语谱图
# plt.figure()
# plt.specgram(x,NFFT=fftlen, Fs=fs,noverlap=fftlen*1/4, window=np.hanning(fftlen))
# # plt.ylabel('Frequency')
# # plt.xlabel('Time(s)')
# # plt.title('specgram')
# plt.show()
#功率谱图
# D = librosa.amplitude_to_db(librosa.stft(x), ref=np.max)#20log|x|
# plt.figure()
# # librosa.display.specshow(D, sr=fs, hop_length=fftlen*1/4,y_axis='linear')
# librosa.display.specshow(D, sr=fs,hop_length=fftlen*1/4)
# # plt.colorbar(format='%+2.0f dB')
# # plt.title('Linear-frequency power spectrogram')
# plt.show()

# STFT时频图
# S = librosa.stft(x,n_fft=fftlen)    # 幅值
# plt.figure()
# # librosa.display.specshow(np.log(np.abs(S)), sr=fs,hop_length=fftlen/4)
# librosa.display.specshow(np.log(np.abs(S)), sr=fs)
# # plt.colorbar()
# # plt.title('STFT')
# plt.savefig('1')
# plt.show()


# mel spectrogram 梅尔语谱图
# melspec = librosa.feature.melspectrogram(x, sr=fs, n_fft=fftlen, n_mels=128) #(128,856)
# logmelspec = librosa.power_to_db(melspec)# (128,856)
# plt.figure()
# # librosa.display.specshow(logmelspec, sr=fs, x_axis='time', y_axis='mel')
# librosa.display.specshow(logmelspec, sr=fs)
# # plt.title('log melspectrogram')
# plt.show()

# MFCC
y, sr = librosa.load('D:\snoring-dataset\Snoring Dataset/1_0.wav', sr=16000)
# 提取 mel spectrogram feature
# melspec = librosa.feature.melspectrogram(y, sr, n_fft=1024, hop_length=512, n_mels=128)
melspec = librosa.feature.melspectrogram(y, sr, n_fft=1024, hop_length=512, n_mels=128)
logmelspec = librosa.power_to_db(melspec)       # 转换为对数刻度
# 绘制 mel 频谱图
plt.figure()
librosa.display.specshow(logmelspec, sr=sr)
# librosa.display.specshow(logmelspec, sr=sr, x_axis='time', y_axis='mel')
# plt.colorbar(format='%+2.0f dB')        # 右边的色度条
# plt.title('Beat wavform')
plt.show()





