import matplotlib.pyplot as plt
import os
from urllib import request, parse
import json
# 有道翻译：中文→英文
def fy(i):
    req_url = 'http://fanyi.youdao.com/translate'  # 创建连接接口
    # 创建要提交的数据
    Form_Date = {}
    Form_Date['i'] = i
    Form_Date['doctype'] = 'json'
    Form_Date['form'] = 'AUTO'
    Form_Date['to'] = 'AUTO'
    Form_Date['smartresult'] = 'dict'
    Form_Date['client'] = 'fanyideskweb'
    Form_Date['salt'] = '1526995097962'
    Form_Date['sign'] = '8e4c4765b52229e1f3ad2e633af89c76'
    Form_Date['version'] = '2.1'
    Form_Date['keyform'] = 'fanyi.web'
    Form_Date['action'] = 'FY_BY_REALTIME'
    Form_Date['typoResult'] = 'false'

    data = parse.urlencode(Form_Date).encode('utf-8')  # 数据转换
    response = request.urlopen(req_url, data)  # 提交数据并解析
    html = response.read().decode('utf-8')  # 服务器返回结果读取
    # print(html)
    # 可以看出html是一个json格式
    translate_results = json.loads(html)  # 以json格式载入
    translate_results = translate_results['translateResult'][0][0]['tgt']  # json格式调取
    # print(translate_results)  # 输出结果
    return translate_results;  # 返回结果
#
#
# res = fy('this is a dog')
# print(res)  # 这是一只狗


plt.style.use("seaborn")
no_snore_path='D:/snoring-dataset/no-snore/'
no_snore_path_dir=os.listdir(no_snore_path)
no_snore_num=0
count=0
no_snore_typrname=[]
for i,filename in enumerate(no_snore_path_dir):
    oldname=filename
    print(oldname)
    newname = filename[6:]
    newname=fy(newname)
    print(newname)
    Oldname=os.path.join(no_snore_path,oldname)
    Newname=os.path.join(no_snore_path,newname)
    os.rename(Oldname,Newname)
    # no_snore_typrname.append(newname)
    count+=1
no_snore_num=count
print(no_snore_num)
# print(no_snore_typrname)
# print(no_snore_num)
# newnames=[]
# for i,file in enumerate(no_snore_typrname):
#     oldname=file
#     newname=file[6:]
#     newname=fy(newname)
#     newnames.append(newname)
#     os.rename(oldname,newname)
# print(newnames)