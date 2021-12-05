'''
log view
生成日志
查看日志
'''

import os
import time


# 创建目录
# 发脚本目录格式：20211205_7.9.45_01
# 环境升级目录格式：20211205_DEV01_ST01_UAT01_01
def dir_create(flag):
    times = 1
    while True:
        if not os.path.exists('%s_%s_%02d' % (time.strftime("%Y%m%d", time.localtime()), flag, times)):
            os.mkdir('%s_%s_%02d' % (time.strftime("%Y%m%d", time.localtime()), flag, times))
            break
        else:
            times += 1


# 检查日志是否报错
def log_check(dir):
    for i in range(os.listdir(dir)):
        print(i,end='  ')
        with open(i) as f:
            content = f.read()
        # 所有的SQLSTATE=02000时，表示日志无报错。
        if content.find("SQLSTATE=") == content.find("SQLSTATE=02000"):
            print('√√√')
        else:
            print('日志报错，请查看日志文件！')



if __name__ == '__main__':
    pass
