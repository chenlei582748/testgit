# $ {PROJECT_NAME}:
# $ {NAME}:
# $ {USER}: chenlei
# type:openpyxl.workbook.workbook.Worksheet
# 2022/3/9
# 14:18
import yaml


def read_yaml(fileData):

    with open(file=fileData,mode='r+',encoding='utf-8')as f:

        list2 = []
        lis = yaml.load(stream=f,Loader=yaml.FullLoader)
        for i in lis:
            list2.append((i["request"],i["resp"]))
        return list2

def writer_yaml(fileData,data):

    with open(file=fileData,mode='r+',encoding='utf-8')as f:
        yaml.dump(data=data,stream=f)

def clear_yaml(fileData):

    with open(file=fileData,mode='r+',encoding='utf-8')as f:
        f.truncate()