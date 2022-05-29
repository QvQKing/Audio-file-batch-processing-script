# encoding:utf-8

# 用于重设图片大小，主要用来遇到图片大小限制时缩放图片

import cv2

if __name__ == '__main__':
    img = cv2.imread('D:\snoring-dataset\Snoring Dataset\音频数据\标注文件\mfcc\ss/000000.png')
    cv2.imshow('resize before', img)
    # 直接指定目标图片大小
    img = cv2.resize(img, (416, 416))

    # 按比例缩小，例如缩小2倍
    # 原图高
    # height = img.shape[0]
    # # 原图宽
    # width = img.shape[1]
    # # 元祖参数，为宽，高
    # img = cv2.resize(img, (int(width / 2), int(height / 2)))

    cv2.imshow('resize after', img)

    # 写入新文件
    cv2.imwrite('./2.jpg', img)
    # 延迟关闭
    cv2.waitKey()

