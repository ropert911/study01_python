# -*- coding: utf-8 -*-

import os


def mkdirs(path):
    dirName = os.path.dirname(path)
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    else:
        print ("{} 哈哈 exist".format(dirName))


path = "/home/abcde/love.xlsx"
print(os.path.dirname(path))  # /home/xq
print(os.path.basename(path))  # love.xlsx
fileName = os.path.basename(path)
print(os.path.splitext(fileName)[0])  # love


mkdirs(path)
