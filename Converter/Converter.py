import os
import re
import shutil
import random
import subprocess

files = os.listdir(os.getcwd())
under_score = ['(',')','[',']'] 
dot = [' ']
root = os.curdir
mp3Folder = os.path.join(root, "MP3s")
wavFolder = os.path.join(root, "WAVs")
oggFolder = os.path.join(root, "OGGs")
flacFolder = os.path.join(root, "FLACs")

#subprocess.call("FFMPEGConvert.bat")


for f in files:
    copy_f = f
    for char in copy_f:
        if (char in dot): copy_f = copy_f.replace(char, '.')
        if (char in under_score): copy_f = copy_f.replace(char,'_')
    os.rename(f,copy_f)



for root, dir, files in os.walk("WAVS"):
   for name in files:
      subprocess.call(["wav2msu.exe" , os.path.join(root, name)])
      print name
