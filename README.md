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

# SONG NUMBERS AND WHAT THEY MEAN (FOR CUSTOMIZATION)

For the MSU-1 patch, all files are numbered, with the number corresponding to what track they are replacing in the game, below I've provided a full list of what number corresponds to what track, in order to customize farther, create a folder named whatever you like, put the songs you want in said folder, open Configs/Final Fantasy VI/CONFIGS.txt and add a new line with the name of the folder you added, then create a new text file of the same name and input the track number(s) you would like to replace, congratulations, you can now fully customize how many categories are available by following these steps!

# SONG TRACK NUMBERS AND THEIR CORRESPONDING TRACKS

01 - The Prelude 
02 - Opening Part 01 (Title Screen)
03 - Opening Part 02 (War of the Magi)
04 - Opening Part 03 (Magitek March)
05 - Awakening
06 - Terra
07 - Shadow
08 - Stragus
09 - Gau
10- Edgar & Sabin
11- Coin Song
12- Cyan/Cayenne
13- Locke
14 - Forever Rachel
15 - Relm
16 - Setzer
17 - Epitaph
18 - Celes
19 - Techno de Chocobo
20 - Decisive Battle
21 - Johnny C Bad
22 - Kefka
23 - Narshe
24 - Mystic Forest
25 - Wild West
26 - Save Them
27 - The Gestahl Empire
28 - Troops March On
29 - Under Martial Law
30 - Rain Effect
31 - Metamorphosis
32 - Train Effect? Mystery Train intro? (Special handling)
33 - Esper World
34 - Grand Finale
35 - Mt Koltz
36 - Battle
37 - Unlisted Fanfare
38 - The Wedding Waltz Part 1
39 - Aria de Mezzo Carattare
40 - The Serpent Trench
41 - Slam Shuffle
42 Kids Run Through The City Corner
43 What?/??
44 Grand Finale 1 (Crowd Roar?) (Possibly special handling?)
45 Gogo
46 Returners
47 Fanfare
48 - Umaro
49 - Mog
50 - The Unforgiven
51 - The Fierce Battle
52 - From That Day Forward/The Day After
53 - Blackjack
54 - Catastrophe
55 - The Magic House
56 - Nighty Night (Inn Sleep Effect.)
57 - Wind (Wind.)
58 - Windy Shores (More wind.)
59 - Dancing Mad Parts 1 through 3 (Special handling)
60 - Raft effects ()
61 - Spinach Rag
62 - Rest in Peace
63 - Train running ()
64 - Dream of a train (miscellaneous phantom train scene effects)
65 - Overture Part 1
66 - Part 2
67 - Part 3
68 - Wedding Waltz Part 2
69 - Part 3
70 - Part 4
71 - Devil's Lab/Magitek Research Facility
72 - Fire effect
73 - Machine effect
74 - Burning house background effects
75 - New Continent/The Floating Continent
76 - Searching for Friends
77 - Fanatics
78 - Last Dungeon
79 - Dark World
80 - Dancing Mad 4.2
81 - Silence
82 - Dancing Mad 4.1
83 - Ending Part 1
84 - Ending Part 2
