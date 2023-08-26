#!/bin/bash
# Grep line with " jane " in the List.txt file and cut the third field)
# (note: no additional character in front/end of "jane")
files=$(grep " jane " ~/data/list.txt | cut -d ' ' -f 3)
# Loop through the files
# If the file exist in the directory (/data directory), 
# Append the file name to oldFiles.txt
for file in $files; do
    if [ -e "..$file" ]; then
        echo $file >> oldFiles.txt;
    fi
done

######

#!/usr/bin/env python3
import sys # to catch argument/command
import subprocess # to run the command
# Read the 1st argument from cmd as the file name
f= open (sys.argv[1],"r")
# The system's home path (change to your own directory)
path='/home/<student-id>'
# Loop through the file
for line in f.readlines():
    # Strip the line (remove the \n)
    old_name = line.strip()
    # Replace the old name with the new name
    new_name = old_name.replace("jane","jdoe")
    # Move the file to the new name (mv <old_path> <new_path>)
    subprocess.run(["mv",path+old_name,path+new_name])
f.close()

or

#!/usr/bin/env python3

import sys
import os
from pathlib import Path
with open (sys.argv[1], "r") as myfile:
   for line in myfile:
    data= line.replace("\n", "")
    base=os.path.basename(data)
    baseNew = base.replace("jane","jdoe")
    #Dont forget to change to your own directory
    os.chdir('/home/student-02-06265fe82641/data')
    os.rename(base, baseNew)
myfile.close()