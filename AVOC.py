from lxml import etree


class GEN_Annotations:
    def __init__(self, filename, imgpath):
        self.root = etree.Element("annotation")

        child1 = etree.SubElement(self.root, "folder")
        child1.text = "ss"

        child2 = etree.SubElement(self.root, "filename")
        child2.text = filename

        child3 = etree.SubElement(self.root,"path")
        child3.text = imgpath

        child4 = etree.SubElement(self.root, "source")

        # child4 = etree.SubElement(child3, "annotation")
        # child4.text = "PASCAL VOC2007"
        child5 = etree.SubElement(child4, "database")
        child5.text = "Unknown"
        #
        # child6 = etree.SubElement(child3, "image")
        # child6.text = "flickr"
        # child7 = etree.SubElement(child3, "flickrid")
        # child7.text = "35435"

    def set_size(self, witdh, height, channel):
        size = etree.SubElement(self.root, "size")
        widthn = etree.SubElement(size, "width")
        widthn.text = str(witdh)
        heightn = etree.SubElement(size, "height")
        heightn.text = str(height)
        channeln = etree.SubElement(size, "depth")
        channeln.text = str(channel)

    def set_segmented(self,seg=0):
        segmented = etree.SubElement(self.root,"segmented")
        segmented.text = str(seg)


    def savefile(self, filename):
        tree = etree.ElementTree(self.root)
        tree.write(filename, pretty_print=True, xml_declaration=False, encoding='utf-8')

    def add_pic_attr(self, label, xmin, ymin, xmax, ymax):
        object = etree.SubElement(self.root, "object")

        namen = etree.SubElement(object, "name")
        namen.text = label

        pose = etree.SubElement(object,"pose")
        pose.text = "Unspecified"

        truncated = etree.SubElement(object,"truncated")
        truncated.text = "0"

        difficult = etree.SubElement(object,"difficult")
        difficult.text = "0"

        bndbox = etree.SubElement(object, "bndbox")
        xminn = etree.SubElement(bndbox, "xmin")
        xminn.text = str(xmin)
        yminn = etree.SubElement(bndbox, "ymin")
        yminn.text = str(ymin)
        xmaxn = etree.SubElement(bndbox, "xmax")
        xmaxn.text = str(xmax)
        ymaxn = etree.SubElement(bndbox, "ymax")
        ymaxn.text = str(ymax)


import os
import cv2


def getFileList(dir, Filelist, ext=None):
    """
    获取文件夹及其子文件夹中文件列表
    输入 dir：文件夹根目录
    输入 ext: 扩展名
    返回： 文件路径列表
    """
    newDir = dir
    if os.path.isfile(dir):
        if ext is None:
            Filelist.append(dir)
        else:
            if ext in dir[-3:]:
                Filelist.append(dir)

    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir = os.path.join(dir, s)
            getFileList(newDir, Filelist, ext)

    return Filelist


# org_img_folder = './org'

# 检索文件
# imglist = getFileList(org_img_folder, [], 'jpg')
# print('本次执行检索到 ' + str(len(imglist)) + ' 张图像\n')

# for imgpath in imglist:
#     imgname = os.path.splitext(os.path.basename(imgpath))[0]
#     img = cv2.imread(imgpath, cv2.IMREAD_COLOR)
    # 对每幅图像执行相关操作

if __name__ == '__main__':
    org_img_folder = r'.\标注文件\mfcc\ss'

    # 检索文件
    imglist = getFileList(org_img_folder, [], 'png')
    print('本次执行检索到 ' + str(len(imglist)) + ' 张图像\n')
    #
    # filename = imglist[0]
    # name = filename.split('\\')
    # # print(name)
    # anno = GEN_Annotations(name[4],filename)
    # anno.set_size(800, 550, 3)
    # anno.set_segmented()
    # for i in range(1):
    #     xmin = i + 1
    #     ymin = i + 1
    #     xmax = i + 799
    #     ymax = i + 549
    #     anno.add_pic_attr("Snoring", xmin, ymin, xmax, ymax)
    # filename_saved = filename.split('.')
    # # print(filename_saved)
    # anno.savefile('.'+filename_saved[1]+".xml")

    for imagepath in imglist:
        filename = imagepath
        name = filename.split('\\')
        # print(name)
        anno = GEN_Annotations(name[4], filename)
        anno.set_size(800, 550, 3)
        for i in range(1):
            xmin = i + 99
            ymin = i + 64
            xmax = i + 724
            ymax = i + 493
            anno.add_pic_attr("Snoring", xmin, ymin, xmax, ymax)
        # filename_saved = filename.split('.')
        filename_saved=name[4].split('.')
        path=r'E:\语音处理\频谱\VOC\mfcc/ss/'
        anno.savefile(path + filename_saved[0] + ".xml")