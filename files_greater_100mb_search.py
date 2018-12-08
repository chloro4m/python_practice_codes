#! python 3

#Looks thru folder tree and prints all files/folders >100MB in size
#Prints files w/ abs path

import os, shutil

path = r'C:\Users\Eric\Downloads'

#100MB = ~100,000,000 bytes
size_bytes_limit = 100 * 1024 * 1024

for folder_name, sub_folders, file_names in os.walk(path):
    for filename in file_names:
        abs_path = os.path.join(folder_name, filename)
        fileSize = os.path.getsize(abs_path)
        if fileSize > size_bytes_limit:
            print(abs_path + ' is ' + str(fileSize) + '.')

print('Done.')
            
    
