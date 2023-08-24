#!/usr/bin/env python
# coding: utf-8
import sys
import getopt
import constance
import os
import subprocess

command_list_output = []

def apk_decompile(src_path, output_path):
    output = output_path;
    if (len(output)==0):
        apk_name = os.path.basename(src_path)
        output = os.path.dirname(src_path) + os.path.sep + str(apk_name).split(".")[0]
    print("output paht is [%s]" % output )
    commandList = []
    commandList.append("java")
    commandList.append("-jar")
    commandList.append("apktool.jar")
    commandList.append("d")
    commandList.append("-f")
    commandList.append("--only-main-class")
    commandList.append("-o")
    commandList.append(output)
    commandList.append(src_path)
    print(commandList)  

    result = subprocess.call(commandList, shell=True)
    if result == 0 :
        print ("unpack success")
    else:
        print ("unpack failed")
    pass


if __name__ == '__main__':
    if(len(sys.argv) < 2):
        print("参数不少于两个，至少带上需要反编译apk的文件路径")
        sys.exit()
    opts, args = getopt.getopt(sys.argv[1:], "hfo:", ["help", "empty-framework-dir", "only-main-class"])
    output_path = ""
    for opt_name, opt_value in opts:
        if (opt_name =="-h" or opt_name == "--help"):
            print(constance.COMMON_HELP)
            sys.exit()
        elif (opt_name == "-o"):
            output_path = opt_value
    for file in args:
        if(os.path.isdir(file)): 
            for dir_file in os.listdir(file):
                file_path = file + os.path.sep + dir_file
                apk_decompile(file_path, output_path)
        else:
            apk_decompile(file, output_path)

    
        
            