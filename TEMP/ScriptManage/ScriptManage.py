import os
import chardet
import shutil
import subprocess
from switches import *


class ScriptManage:
    def __init__(self):
        pass

    def input_valid(self, dir):
        self.check_path = os.path.abspath(os.path.join(root_path, dir))
        self.run_list = []
        self.version = dir
        # 校验输入
        if dir == '0':
            return 0
        elif not os.path.isdir(self.check_path):
            print('ERROR:没有此目录，请检查本地代码是否更新！\n')
            return 1
        else:
            print(self.check_path)
            return 2

    # 检查文件编码是否为gbk
    def check_encoding(self, file):
        with open(file, 'rb') as f:
            data = f.read()
            if chardet.detect(data)['encoding'] == 'GB2312':
                return True
            else:
                return False

    # 重写非gbk编码的sql
    def rewrite_file(self, file):
        try:
            content = self.read_file(file)
            os.remove(file)
            with open(file, 'w', encoding='GB2312') as f:
                f.write(content)
        except Exception as e:
            print(file + ' GB2312转换失败！')
        else:
            print(file + ' GB2312')

    # 读取非gbk编码的sql内容
    def read_file(self, file):
        with open(file, 'r', encoding='utf-8') as f:
            return f.read()

    def dos2unix(self, file):
        try:
            if not os.path.isfile(file):
                print('ERROR: %s invalid normal file' % file)
                return -1
            # newline这个参数是为了防止python自动把\r\n转\n
            with open(file, 'r', encoding='gbk', newline='') as fd:
                lines = fd.read()
                lines = lines.replace('\r\n', '\n')
                tmpfile = open(file + '_tmp', 'w', newline='')
                tmpfile.write(lines)
                tmpfile.close()
            os.remove(file)
            os.rename(file + '_tmp', file)
        except Exception as e:
            print(file + ' UNIX(LF)转换失败！')
        else:
            print(file + ' UNIX(LF)\n')

    # 生成run.txt
    def genrun(self):
        if os.path.isfile('run.txt'):
            os.remove('run.txt')
        try:
            with open('run.txt', 'w', newline='') as f:
                f.write('-- ' + self.version + '\n\n')
                for i in range(len(self.run_list)):
                    if self.run_list[i] == '02_params_xml.sql' or self.run_list[i].find('rollbak') != -1:
                        continue
                    else:
                        f.write(
                            'db2 -tvmf ' + self.run_list[i] + '          |tee cbs_' + self.version + '_' +
                            self.run_list[i] + '.log\n')
        except Exception as e:
            print('ERROR:run.txt生成失败！')
        else:
            print('run.txt生成成功！内容如下：\n')
        with open('run.txt', 'r') as f:
            content = f.read()
        print(content)

    def format_main(self):
        os.chdir(self.check_path)
        for i in os.listdir():
            if os.path.isdir('%s' % i):
                self.check_path = os.path.join('.', i)
                self.format_main()
            elif os.path.splitext(i)[-1] == '.sql':
                self.run_list.append(i)
                if not self.check_encoding(i):
                    self.rewrite_file(i)
                else:
                    print(i + ' GB2312')
                self.dos2unix(i)
            else:
                pass

    def func_select(self):
        print('请输入序号选择功能【1/2/3】')
        print('【1】脚本格式转换\n【2】开发环境升级\n【3】测试环境xml生成')
        while True:
            flag = input()
            if flag == '1':
                return 1
            elif flag == '2':
                return 2
            elif flag == '3':
                return 3
            else:
                print('ERROR:输入出错，或者没有该选项! 请重新输入!')

    def dev_upg(self):
        try:
            list_file = os.path.abspath('list.txt')
            if os.path.exists('WORKSPACE'):
                os.system('rd WORKSPACE /s/q')
            os.system('mkdir WORKSPACE')
            os.chdir('WORKSPACE')

            print('请输入要升级的数据库名(本地别名)：')
            db_no = input()
            print('请输入数据库密码：')
            db_pwd = input()

            # 复制各项目脚本目录到WORKSPACE，修改run.bat,执行脚本
            for line in open(list_file):
                print(
                    '===================================================================================')
                line = line.strip('\n')
                if self.input_valid(line) == 2:
                    shutil.copytree(os.path.join(
                        self.check_path, 'DB\\SQL\\DB2'), line)
                    os.chdir(line)
                    self.genbat('run.txt', db_no, db_pwd)
                    cmd = os.system('db2cmd call run.bat')
                    try:
                        subp = subprocess.Popen(cmd, shell=True)
                        subp.wait()
                    except Exception as e:
                        print(e)
                    os.chdir('..')
                else:
                    print('ERROR:请检查list.txt!')
                    break
            # 回到TEMP目录
            os.chdir(origin_path)
        except Exception as e:
            print(e)
            return None

    def genbat(self, file, db_no, db_pwd):
        with open(file, 'r') as f:
            content = f.read()
            content = content.replace('|tee', '>>')
            content = content[content.find('\n'):]
            connect_info = 'db2 connect to %s user fmquery using %s\n' % (
                db_no, db_pwd)
            content = connect_info + content
            print(file + ' 要执行的命令如下：')
            print(content)
            # 参数为N时不用确认就继续执行
            if EXEC_AFTER_CONFIRM == "Y":
                print('请确认后输入任意字符回车继续！')
                continue_info = input()
        with open('run.bat', 'w') as f:
            f.write(content)

    def gen_xml(self):
        pass


if __name__ == "__main__":
    # 该脚本存放目录
    origin_path = os.getcwd()
    # 代码库根目录
    root_path = os.path.join(origin_path, '../..')
    sm = ScriptManage()
    try:
        while True:
            func_id = sm.func_select()
            if func_id == 1:
                while True:
                    print('----请输入脚本目录(例：CBS7.8.10)--(输0返回上一级)')
                    dir = input()
                    input_stat = sm.input_valid(dir)
                    if not input_stat:
                        break
                    elif input_stat == 1:
                        continue
                    else:
                        sm.format_main()
                        sm.genrun()
                        os.chdir(origin_path)
            elif func_id == 2:
                sm.dev_upg()
            elif func_id == 3:
                sm.st_xml()
            else:
                pass
    except Exception as e:
        print('ERROR:执行失败!')
