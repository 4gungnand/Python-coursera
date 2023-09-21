#!/usr/bin/env python3
import sys
import subprocess
import os
# The system's home path (input <student-id> manually)
path = '/home/<student-id>'
# Loop through the file
with open(sys.argv[1], "r") as f:
    for line in f.readlines():
        # Strip the line (remove the \n)
        old_name = line.strip() # or line.replace("\n", "")
        # Replace the old name with the new name
        new_name = old_name.replace("jane", "jdoe")
        # Move the file to the new name (mv <old_path> <new_path>)
        subprocess.run(["mv", path+old_name, path+new_name])
    '''
    for line in f:
        data = line.replace("\n", "")
        base = os.path.basename(data)
        baseNew = base.replace("jane", "jdoe")
        # Dont forget to change to your own directory
        os.chdir(path + '/data')
        os.rename(base, baseNew)
    '''
f.close()
