CBS脚本处理、环境升级。

1.客户端
2.支持多个环境同时跑、多项目同时跑
3.支持导出请求接口

目录：
CBS发版小助手.exe
config.info
CBS发版小助手快捷方式



实现功能：环境升级（已上线的项目+未上线的项目）、发脚本、跑临时脚本
场景：
1、环境升级（已上线项目+未上线项目）三个环境同时，到某个项目需要终止
2、发现金管理平台脚本
3、现金管理平台脚本要回退后发脚本（如果回退的是不可重复执行，需要注意）
4、发测试临时脚本
5、某个环境中漏了某个项目（已上线+未上线）中的某些脚本，需要补充执行
6、05_cbs.sql需要在所有测试环境执行
痛点：
从平台导出后需要删掉del文件等
手动粘贴接口名用程序导出接口，太烦
不可重复执行脚本重复执行了，导致报错或者数据冗余
现金管理平台回退脚本时，不可重复执行脚本也回退会重复执行

发脚本：
从登记脚本，到整理到库：
1.删掉不用的文件，从开发环境导出del
2.归类、不可重复执行****
3.加07.sql
4.改格式，生成run（确定这次需要执行的脚本）
5.提交的时候检查修改内容，检查这次的不可重复执行脚本是不是首次执行。
git pull,生成文件，提交代码
执行脚本
6.检查日志 
7.每次运行就生成20211119_01格式的目录
8.使用自动化工具后不能丢失原有能力

从平台的压缩包---》脚本库