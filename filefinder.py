
'''this script will traverse a given directory tree and return a list of files of a given type
for example, search all .py files in My Documents tree'''

from pathlib import Path
import os

p = Path(input('input the parent directory: '))
fileType = input('what file extension do you want to return? ')
matches = [] # to hold the matched files

if not fileType.startswith('.'): # ensure there is a leading '.' in filetype; standardise input
    fileType = '.' + fileType

matchFile = open(p/'matched files.txt','w') # create a txt file to hold the full file paths to the returned files
matchFile.write(f'the following is a list of "{fileType}" files within the "{p}" root directory:\n\n')

for root, subfolders, files in os.walk(p): # walk given directory tree
    for file in files:
        if file.endswith(fileType): # if os.walk() encounters a file, check if it ends with fileType...
            matches.append(file) # ...if so, add to matches
            matchFile.write(f'{os.path.join(root,file)}\n') # construct the file path
    
matchFile.close()
print()
for i in matches:
    print(i)

