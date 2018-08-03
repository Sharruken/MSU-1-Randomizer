# Import required libraries
import os
import random
import shutil
import ntpath

# Reads the Filenames list
rompath = raw_input ("Please drag your ROM into this window: ").strip('\"')
battlecfg = raw_input ("Please drag your MSU-1 Battle configuration text file into this window: ").strip('\"')
bosscfg = raw_input ("Please drag your MSU-1 Boss configuration text file into this window: ").strip('\"')
charcfg = raw_input ("Please drag your MSU-1 Character configuration text file into this window: ").strip('\"')
eventcfg = raw_input ("Please drag your MSU-1 Event configuration text file into this window: ").strip('\"')
fieldcfg = raw_input ("Please drag your MSU-1 Field configuration text file into this window: ").strip('\"')
rombase = ntpath.basename(rompath)
rom = os.path.splitext(rombase)
battle_file = open(battlecfg)
battle_names = list(line.rstrip('\n') for line in battle_file.readlines())
battle_file.close()
char_file = open(charcfg)
char_names = list(line.rstrip('\n') for line in char_file.readlines())
char_file.close()
field_file = open(fieldcfg)
field_names = list(line.rstrip('\n') for line in field_file.readlines())
field_file.close()
event_file = open(eventcfg)
event_names = list(line.rstrip('\n') for line in event_file.readlines())
event_file.close()
boss_file = open(eventcfg)
boss_names = list(line.rstrip('\n') for line in boss_file.readlines())
boss_file.close()

# Set the root path
root = os.curdir

# Path to copy files from
inputFolder = os.path.join(root, "Music")
battleFolder = os.path.join(inputFolder, "Battle")
charFolder = os.path.join(inputFolder, "Character")
fieldFolder = os.path.join(inputFolder, "Field")
eventFolder = os.path.join(inputFolder, "Event")
bossFolder = os.path.join(inputFolder, "Boss")
# Path to copy files to
outputFolder = os.path.join(root, "Output")

# Store the copied file names here
copiedFiles = []

# Clear the output folder first
for dir in os.listdir(os.curdir):
    if os.path.exists(outputFolder):
        shutil.rmtree(outputFolder)
#Create the output folder
os.makedirs("Output")


# Read the files in the directory
for root, dirs, files in os.walk(charFolder):

    for name in char_names:
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
                    f.write(rom[0]+"-"+name + " is " + file + "-Character" + "\r\n")
                f.close()
                os.rename(file, rom[0]+"-"+name)
                msu = open(rom[0]+'.msu', 'w')
                os.chdir("..")
                
for root, dirs, files in os.walk(battleFolder):

    for name in battle_names:
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
                    f.write(rom[0]+"-"+name + " is " + file + "-Battle"  + "\r\n")
                f.close()
                os.rename(file, rom[0]+"-"+name)
                msu = open(rom[0]+'.msu', 'w')
                os.chdir("..")

for root, dirs, files in os.walk(fieldFolder):

    for name in field_names:
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
                    f.write(rom[0]+"-"+name + " is " + file + "-Field"  + "\r\n")
                f.close()
                os.rename(file, rom[0]+"-"+name)
                msu = open(rom[0]+'.msu', 'w')
                os.chdir("..")

for root, dirs, files in os.walk(eventFolder):

    for name in event_names:
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
                    f.write(rom[0]+"-"+name + " is " + file + "-Event"  + "\r\n")
                f.close()
                os.rename(file, rom[0]+"-"+name)
                msu = open(rom[0]+'.msu', 'w')
                os.chdir("..")

for root, dirs, files in os.walk(bossFolder):

    for name in boss_names:
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
                    f.write(rom[0]+"-"+name + " is " + file + "-Boss"  + "\r\n")
                f.close()
                os.rename(file, rom[0]+"-"+name)
                msu = open(rom[0]+'.msu', 'w')
                os.chdir("..")
                
shutil.copy(rompath, outputFolder)


