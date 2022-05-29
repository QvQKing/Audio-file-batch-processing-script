import matplotlib.pyplot as plt
import librosa
import librosa.display
import numpy as np
import sys


# 读取音频wav文件
audio_path = r"D:\CloudMusic\no/000000.wav"
y, sr = librosa.load(audio_path, sr=None, mono=True)
"""
:param
    path	音频路径
    sr	采样率（默认22050，但是有重采样的功能）
    mono	设置为true是单通道，否则是双通道
    offset	音频读取的时间
    duration	获取音频的时长

:returns
    y : 音频的信号值，类型是ndarray
    sr : 采样率
"""
###############################################################################

################################################################################
# 03 使用librosa获取mel谱图
n_mels = 64
n_frames = 5
n_fft = 1024
hop_length = 512
power = 2.0

mel_spectrogram = librosa.feature.melspectrogram(y=y,
                                                 sr=sr,
                                                 n_fft=n_fft,
                                                 hop_length=hop_length,
                                                 n_mels=n_mels,
                                                 power=power)

# librosa.display.specshow(librosa.power_to_db(mel_spectrogram, ref=np.max),
#                          y_axis='mel', fmax=8000, x_axis='time')
# plt.colorbar(format='%+2.0f dB')
##################################################################################

# 04 将mel谱图转换为log mel谱图
log_mel_spectrogram = 20.0 / power * np.log10(np.maximum(mel_spectrogram, sys.float_info.epsilon))
librosa.display.specshow(librosa.power_to_db(log_mel_spectrogram, ref=np.max),
                         y_axis='mel', fmax=8000, x_axis='time')
# plt.colorbar(format='%+2.0f dB')
##################################################################################

plt.show()
