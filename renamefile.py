import os
path=r'D:\snoring-dataset\40test\402 - Mouse click'
filedir=os.listdir(path)
count=0
for i,file in enumerate(filedir):
    # 分割文件的文件名和扩展名
    filename=os.path.splitext(file)[0]
    filetype=os.path.splitext(file)[1]
    # 判断文件类型
    if filetype=='.ogg':
        if count%10==0:
            print(count)
        oldname=os.path.join(path,file)
        newname=os.path.join(path,str(count+3000).zfill(6)+'.wav')
        os.rename(oldname,newname)
    count+=1
print(count)
