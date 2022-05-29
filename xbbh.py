import matplotlib.pyplot as plt
import librosa.display
import os
# 批量重命名
vpath='D:\CloudMusic/ss'
mps_dir=os.listdir(vpath)
count=0
for i,file in enumerate(mps_dir):
    print(count)
    filename=os.path.splitext(file)[0]
    filetype=os.path.splitext(file)[1]
    if filetype=='.wav':
        olddir=os.path.join(vpath,file)
        newdir=os.path.join(vpath,str(count).zfill(6)+'.wav')
        os.rename(olddir, newdir)
    count+=1


# # 批量转图片-波形图
# vpath='D:\CloudMusic/ss'
# mps_dir=os.listdir(vpath)
# count=0
# for i,file in enumerate(mps_dir):
#     filename=os.path.splitext(file)[0]
#     filetype=os.path.splitext(file)[1]
#     audio_path=vpath+'/'+file
#     print(audio_path,file,filetype,filename)
#     if filetype=='.wav':
#         music,sr=librosa.load(audio_path)
#         plt.figure(figsize=(4,4))
#         librosa.display.waveplot(music,sr=sr)
#         plt.savefig(vpath+'/'+filename)
# #         # plt.show()

# # 音乐文件载入
# path='D:\CloudMusic'
# filename='1.wav'
# audio_path = path+'/'+filename
# music, sr = librosa.load(audio_path)
#
# # 宽高比为14:5的图
# plt.figure(figsize=(224, 224))
# librosa.display.waveplot(music, sr=sr)
# plt.savefig('D:\CloudMusic/1.jpg')
# # 显示图
# plt.show()
