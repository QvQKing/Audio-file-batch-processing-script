import os
from PIL import Image
import numpy as np

rootimgs = 'D:\paper\\3low_light_image\compare_lowlighr_enchace\enhancement_image\MBLLEN\\'
targetroot = 'D:\paper\\3low_light_image\compare_lowlighr_enchace\enhancement_image\\'
savdir = 'D:\paper\\3low_light_image\compare_lowlighr_enchace\enhancement_image\\'
file_imgs = os.listdir(rootimgs)

for file_img in file_imgs:
    imgpath = rootimgs + file_img
    targetimg = targetroot + file_img
    image = Image.open(imgpath)  # 用PIL中的Image.open打开图像
    image_arr = np.array(image)  # 转化成numpy数组
    image_tar = image_arr[:, int(image_arr.shape[1] / 3):int(2 * image_arr.shape[1] / 3), :]
    im = Image.fromarray(image_tar)
    im.save(targetimg)