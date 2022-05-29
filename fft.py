import librosa
import librosa.display
import matplotlib.pyplot as plt
import pywt
# 读取音频文件
filepath = 'D:\snoring-dataset\Snoring Dataset/'
filename = filepath + '000000.wav'
x, sr = librosa.load(filename, sr=None)  # x--音频时间序列(一维数组) ； sr--音频的采样率

# STFT处理绘制声谱图

X = librosa.stft(x)
Xdb = librosa.amplitude_to_db(abs(X))  # X--二维数组数据

plt.figure(figsize=(5, 5))
librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='log')
plt.colorbar()
plt.title('STFT transform processing audio signal')
plt.show()

