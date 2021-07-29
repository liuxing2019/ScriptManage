import os
import sys
import time
import chardet


class Script_Check:
    def __init__(self,dir):
        self.check_path = os.path.join('..',dir)
        print(self.check_path)
        self.run_list = []
        self.version = dir
        # 校验输入
        if not os.path.isdir(self.check_path):
            print('ERROR:没有此目录，请检查本地仓库是否更新！\n')
            return None
        

    # 检查文件编码是否为gbk
    def check_coding(self,file):
        with open(file,'rb') as f:
            data = f.read()
            if chardet.detect(data)['encoding'] == 'GB2312':
                return True
            else:
                return False


    # 重写非gbk编码的sql
    def rewrite_file(self,file):
        try:
            print(file + ' 编码格式有误，正在转换...')
            content = self.read_file(file)
            os.remove(file)
            with open(file,'w',encoding='GB2312') as f:
                f.write(content)
        except Exception as e:
            print(file + '转换失败！')
        else:
            print(file + '转换成功！')


    # 读取非gbk编码的sql内容
    def read_file(self,file):
        with open(file,'r',encoding = 'utf-8') as f:
            return f.read()


    # dos2unix
    def dos2unix(self,file):
        try:
            print(file + ' dos2unix转换中...')
            if not os.path.isfile(file):
                print('ERROR: %s invalid normal file' % file)
                return -1
            # newline这个参数是为了防止python自动把\r\n转\n
            with open(file, 'r',encoding = 'gbk',newline = '') as fd:
                lines = fd.read()
                lines = lines.replace('\r\n','\n')
                tmpfile = open(file+'_tmp', 'w',newline = '')
                tmpfile.write(lines)
                tmpfile.close()
            os.remove(file)
            os.rename(file+'_tmp', file)
        except Exception as e:
            print(file + ' dos2unix转换失败！')
        else:
            print(file + ' dos2unix转换成功！\n')
    
    # 生成02_params_xml.sql
    def gensql(self):
        try:
            if os.path.isfile('02_params_xml.sql'):
                os.remove('02_params_xml.sql')
            with open('02_params.sql','r',newline = '') as f:
                content = f.read()
                content = content.replace('IMPORT FROM \'','IMPORT FROM \'SQL/DB2/')
                new_sql = open('02_params_xml.sql','w',newline = '')
                new_sql.write(content)
                new_sql.close()
            print('生成02_params_xml成功！\n')
        except Exception as e:
            print('ERROR:生成02_params_xml失败！')


    # 生成run.txt
    def genrun(self):
        if os.path.isfile('run.txt'):
            os.remove('run.txt')
        try:
            with open('run.txt','w',newline = '') as f:
                f.write('-- ' + self.version + '\n\n')
                for i in range(len(self.run_list)):
                    if self.run_list[i] == '02_params_xml.sql' or self.run_list[i].find('rollbak')!= -1:
                        continue
                    else:
                        f.write('db2 -tvmf ' + self.run_list[i] + '          |tee cbs_' + self.version + '_' + self.run_list[i] + '.log\n')
        except Exception as e:
            print('ERROR:run.txt生成失败！')
        else:
            time.sleep(1)
            print('run.txt生成成功！内容如下：\n')
            time.sleep(1)
        with open('run.txt','r') as f:
            content = f.read()
        print(content)


    def main(self):
        os.chdir(self.check_path)
        for i in os.listdir():
            if os.path.isdir('%s' %i):
                self.check_path = os.path.join('.',i)
                self.main()
                # 只操作最里层目录
                # os.chdir('..')
            elif os.path.splitext(i)[-1] == '.sql':
                time.sleep(0.3)
                self.run_list.append(i)
                if not self.check_coding(i):
                    self.rewrite_file(i)
                else:
                    print(i + ' 编码格式正确')
                self.dos2unix(i)
            else:
                pass


if __name__ == "__main__":
    origin_path = os.getcwd()
    while True:
        print('----输入要转换的目录名----(例：CBS7.7.10)')
        dir = input()
        sc = Script_Check(dir)
        try:
            sc.main()
            sc.genrun()
            #sc.gensql()
            os.chdir(origin_path)
        except Exception as e:
            print('ERROR:执行失败!')
