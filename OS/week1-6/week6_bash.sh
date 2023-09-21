#!/bin/bash
''' 
Grep all lines with the string " jane " in the list.txt file
and only take the third field with ' ' as delimiter. The grep 
should match the pattern "jane" with no additional character 
in front or end thus wont match "janet" or "marryjane")
'''
files =$(grep " jane " ~/data/list.txt | cut - d ' ' - f 3)

''' 
Loop through the lines in files only if the file exist
in the directory right "above" it, in this case (/data) and
append the file names in to a new file called oldFiles.txt
'''
for file in $files do
    if [-e "..$file"] then
        echo $file >> oldFiles.txt
    fi
done