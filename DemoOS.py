#DemoOS.py

from os.path import *

fileName = "python.exe"
print(abspath(fileName))
print(basename("c:\\work\\demo.txt"))

if exists("c:\\python310\\python.exe"):
    print("파일크기:{0}".format(getsize("c:\\python310\\python.exe")))

else:
    print("파일 없음")


import os
print("운영체제이용:{0}".format(os.name))
print("환경변수 :{0}".format(os.environ))
#os.system("notePad.exe")

import glob
print(glob.glob("c:\\work\\*.py"))

