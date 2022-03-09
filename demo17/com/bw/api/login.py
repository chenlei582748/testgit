# $ {PROJECT_NAME}:
# $ {NAME}:
# $ {USER}: chenlei
# type:openpyxl.workbook.workbook.Worksheet
# 2022/3/9
# 14:12
import requests

from demo17.com.bw.configs.config import HOST


class Login():

    #requestBody={url,method,data}
    def login(self,requestBody):
        url = HOST+requestBody["url"]
        data = requestBody["data"]
        method = requestBody["method"]

        res = requests.request(method=method,url=url,data=data)
        return res.json()