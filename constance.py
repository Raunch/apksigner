#!/usr/bin/env python
# coding: utf-8

COMMON_HELP = '''
-h 显示帮助文档
-f 强制重新反编译
-o 反编译输出路径

--help 显示帮助文档
--empty-framework-dir 通过执行如下命令，删除~/Library/apktool/framework/1.apk文件。再次重新反编译，修改之后回编译问题解决
--only-main-class 反编译不涉及asset等目录
'''

JKS_FILE_NAME = "commonalias_pwd_common123456.jks"

JKS_ALIAS = "commonalias"

JKS_PASSWORK = "common123456"

DEFAULT_OUTPUT_NAME = "_signed.apk"

DEFAULT_TEMP_NAME = "_tmp.apk"

ZIPALIGN = "zipalign"

APK_SIGNER = "apksigner"
