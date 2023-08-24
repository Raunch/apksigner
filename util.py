#!/usr/bin/env python
# coding: utf-8
import platform


def get_executable_name(executable_name):
    executable = "";
    if (platform.system().lower() == "windows"):
        executable = executable_name + ".exe"
    else:
        executable = executable_name
    return executable
