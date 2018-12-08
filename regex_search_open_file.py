#! python3

import re, os
path = r'C:\Users\Eric\Desktop\python_learn\sample_txts'
#Opens all .txt files in folder, scans in user's regex
#Searches for any matching lines, then prints matches out

#DONE: Gather the regex from the user, create rgx obj stuff
print('Please enter a regex: ')
rgx_in = input()
rgx = re.compile(rgx_in)
print('Will look in ' + path + 'for all regex matches and print them.')

#TODO: For each file, scan for matches and store in list:
matches = []
total_files = 0
for filename in os.listdir(path):
    total_files += 1
    abs_path = os.path.join(path, filename)
    file_obj = open(abs_path, 'r')
    text = file_obj.read()
    #do rgx shit, remember to catch all instances, not just one 
    matches += rgx.findall(text) 
    file_obj.close()

#DONE: Print matches from list
print('Here is a list of matches to your regex. We scanned a \
total of ' + str(total_files) + ' files.')
for i in range(0, len(matches)):
    print(matches[i] + '\n')
