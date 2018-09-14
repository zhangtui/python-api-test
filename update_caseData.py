
import time
from common.SignatureGenerator import *
from common.read_config import read_config
from common.dir_config import *
class UpdateDatas:
    def updateDates(self,caseDatas,i):
        app_key = read_config().read_config(config_dir, "http", "app_key")
        ip = read_config().read_config(config_dir, "http", "server_ip")
        param_map = eval(caseDatas[i]["request_data"])
        url = caseDatas[i]["url"]
        signt = str(int(time.time() * 1000))
        param_map.update(signt=signt, appkey=app_key)
        sign = SignatureGenerator.generate(url, param_map)
        param_map.update(sign=sign)
        caseDatas[i]["request_data"] = str(param_map)
        caseDatas[i]["url"] = ip + url
if __name__=='__main__':
    from common.MyExcel import MyExcel
    filePath = "E:\\PycharmProjects\\python-api\\TestDatas\\TestData.xlsx"
    me = MyExcel(filePath)
    caseDatas = me.get_all_testDatas()
    UpdateDatas().updateDates(caseDatas,1)
    print(eval(caseDatas[1]["expected_data"]))
    print(type(eval(caseDatas[1]["expected_data"])))