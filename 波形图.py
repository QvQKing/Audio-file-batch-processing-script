import pyworld
import librosa
import librosa.display
from IPython.display import Audio
import numpy as np
from matplotlib import pyplot as plt
# plt.style.use('seaborn-white')
# plt.style.use('seaborn')
# 波形图
x, fs = librosa.load("D:\snoring-dataset\Snoring Dataset/1_0.wav", sr=16000) #librosa load输出的waveform 是 float32
x = x.astype(np.double) # 格式转换
fftlen = pyworld.get_cheaptrick_fft_size(fs)#自动计算适合的fftlen
# 波形图
plt.figure(figsize=(16,11),dpi=50)
# plt.figure()
librosa.display.waveplot(x, sr=fs,x_axis=None,)
plt.savefig('D:\snoring-dataset\Snoring Dataset/1_0-1.png')
plt.show()