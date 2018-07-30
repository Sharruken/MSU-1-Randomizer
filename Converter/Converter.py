import os
import re
import shutil
import random
import subprocess

Music = os.listdir("Music")
under_score = ['(',')','[',']'] 
dot = [' ']
root = os.curdir

subprocess.call("FFMPEGConvert.bat")

os.chdir("Music")
for f in Music:
    copy_f = f
    for char in copy_f:
        if (char in dot): copy_f = copy_f.replace(char, '.')
        if (char in under_score): copy_f = copy_f.replace(char,'_')
    os.rename(f,copy_f)
os.chdir("..")


for root, dir, files in os.walk(os.curdir):
   for name in files:
      subprocess.call(["wav2msu.exe" , os.path.join(root, name)])
      print name
