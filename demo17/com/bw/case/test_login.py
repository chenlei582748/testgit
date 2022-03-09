# $ {PROJECT_NAME}:
# $ {NAME}:
# $ {USER}: chenlei
# type:openpyxl.workbook.workbook.Worksheet
# 2022/3/9
# 14:32
import os

import pytest

from demo17.com.bw.api.login import Login
from demo17.com.bw.tools import get_yaml


class TestLogin():

    @pytest.mark.parametrize("req,res",get_yaml.read_yaml(os.getcwd()+r"/com/bw/data/login.yaml"))
    def test_login(self,req,res):
        try:
            responseBody = Login().login(req)
            print(responseBody)
        except Exception as e:
            print(e)
        finally:
            assert responseBody["msg"] == res["message"]