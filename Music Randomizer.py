# Import required libraries
import os
import random
import shutil
import ntpath

# Reads the Filenames list
musiccfg = raw_input ("Please drag your MSU-1 configuration text file into this window: ").strip('\"')
rompath = raw_input ("Please drag your ROM into this window: ").strip('\"')
rombase = ntpath.basename(rompath)
rom = os.path.splitext(rombase)
names_file = open(musiccfg)
names = list(line.rstrip('\n') for line in names_file.readlines())
names_file.close()
# Set the root path
root = os.curdir

# Path to copy files from
inputFolder = os.path.join(root, "Music")

# Path to copy files to
outputFolder = os.path.join(root, "Output")

# Store the copied file names here
copiedFiles = []

# Clear the output folder first
for dir in os.listdir(os.curdir):
    if os.path.exists(outputFolder):
        shutil.rmtree(outputFolder)
#Create the output folder
os.makedirs("OutPut")


# Read the files in the directory
for root, dirs, files in os.walk(inputFolder):

    for name in names:
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
            if os.path.isfile(path) and file not in copiedFiles:
                # File is valid
                validFile = True

                # Copy the name to the new list
                copiedFiles.append(file)

                # Copy the file to the output folder
                shutil.copy(path, outputFolder)

                # Rename the file
                os.chdir(outputFolder)
                print "Copied " + file + ", renamed it to " + rom[0]+"-"+name + "!"
                f = open("Output.txt", "a+")
                for i in range(1):                
                    f.write(file + " is " + rom[0]+"-"+name+ "\r\n")
                f.close()
                os.rename(file, rom[0]+"-"+name)
                msu = open(rom[0]+'.msu', 'w')
                os.chdir("..")

shutil.copy(rompath, outputFolder)


