'''
this file is to convert the package exported from XJGL platform into formatted files.
'''

import os
import zipfile


# 解压文件到当前工作目录
def unzip(file_path):
    zip_file = zipfile.ZipFile(file_path)
    zip_list = zip_file.namelist()

    for f in zip_list:
        zip_file.extract(f,'.')
    zip_file.close()
    os.mkdir('WORKSPACE')
    os.system('move DB\\*.sql WORKSPACE')
    os.chdir('WORKSPACE')


# 读取02_params.sql中的请求接口
def read_params():
    request_list = []
    interface_list = []
    dict_list = []
    error_code_list = []
    menu_list = []
    with open('02_params.sql',encoding='gbk') as f:
        content = f.read()
        if content.find('--请求') != -1:
            request_start_addr = content.find('--请求') + 8
            nextline_addr = content[request_start_addr:].find('\n') + request_start_addr
            for addr in range(request_start_addr,nextline_addr,3):
                next_addr = content[addr:].find('\'') + addr
                request_list.append(content[addr:next_addr])
                addr = next_addr + 3
        if content.find('--接口') != -1:
            interface_start_addr = content.find('--接口') + 8
            nextline_addr = content[interface_start_addr:].find('\n') + interface_start_addr
        if content.find('--字典') != -1:
            dict_start_addr = content.find('--字典') + 8
            nextline_addr = content[dict_start_addr:].find('\n') + dict_start_addr
        if content.find('--错误代码') != -1:
            error_code_start_addr = content.find('--错误代码') + 10
            nextline_addr = content[error_code_start_addr:].find('\n') + error_code_start_addr
        if content.find('--菜单定义') != -1:
            menu_start_addr = content.find('--菜单定义') + 10
            nextline_addr = content[menu_start_addr:].find('\n') + menu_start_addr







if __name__ == '__main__':
    pass