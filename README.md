# MSU-1-Randomizer

This is a randomizer to be used with any and all MSU-1 patched SNES games.

# MSU-1 Randomizer Chaos Usage

1. Place all .pcm files in the music folder
2. Run 'Music Randomizer.py'
3. Follow the instructions in the prompt
4. If needed, patch the ROM in the Output folder with the relevant patch from the Patches folder (this is still being expanded)
5. Run your ROM with Retroarch's Snes9x Core, or the latest version of Snes9x (if requested, I'll gather files for the few other emulators that work for MSU-1 and the SD2SNES files)

# Category Usage

Same as the Chaos mode, but pulls from subdirectories in the Music Categories Folder, pulls from Battle, Event, Field, Character and Boss, make sure there are enough files to populate the text config files you're using, otherwise the process will hang without ever finishing.

# IMPORTANT NOTE

Category will only randomize songs within a specific category. Currently those are hardcoded to be Battle, Event, Field, Character and Boss. You'll need to make a "Music Categories" folder and put your music files into each respective folder. The configuration files define which songs from FFVI vanilla are swapped with the music in each category folder. Make sure there are enough files to populate the text config files you're using, otherwise the process will hang without ever finishing.
