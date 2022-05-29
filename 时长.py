import contextlib
import wave
file_path = r"D:\snoring-dataset\Snoring Dataset\1_1.wav"
with contextlib.closing(wave.open(file_path, 'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    wav_length = frames / float(rate)
    print("音频长度：",wav_length,"秒")
