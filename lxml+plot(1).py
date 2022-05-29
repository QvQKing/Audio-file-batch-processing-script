from lxml import etree
with open(r'C:\Users\c9347\Desktop\hehehe\temp.xml', 'r', encoding='utf-8') as f:
    str = f.read()
# print(str)
xml=etree.fromstring(str)
# xml=etree.XML(str)
# xml=etree.HTML(str)
xml=etree.parse(r'C:\Users\c9347\Desktop\hehehe\temp.xml')

print(etree.tostring(xml).decode('utf-8'))
name=xml.xpath('/annotation/object/name/text()')
print(name)

# import matplotlib.pyplot as plt
# # # 一个figure(画布)上，可以有多个区域axes(坐标系)，
# # # 我们在每个坐标系上绘图，也就是说每个axes(坐标系)中，都有axis(坐标轴)。
# # # 如果绘制一个简单的小图形，我们可以不设置figure对象，使用默认创建的figure对象，
# # # 当然我们也可以显示创建figure对象。如果一张figure画布上，需要绘制多个图形。
# # # 那么就必须显示的创建figure对象，然后得到每个位置上的axes对象，进行对应位置上的图形绘制。
# # # 定义fig
# # fig = plt.figure()
# # # 建立子图
# # ax = fig.subplots(2,2)    # 2*2
# # fig, ax = plt.subplots(2,2)
# # # 第一个图为
# # ax[0,0].plot([1,2,5], [3,4,8],label='a')
# # # 第二个图为
# # ax[0,1].plot([1,2], [3,4])
# # # 第三个图为
# # ax[1,1].plot([1,2], [3,4])
# # # 第四个图为
# # ax[1,0].plot([1,2], [3,4])
# # x1 = [0, 1, 2, 3]
# # y1 = [3, 7, 5, 9]
# # x2 = [0, 1, 2, 3]
# # y2 = [6, 2, 13, 10]
# #
# # ax[0,0].plot(x1, y1,label='b')
# # ax[0,0].plot(x2, y2,label='c')
# # ax[0,0].xticks([0,2,4,6,8])
# # plt.show()
# counts=[1,5,4,7,5]
# labels=['a','b','c','d','e']
# fig,ax=plt.subplots()
# # ax.pie(counts,labels=labels,colors=['red','blue','red','blue','red'])
# # plt.show()
# ax.barh(labels,counts)
# for index,item in enumerate(counts):
#     ax.text(item+1,index,str(item))
# plt.show()