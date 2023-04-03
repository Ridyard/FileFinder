
'''this script will traverse a given directory tree and return a list of files of a given type
for example, search all .py files in My Documents tree'''

from pathlib import Path
import os, pyinputplus as pyip


p = Path(input('input the parent directory: '))
if not p.exists(): # checks that the file path is valid
    print(f'file path not recognised - please check again & enter a valid file path\n"{p}"\ngoodbye')
    exit()


fileType = pyip.inputStr('what file extension do you want to return? ') # module to validate the user input (can elaborate here)
print(f'\n==========\n\nthe list of returned matches will be saved in a txt file at location:\n{p}\n\n==========')
matches = [] # to hold the matched files

if not fileType.startswith('.'): # ensure there is a leading '.' in filetype; standardise input
    fileType = '.' + fileType


try:
    matchFile = open(p/'matched files.txt','w') # create a txt file to hold the full file paths to the returned files
    matchFile.write(f'the following is a list of "{fileType}" files within the "{p}" root directory:\n\n')
    
    for root, subfolders, files in os.walk(p): # walk given directory tree
        for file in files:
            if file.endswith(fileType): # if os.walk() encounters a file, check if it ends with fileType...
                matches.append(file) # ...if so, add to matches
                matchFile.write(f'{os.path.join(root,file)}\n') # construct the file path

    matchFile.close()
    print()
except Exception as e:
    print(f'an error occurred:\n{e}')


if len(matches) == 0:
    print(f'there were no {fileType} files returned')
        
for i in matches:
    print(i)

#TO DO: 
# add exception to the firewall?
