#!/usr/bin/env python
# coding: utf-8
import sys
import getopt
import constance
import os
import subprocess

def apk_compile(decompile_path):
    print("decompile_path is [%s]" % decompile_path )
    commandList = []
    commandList.append("java")
    commandList.append("-jar")
    commandList.append("apktool.jar")
    commandList.append("b")
    commandList.append(decompile_path)
    commandList.append("empty-framework-dir")
    commandList.append("--use-aapt2")
    print(commandList)  
    result = subprocess.call(commandList, shell=True)
    if result == 0 :
        print ("compile success")
    else:
        print ("compile failed")
    pass


if __name__ == '__main__':
    if(len(sys.argv) < 2):
        print("参数不少于两个，至少带上需要反编译apk的文件路径")
        sys.exit()
    opts, args = getopt.getopt(sys.argv[1:], "hfo:", ["help", "empty-framework-dir", "only-main-class"])
    for opt_name, opt_value in opts:
        if (opt_name =="-h" or opt_name == "--help"):
            print(constance.COMMON_HELP)
            sys.exit()
    for file in args:
        if(os.path.isdir(file)):
            apk_compile(file)
        else:
            print("compile must be a folder")

    
        
            