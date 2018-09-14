
import os
cur_dir = os.path.split(os.path.abspath(__file__))[0]
config_dir = cur_dir.replace("common","common\common.conf")
print(config_dir)
testcase_dir = cur_dir.replace("common","TestDatas")

htmlrepost_dir = cur_dir.replace("common","HtmlTestReport")

logs_dir = cur_dir.replace("common","Logs")