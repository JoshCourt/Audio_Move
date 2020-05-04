# Audio  MOVE
from tkinter import filedialog
from tkinter import *
from os.path import isfile
from os.path import isdir
from os import listdir
from os.path import isfile, join
from pathlib import Path
import time
import os
import subprocess

def listfiles1(LOCATION):
    onlyfiles = [f for f in listdir(LOCATION) if isfile(join(LOCATION, f))]
    print(onlyfiles)
    time.sleep(2)
    return(onlyfiles)

def wherearefiles():
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    return folder_selected

includesuffix = ('.mov', '.mp4', '.mpg', '.mpg2', '.mpg4', '.mpeg', '.mov', 'MP4', '.M4P', '.M4V', '.OGG', '.AVI', '.WMV', '.MOV', '.QT', )

def MAIN():
    videosloc = wherearefiles()
    vidsinloc = listfiles1(videosloc)
    videosloc = Path(videosloc)
    for file in vidsinloc:
        print(file)
        if file.endswith(includesuffix):
        # The following code changes the paths as the function "listfiles" and "wherearefiles" are not outputting in the same path format IE /s with \s ERRHH
            fullloc = videosloc / file
            print(fullloc)
            just_filename = os.path.splitext(file)
            just_filename = just_filename[0]
            fullloc_noextension = os.path.splitext(fullloc)
            fullloc_noextension = fullloc_noextension[0]
            print("just_filename is : "+str(just_filename))
            print("fullloc_noextension is : "+str(fullloc_noextension))
            command = "ffmpeg -i \""+str(fullloc)+"\" -itsoffset -0.50 -i \""+str(fullloc)+"\" -map 0:v -map 1:a -c copy \""+str(fullloc_noextension)+"EDITED.mpg\""
            subprocess.call(command, shell=True)

MAIN()
