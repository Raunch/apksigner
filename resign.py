#!/usr/bin/env python
# coding: utf-8
import sys
import getopt
import constance
import util
import os
import subprocess

def apk_resign(apk_path, output_path):
    print("apk_path is [%s]" % apk_path )
    
    temp_apk_path = apk_zipalign(apk_path)
    if(len(temp_apk_path) == 0):
        print("apk align failed")
        sys.exit()

    if(len(output_path) == 0):
        apk_name = os.path.basename(apk_path)
        output_path = os.path.dirname(apk_path) + os.path.sep + str(apk_name).split(".")[0] + constance.DEFAULT_OUTPUT_NAME
    
    commandList = []
    commandList.append("java")
    commandList.append("-jar")
    commandList.append("apksigner.jar")
    commandList.append("sign")
    commandList.append("--ks")
    commandList.append(constance.JKS_FILE_NAME)
    commandList.append("--ks-key-alias")
    commandList.append(constance.JKS_ALIAS)
    commandList.append("--ks-pass")
    commandList.append("pass:" + constance.JKS_PASSWORK)
    commandList.append("--key-pass")
    commandList.append("pass:" + constance.JKS_PASSWORK)
    commandList.append("--v2-signing-enabled")
    commandList.append("true")
    commandList.append("--v4-signing-enabled")
    commandList.append("false")
    commandList.append("--out")
    commandList.append(output_path)
    commandList.append(temp_apk_path)
    print(commandList)  
    result = subprocess.call(commandList, shell=True)
    if result == 0 :
        print ("compile success")
    else:
        print ("compile failed")
    pass

def apk_zipalign(apk_path):
    apk_name = os.path.basename(apk_path)
    temp = os.path.dirname(apk_path) + os.path.sep + str(apk_name).split(".")[0] + constance.DEFAULT_TEMP_NAME
    commandList = []
    commandList.append(util.get_executable_name(constance.ZIPALIGN))
    commandList.append("-p")
    commandList.append("-f")
    commandList.append("-v")
    commandList.append("4")
    commandList.append(apk_path)
    commandList.append(temp)
    print(commandList)  
    result = subprocess.call(commandList, shell=True)
    if result == 0 :
        print ("zipalign success")
        return temp
    else:
        print ("zipalign failed")
        return ""


if __name__ == '__main__':
    if(len(sys.argv) < 2):
        print("参数不少于两个，至少带上需要反编译apk的文件路径")
        sys.exit()
    opts, args = getopt.getopt(sys.argv[1:], "ho:", ["help", "empty-framework-dir", "only-main-class"])
    output_path = ""
    for opt_name, opt_value in opts:
        if (opt_name =="-h" or opt_name == "--help"):
            print(constance.COMMON_HELP)
            sys.exit()
        elif (opt_name == "-o"):
            output_path = opt_value
    for file in args:
        if(os.path.isdir(file)):
            for apk_name in os.listdir(file):
                apk_path = file + os.path.sep + apk_name
                apk_resign(file, output_path)
        else:
            apk_resign(file, output_path)

    
        
            