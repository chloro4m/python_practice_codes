#! python 3

#In folder, for given prefix, such as hi001.txt, hi002.txt...
#If numbering gap, rename all later files to close gap
#Example: (hi001, hi003, hi006) -> (hi001, hi002, hi003)
#Ex. in C:\Users\Eric\Desktop\gaps_practice\prac1

import os, shutil, re
path = r'C:\Users\Eric\Desktop\gaps_practice\prac1'

file_names = os.listdir(path) #['hi001.txt', 'hi003.txt', 'hi006.txt']
total_files = len(file_names)

rgx_3num = re.compile('(\D+)(\d\d\d)(\D+)')
prefix_obj = rgx_3num.search(file_names[0])
prefix = prefix_obj.group(1)
suffix_obj = rgx_3num.search(file_names[0])
suffix = suffix_obj.group(3)

file_num_only = [] #for the '001', 003, etc
for i in range(0, total_files):
    match_obj = rgx_3num.search(file_names[i])
    file_num_only.append(match_obj.group(2))

file_num_only_int = [] #converts above list to list of ints
for i in range(0, total_files):
    file_num_only_int.append(int(file_num_only[i]))

min_file_num = file_num_only_int[0]
gap_fixed_int = []
for i in range(0, total_files):
    if i == 0:
        gap_fixed_int.append(min_file_num)
    else:
        gap_fixed_int.append(gap_fixed_int[i-1] + 1)

gap_fixed_str = []
for i in range(0, total_files):
    gap_fixed_str.append(str(gap_fixed_int[i]).rjust(3, '0'))
    
#last pieces:
for i in range(0, total_files):
    new_path = prefix + gap_fixed_str[i] + suffix
    shutil.move(os.path.join(path, file_names[i]), \
                os.path.join(path, new_path))

print('Done.')
    

#Extra credit: Insert gaps
