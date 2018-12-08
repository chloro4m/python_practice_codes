#! python 3

#Walks folder tree and searches for certain extensions (I'll do .pdf)
#Copies found files to a new folder

import os, shutil, re

path = r'C:\Users\Eric\Downloads'
#C:\Users\Eric\Downloads\folder1 has some nested pdf 1, 1.1, 2 to test

#DONE: Create new folder to store all .pdf copies
os.makedirs(os.path.join(path, 'pdf_copies'))

###Don't need?: create '.pdf' regex
##pdf_regex = re.compile(r'.pdf$') #matches last characters
##match_obj = pdf_regex.search(filename)

#DONE: Walk the folder tree, copy .pdf files to new folder
    #Need to parse by ".pdf" extension somehow
for folderName, subfolders, filenames in os.walk(path):
        for filename in filenames:
            print('FILE INSIDE ' + folderName + ': '+ filename)
            if filename[-4:] == '.pdf':
                shutil.copy(os.path.join(folderName, filename), os.path.join(path, 'pdf_copies'))
