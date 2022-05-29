import os
# png文件路径
png_path=r'E:\语音处理\频谱\标注文件\stft\no'
# jpg_path=r'E:\语音处理\频谱'
files=os.listdir(png_path)
k=0
for i,file in enumerate(files):
    filename=os.path.splitext(file)[0]
    filetype=os.path.splitext(file)[1]
    if filetype=='.png':
        old_name=os.path.join(png_path,file)
        new_name=os.path.join(png_path,filename+'.jpg')
        os.rename(old_name,new_name)
        # print(old_name,new_name)
        k+=1
print(k)