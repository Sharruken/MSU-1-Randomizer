# Import required libraries
import os
import random
import shutil
import ntpath
import subprocess

# Reads the Filenames list
root = os.curdir
CONFIG_FILE = open(root+("/Configs/Final Fantasy VI/CONFIG.txt"))
CONFIG = list(line.rstrip('\n') for line in CONFIG_FILE.readlines())
CONFIG_NUM = len(CONFIG)
print(CONFIG)
print(CONFIG_NUM)
rompath = input ("Please drag your ROM into this window:\n").strip('\"')
rombase = ntpath.basename(rompath)
rom = os.path.splitext(rombase)
pcmExt = ".pcm"
# Set the root path



# Path to copy files from
inputFolder = os.path.join(root, "Music")

# Path to copy files to
outputFolder = os.path.join(root, rom[0])
print ("Outputting to: " + outputFolder.strip("."))

# Store the copied file names here
copiedFiles = []
rType = "1"
catInput = "Music Categories"

# Clear the output folder first
for dir in os.listdir(os.curdir):
    if os.path.exists(outputFolder):
        shutil.rmtree(outputFolder)
#Create the output folder
os.makedirs(outputFolder)
shutil.copy(rompath, outputFolder)

def randomize(rand):
    root = os.curdir
    Folder = (root+("/Music Categories/"+rand))
    music_cfg = (root+("/Configs/Final Fantasy VI/"+rand+'.txt'))
    music_file = open(music_cfg)
    music_names = list(line.rstrip('\n') for line in music_file.readlines())
    music_file.close()
    musicname = (root+"/Configs/Final Fantasy VI/Final Fantasy VI Music Names.txt")
    musicname_file = (open(musicname))
    musicnames_cfg = list(line.rstrip('\n') for line in musicname_file.readlines())
    musicname_file.close()
    for root, dirs, files in os.walk(Folder):
        try:
            for name in music_names:
                # Validation flag
                validFile = False

                # Validate the file that will be picked
                while not validFile:

                    # Get a random index
                    index = random.choice(range(len(files)))

                    # Get the path and file from the picked index
                    path = os.path.join(root, files[index])
                    file = files[index]


                    # It must be a file and not be already picked
                    if os.path.isfile(path) and file not in copiedFiles and file.endswith(pcmExt):
                        # File is valid
                        validFile = True

                        # Copy the name to the new list
                        copiedFiles.append(file)

                        # Copy the file to the output folder
                        shutil.copy(path, outputFolder)

                        # Rename the file
                        os.chdir(outputFolder)
                        int_name=int(name)
                        print (musicnames_cfg[int_name-1]+" is now "+file+"!")
                        f = open("Output.txt", "a+")
                        for i in range(1):                
                            f.write(rand+" Music - "+musicnames_cfg[int_name-1]+" is "+file+"\r\n")
                        f.close()
                        os.rename(file, rom[0]+"-"+name+".pcm")
                        msu = open(rom[0]+'.msu', 'w')
                        os.chdir("..")
        except:
            pass
            
for i in range(CONFIG_NUM):
    try:
        randomize(CONFIG[i])
    except FileNotFoundError:
        pass

ipsQ = input ("\nWould you like to apply an IPS patch to your ROM? y/n: ")

if ipsQ == "y" or ipsQ == "Y":
    subprocess.run(["liteips.exe", "-f", os.curdir+"/Patches/Final Fantasy VI.ips", outputFolder+"/"+rom[0]+rom[1]])
scExit = input ("\nPlease press enter to quit.")


