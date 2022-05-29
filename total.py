import os
import glob
import shutil

from PIL import Image
import random

from lxml import etree

# 所有路径以'/'结尾
your_voc_path = 'C:/Users/c9347/Desktop/voc/'  # voc数据集路径
yolo_path = 'D:/labels/positive/'  # 原始数据集路径
yolo_filtered_path = 'D:/labes_29/'  # 过滤后的yolo数据集路径
# trainval_percent = 0.9
# train_percent = 0.9
threshold = 200  # 图片数量阈值，选取图片数量大于350的类别
# threshold_cls = 15  # 类别阈值，选取最多的前15类数据

labels = ['road roller', 'bar deposits', 'piece deposits', 'brick', 'earth vehicles', 'tower', 'digger', 'bulldozer',
          'drill', 'crane', 'concrete truck', 'mixer', 'concrete simple house', 'simple house', 'green cover',
          'black cover', 'blue enclosure', 'grey enclosure', 'color enclosure', 'building', 'groove', 'big building',
          'building frame', 'scaffold', 'vehicle', 'grave mound', 'garbage', 'crushed stones', 'bricks', 'greenhouse',
          'site shanty', 'woodpile', 'fuel tank', 'big truck', 'car', 'boxcar', 'small truck', 'van car',
          'watering car', 'tutu', 'crane closed', 'Agricultural Tricycles', 'bus', 'pickup', 'large cement pipes',
          'middle cement pipes', 'small cement pipes', 'thin steel pipe', 'crude steel pipe', 'big stell pipe', 'slab',
          'U-steel', 'road leveling machine']
# 建立所需文件夹
# os.path.exists(path)——检验指定的对象是否存在。是True,否则False.
# os.makedirs(path[, mode]) 递归文件夹创建函数。
if not os.path.exists(your_voc_path + 'VOCdevkit/VOC2007/Annotations/'):
    os.makedirs(your_voc_path + 'VOCdevkit/VOC2007/Annotations/')
if not os.path.exists(your_voc_path + 'VOCdevkit/VOC2007/ImageSets/Layout'):
    os.makedirs(your_voc_path + 'VOCdevkit/VOC2007/ImageSets/Layout')
if not os.path.exists(your_voc_path + 'VOCdevkit/VOC2007/ImageSets/Main'):
    os.makedirs(your_voc_path + 'VOCdevkit/VOC2007/ImageSets/Main')
if not os.path.exists(your_voc_path + 'VOCdevkit/VOC2007/ImageSets/Segmentation'):
    os.makedirs(your_voc_path + 'VOCdevkit/VOC2007/ImageSets/Segmentation')
if not os.path.exists(your_voc_path + 'VOCdevkit/VOC2007/JPEGImages'):
    os.makedirs(your_voc_path + 'VOCdevkit/VOC2007/JPEGImages')
if not os.path.exists(your_voc_path + 'VOCdevkit/VOC2007/labels'):
    os.makedirs(your_voc_path + 'VOCdevkit/VOC2007/labels')
if not os.path.exists(your_voc_path + 'VOCdevkit_filtered/VOC2007/Annotations/'):
    os.makedirs(your_voc_path + 'VOCdevkit_filtered/VOC2007/Annotations/')
if not os.path.exists(your_voc_path + 'VOCdevkit_filtered/VOC2007/ImageSets/Layout'):
    os.makedirs(your_voc_path + 'VOCdevkit_filtered/VOC2007/ImageSets/Layout')
if not os.path.exists(your_voc_path + 'VOCdevkit_filtered/VOC2007/ImageSets/Main'):
    os.makedirs(your_voc_path + 'VOCdevkit_filtered/VOC2007/ImageSets/Main')
if not os.path.exists(your_voc_path + 'VOCdevkit_filtered/VOC2007/ImageSets/Segmentation'):
    os.makedirs(your_voc_path + 'VOCdevkit_filtered/VOC2007/ImageSets/Segmentation')
if not os.path.exists(your_voc_path + 'VOCdevkit_filtered/VOC2007/JPEGImages'):
    os.makedirs(your_voc_path + 'VOCdevkit_filtered/VOC2007/JPEGImages')
if not os.path.exists(your_voc_path + 'VOCdevkit_filtered/VOC2007/labels'):
    os.makedirs(your_voc_path + 'VOCdevkit_filtered/VOC2007/labels')
if not os.path.exists(yolo_filtered_path):
    os.makedirs(yolo_filtered_path)
# 数据重命名
# os.listdir(path)——列出path目录下所有的文件和目录名。
listdir = os.listdir(yolo_path)
count = 0
for i, file in enumerate(listdir):
    if i % 100 == 0:
        print(i)
    #  os.path.splitext(path)
    # 分离文件名与扩展名；默认返回(fname,fextension)元组，可做分片操作>>> os.path.splitext('c:\\csv\\test.csv')
    # ('c:\\csv\\test', '.csv')
    filename = os.path.splitext(file)[0]  # 文件名
    filetype = os.path.splitext(file)[1]  # 文件扩展名
    if filetype == '.txt':
        continue
    # os.path.join(path1[, path2[, ...]])
    # 将多个路径组合后返回，第一个绝对路径之前的参数将被忽略。>>> os.path.join('c:\\', 'csv', 'test.csv')
    # 'c:\\csv\\test.csv'

    Olddir = os.path.join(yolo_path, file)
    Newdir = os.path.join(yolo_path, str(count).zfill(6) + '.jpg')
    Oldanno = os.path.join(yolo_path, filename + '.txt')
    Newanno = os.path.join(yolo_path, str(count).zfill(6) + '.txt')
    # os.rename(src, dst) 重命名文件或目录，从 src 到 dst
    os.rename(Olddir, Newdir)
    os.rename(Oldanno, Newanno)
    shutil.copyfile(Newdir, your_voc_path + 'VOCdevkit/VOC2007/JPEGImages/' + str(count).zfill(6) + '.jpg')
    count += 1

# 生成voc格式数据集
voc_xml = your_voc_path + 'VOCdevkit/VOC2007/Annotations/'

# 匹配文件路径下的所有jpg文件，并返回列表
img_glob = glob.glob(yolo_path + '*.jpg')

img_base_names = []

for img in img_glob:
    # os.path.basename:取文件的后缀名
    img_base_names.append(os.path.basename(img))

img_pre_name = []

for img in img_base_names:
    # os.path.splitext:将文件按照后缀切分为两块
    temp1, temp2 = os.path.splitext(img)
    img_pre_name.append(temp1)
    print(f'imgpre:{len(img_pre_name)}')
for i, img in enumerate(img_pre_name):
    if i % 100 == 0:
        print(i)
    with open(voc_xml + img + '.xml', 'w') as xml_files:
        image = Image.open(yolo_path + img + '.jpg')
        img_w, img_h = image.size
        xml_files.write('<annotation>\n')
        xml_files.write('   <folder>folder</folder>\n')
        xml_files.write(f'   <filename>{img}.jpg</filename>\n')
        xml_files.write('   <source>\n')
        xml_files.write('   <database>Unknown</database>\n')
        xml_files.write('   </source>\n')
        xml_files.write('   <size>\n')
        xml_files.write(f'     <width>{img_w}</width>\n')
        xml_files.write(f'     <height>{img_h}</height>\n')
        xml_files.write(f'     <depth>3</depth>\n')
        xml_files.write('   </size>\n')
        xml_files.write('   <segmented>0</segmented>\n')
        with open(yolo_path + img + '.txt', 'r') as f:
            # 以列表形式返回每一行
            lines = f.read().splitlines()
            for each_line in lines:
                line = each_line.split(' ')
                xml_files.write('   <object>\n')
                xml_files.write(f'      <name>{labels[int(line[0])]}</name>\n')
                xml_files.write('      <pose>Unspecified</pose>\n')
                xml_files.write('      <truncated>0</truncated>\n')
                xml_files.write('      <difficult>0</difficult>\n')
                xml_files.write('      <bndbox>\n')
                center_x = round(float(line[1]) * img_w)
                center_y = round(float(line[2]) * img_h)
                bbox_w = round(float(line[3]) * img_w)
                bbox_h = round(float(line[4]) * img_h)
                xmin = str(int(center_x - bbox_w / 2))
                ymin = str(int(center_y - bbox_h / 2))
                xmax = str(int(center_x + bbox_w / 2))
                ymax = str(int(center_y + bbox_h / 2))
                xml_files.write(f'         <xmin>{xmin}</xmin>\n')
                xml_files.write(f'         <ymin>{ymin}</ymin>\n')
                xml_files.write(f'         <xmax>{xmax}</xmax>\n')
                xml_files.write(f'         <ymax>{ymax}</ymax>\n')
                xml_files.write('      </bndbox>\n')
                xml_files.write('   </object>\n')
        xml_files.write('</annotation>')

# # 划分数据集
# xmlfilepath = your_voc_path + 'VOCdevkit/VOC2007/Annotations/'
# txtsavepath = your_voc_path + 'VOCdevkit/VOC2007/ImgSets/Main/'
# total_xml = os.listdir(xmlfilepath)
#
# num = len(total_xml)
# list = range(num)
# tv = int(num * trainval_percent)
# tr = int(tv * train_percent)
# trainval = random.sample(list, tv)
# train = random.sample(trainval, tr)
#
# ftrainval = open(your_voc_path + 'VOCdevkit/VOC2007/ImageSets/Main/trainval.txt', 'w')
# ftest = open(your_voc_path + 'VOCdevkit/VOC2007/ImageSets/Main/test.txt', 'w')
# ftrain = open(your_voc_path + 'VOCdevkit/VOC2007/ImageSets/Main/train.txt', 'w')
# fval = open(your_voc_path + 'VOCdevkit/VOC2007/ImageSets/Main/val.txt', 'w')
#
# for i in list:
#     name = total_xml[i][:-4] + '\n'
#     if i in trainval:
#         ftrainval.write(name)
#         if i in train:
#             ftrain.write(name)
#         else:
#             fval.write(name)
#     else:
#         ftest.write(name)
#
# ftrainval.close()
# ftrain.close()
# fval.close()
# ftest.close()

# 数据筛选
print('根据阈值计算筛选后的类别')
path = your_voc_path + 'VOCdevkit/VOC2007/Annotations/'
listdir = os.listdir(path)
count = [0 for i in range(53)]  # 每个类别的图片数
for file in listdir:
    with open(path + file, "r") as f:
        text = f.read()
    text = etree.fromstring(text)
    name = text.xpath('/annotation/object/name/text()')
    if name[0] not in ['tutu', 'car', 'garbage', 'van car', 'Agricultural Tricycles', 'pickup']:
        count[int(labels.index(name[0]))] += 1
new_labels = []  # 筛选后的类别标签
new_cls = []  # 筛选后的类别编号


# 根据类别阈值筛选
def maxk(arraylist, k):  # 返回最大的前k个数据的索引，k为类别阈值
    maxlist = []
    maxlist_id = [i for i in range(0, k)]
    m = [maxlist, maxlist_id]
    for i in maxlist_id:
        maxlist.append(arraylist[i])
    for i in range(k, len(arraylist)):  # 对目标数组之后的数字
        if arraylist[i] > min(maxlist):
            mm = maxlist.index(min(maxlist))
            del m[0][mm]
            del m[1][mm]
            m[0].append(arraylist[i])
            m[1].append(i)
    return maxlist_id


# kmax_list = maxk(count, threshold_cls)
# for i in kmax_list:
#     new_cls.append(i)
#     new_labels.append(labels[i])
# 根据图片数量阈值筛选
for index, i in enumerate(count):
    if int(i) > threshold:
        new_cls.append(index)
        new_labels.append(labels[index])

img_glob = glob.glob(yolo_path + '*.jpg')
img_base_names = []
for img in img_glob:
    # os.path.basename:取文件的后缀名
    img_base_names.append(os.path.basename(img))
print('开始筛选数据')
img_pre_name = []
count = 0
for img in img_base_names:
    # os.path.splitext:将文件按照后缀切分为两块
    temp1, temp2 = os.path.splitext(img)
    img_pre_name.append(temp1)

print('清空筛选后的文件夹')
voc_filter_xml = your_voc_path + 'VOCdevkit_filtered/VOC2007/Annotations/'
listxml = os.listdir(voc_filter_xml)
# 清空筛选后的文件夹
for file in listxml:
    os.remove(voc_filter_xml + file)
voc_filter_img = your_voc_path + 'VOCdevkit_filtered/VOC2007/JPEGImages/'
listimg = os.listdir(voc_filter_img)
for file in listimg:
    os.remove(voc_filter_img + file)
print('写入筛选后的数据')
for i, img in enumerate(img_pre_name):
    if i % 100 == 0:
        print(i)
    with open(yolo_path + img + '.txt', 'r') as f:
        # 以列表形式返回每一行
        lines = f.read().splitlines()
    line = lines[0].split(' ')
    if int(line[0]) in new_cls:
        # 生成筛选后的的yolo格式数据集
        newcls = new_cls.index(int(line[0]))
        newanno_txt = line
        newanno_txt[0] = str(newcls)
        newtxt = ' '.join(newanno_txt)
        with open(yolo_filtered_path + str(count).zfill(6) + '.txt', 'w') as f:
            f.write(newtxt)
        shutil.copyfile(yolo_path + img + '.jpg', yolo_filtered_path + str(count).zfill(6) + '.jpg')
        # 生成筛选后的的xml格式数据集
        shutil.copyfile(yolo_path + img + '.jpg',
                        voc_filter_img + str(count).zfill(6) + '.jpg')
        with open(voc_filter_xml + str(count).zfill(6) + '.xml', 'w') as xml_files:
            image = Image.open(yolo_path + img + '.jpg')
            img_w, img_h = image.size
            xml_files.write('<annotation>\n')
            xml_files.write('   <folder>folder</folder>\n')
            xml_files.write(f'   <filename>{img}.jpg</filename>\n')
            xml_files.write('   <source>\n')
            xml_files.write('   <database>Unknown</database>\n')
            xml_files.write('   </source>\n')
            xml_files.write('   <size>\n')
            xml_files.write(f'     <width>{img_w}</width>\n')
            xml_files.write(f'     <height>{img_h}</height>\n')
            xml_files.write(f'     <depth>3</depth>\n')
            xml_files.write('   </size>\n')
            xml_files.write('   <segmented>0</segmented>\n')
            for each_line in lines:
                line = each_line.split(' ')
                xml_files.write('   <object>\n')
                xml_files.write(f'      <name>{new_labels[newcls]}</name>\n')
                xml_files.write('      <pose>Unspecified</pose>\n')
                xml_files.write('      <truncated>0</truncated>\n')
                xml_files.write('      <difficult>0</difficult>\n')
                xml_files.write('      <bndbox>\n')
                center_x = round(float(line[1]) * img_w)
                center_y = round(float(line[2]) * img_h)
                bbox_w = round(float(line[3]) * img_w)
                bbox_h = round(float(line[4]) * img_h)
                xmin = str(int(center_x - bbox_w / 2))
                ymin = str(int(center_y - bbox_h / 2))
                xmax = str(int(center_x + bbox_w / 2))
                ymax = str(int(center_y + bbox_h / 2))
                xml_files.write(f'         <xmin>{xmin}</xmin>\n')
                xml_files.write(f'         <ymin>{ymin}</ymin>\n')
                xml_files.write(f'         <xmax>{xmax}</xmax>\n')
                xml_files.write(f'         <ymax>{ymax}</ymax>\n')
                xml_files.write('      </bndbox>\n')
                xml_files.write('   </object>\n')
            xml_files.write('</annotation>')
        count += 1

xmlfilepath = your_voc_path + 'VOCdevkit_filtered/VOC2007/Annotations/'
txtsavepath = your_voc_path + 'VOCdevkit_filtered/VOC2007/ImgSets/Main/'
total_xml = os.listdir(xmlfilepath)

# #划分数据集
# num = len(total_xml)
# list = range(num)
# tv = int(num * trainval_percent)
# tr = int(tv * train_percent)
# trainval = random.sample(list, tv)
# train = random.sample(trainval, tr)
#
# ftrainval = open(your_voc_path + 'VOCdevkit_filtered/VOC2007/ImageSets/Main/trainval.txt', 'w')
# ftest = open(your_voc_path + 'VOCdevkit_filtered/VOC2007/ImageSets/Main/test.txt', 'w')
# ftrain = open(your_voc_path + 'VOCdevkit_filtered/VOC2007/ImageSets/Main/train.txt', 'w')
# fval = open(your_voc_path + 'VOCdevkit_filtered/VOC2007/ImageSets/Main/val.txt', 'w')
#
# for i in list:
#     name = total_xml[i][:-4] + '\n'
#     if i in trainval:
#         ftrainval.write(name)
#         if i in train:
#             ftrain.write(name)
#         else:
#             fval.write(name)
#     else:
#         ftest.write(name)
#
# ftrainval.close()
# ftrain.close()
# fval.close()
# ftest.close()
print('数据筛选完成')
