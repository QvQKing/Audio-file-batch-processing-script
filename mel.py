import IPython
import cv2
import IPython.display

import librosa
import librosa.display

from fastai.vision import *

import os

DATA = 'D:\CloudMusic/'
# CSV_TRN_CURATED = DATA + 'train_curated.csv'  # 训练数据集：文件名，标签
# TRN_CURATED = DATA + 'train_curated'  # 训练数据的图片位置。

# Mel-spectrogram Dataset
PREPROCESSED = os.path.join(DATA)  # 生成数据的保存位置
MELS_TRN_CURATED = os.path.join(PREPROCESSED, 'mels_train_curated.pkl')  # 结果保存文件，图片保存成pkl.


def read_audio(conf, pathname, trim_long_data):
    """
    librosa 是音频处理库，conf.sampling_rate 为采样率 44100
    :param conf:
    :param pathname:
    :param trim_long_data:
    :return:
    """
    y, sr = librosa.load(pathname, sr=conf.sampling_rate)  # 将音频文件加载为浮点时​​间系列。
    # trim silence
    if 0 < len(y):  # workaround: 0 length causes error
        y, _ = librosa.effects.trim(y)  # trim, top_db=default(60)
    # make it unified length to conf.samples
    if len(y) > conf.samples:  # long enough 88200
        if trim_long_data:
            y = y[0:0 + conf.samples]
    else:  # pad blank
        padding = conf.samples - len(y)  # add padding at both ends 不够的话就补充。
        offset = padding // 2
        y = np.pad(y, (offset, conf.samples - len(y) - offset), conf.padmode)
    return y


def audio_to_melspectrogram(conf, audio):
    """
    计算一个梅尔频谱系数图
    :param conf:
    :param audio:
    :return:
    """
    spectrogram = librosa.feature.melspectrogram(audio,
                                                 sr=conf.sampling_rate,
                                                 n_mels=conf.n_mels,
                                                 hop_length=conf.hop_length,
                                                 n_fft=conf.n_fft,
                                                 fmin=conf.fmin,
                                                 fmax=conf.fmax)
    spectrogram = librosa.power_to_db(spectrogram)  # 转化频谱系数单位
    spectrogram = spectrogram.astype(np.float32)
    return spectrogram


def show_melspectrogram(conf, mels, title='Log-frequency power spectrogram'):
    """

    :param conf:
    :param mels:
    :param title:
    :return:
    """
    librosa.display.specshow(mels, x_axis='time', y_axis='mel',
                             sr=conf.sampling_rate, hop_length=conf.hop_length,
                             fmin=conf.fmin, fmax=conf.fmax)
    plt.colorbar(format='%+2.0f dB')
    plt.title(title)
    plt.show()


def read_as_melspectrogram(conf, pathname, trim_long_data, debug_display=False):
    """
    :param conf:
    :param pathname:
    :param trim_long_data:
    :param debug_display:
    :return:
    """
    x = read_audio(conf, pathname, trim_long_data)
    mels = audio_to_melspectrogram(conf, x)
    if debug_display:
        IPython.display.display(IPython.display.Audio(x, rate=conf.sampling_rate))
        show_melspectrogram(conf, mels)
    return mels


def mono_to_color(X, mean=None, std=None, norm_max=None, norm_min=None, eps=1e-6):
    """

    :param X:
    :param mean:
    :param std:
    :param norm_max:
    :param norm_min:
    :param eps:
    :return:
    """
    # Stack X as [X,X,X]
    X = np.stack([X, X, X], axis=-1)

    # Standardize
    mean = mean or X.mean()
    X = X - mean
    std = std or X.std()
    Xstd = X / (std + eps)
    _min, _max = Xstd.min(), Xstd.max()
    norm_max = norm_max or _max
    norm_min = norm_min or _min
    if (_max - _min) > eps:
        # Normalize to [0, 255]
        V = Xstd
        V[V < norm_min] = norm_min
        V[V > norm_max] = norm_max
        V = 255 * (V - norm_min) / (norm_max - norm_min)
        V = V.astype(np.uint8)
    else:
        # Just zero
        V = np.zeros_like(Xstd, dtype=np.uint8)
    return V


def convert_wav_to_image(df, source):
    """
    ## 转化WAV文件为图片，返回包含图片的list。
    :param df:
    :param source:
    :return:
    """
    X = []
    for i, row in df.iterrows():
        wav_path = os.path.join(source, str(row.fname))  # WAV文件路径
        print(wav_path)
        x = read_as_melspectrogram(conf, wav_path, trim_long_data=False)  # 读取图像并转化成数组
        x_color = mono_to_color(x)  # 转化为三维图像
        X.append(x_color)
    return X


def save_as_pkl_binary(obj, filename):
    """Save object as pickle binary file.
    Thanks to https://stackoverflow.com/questions/19201290/how-to-save-a-dictionary-to-a-file/32216025
    """
    with open(filename, 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def convert_dataset(df, source_folder, filename):
    """
    转化WAV文件为图片，并保存image。
    :param df:
    :param source_folder:
    :param filename:
    :return:
    """
    X = convert_wav_to_image(df, source=source_folder)
    save_as_pkl_binary(X, filename)
    print(f'Created {filename}')
    return X


class conf:
    sampling_rate = 44100
    duration = 2  # sec
    hop_length = 347 * duration  # to make time steps 128
    fmin = 20
    fmax = sampling_rate // 2
    n_mels = 128
    n_fft = n_mels * 20
    padmode = 'constant'
    samples = sampling_rate * duration


def get_default_conf():
    return conf


def main():
    trn_curated_df = pd.read_csv(CSV_TRN_CURATED)

    # 获取配置参数
    conf = get_default_conf()

    # 转化数据集 128xN   (N/128)*2=时长。
    convert_dataset(trn_curated_df, TRN_CURATED, MELS_TRN_CURATED);
    # convert_dataset(test_df, TEST, MELS_TEST);


if __name__ == '__main__':
    main()