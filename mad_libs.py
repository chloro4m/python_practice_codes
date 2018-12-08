#! python3

#mad libs: read txt file with ADJ, NOUN, ADV, VRB
#allow user to enter replacements for CAPS above^
#create and print out new text file that is also saved off 

#TODO: need to read in text file (madlib1.txt in:
    # C:\Users\Eric\Desktop\python_learn\madlib)
madlib_generic = open('C:\\Users\\Eric\\Desktop\\python_learn\\madlib\\madlib1.txt')
generic_txt = madlib_generic.read()
madlib_generic.close()

#DONE: gather the ADJ...etc in order + occurrence
words = generic_txt.split()
words_unstripped = generic_txt.split()
for i in range(0, len(words)): #strips common punctuations
    words[i] = words[i].strip('.,\'\"?:;!')
    
replace_list = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']
replace_order = []
for i in range(0, len(words)):
    if words[i] in replace_list: #bug: "VERB." not scan--FIXED
        replace_order.append(words[i])

if len(replace_order) == 0:
    print("No ADJ, NOUN, ADV, VRB found.")

#DONE: ask for replacements and scan them in
user_replacements = []

for word in replace_order:
    if word == 'ADJECTIVE' or 'ADVERB':
        print('Enter an ' + word.lower() + ':')
        user_in = input()
        user_replacements.append(user_in)
    elif word == 'NOUN' or 'VERB':
        print('Enter a ' + word.lower() + ':')
        user_in = input()
        user_replacements.append(user_in)

#TODO: create new txt with madlib1.txt's ADJ.. replaced
madlib2 = open('C:\\Users\\Eric\\Desktop\\python_learn\\madlib\\madlib2.txt', 'w')
madlib2.close()

#Need to sub out madlib blanks with user input, *accurately*
for i in range(0, len(words_unstripped)):
    for j in range(0, len(replace_order)):
        words_unstripped[i] = words_unstripped[i].replace(replace_order[j], user_replacements[j], 1)
#words_unstripped now contains the solution in its list        
sentence = ''
for i in range(0, len(words_unstripped)):
    if i == len(words_unstripped)-1:
        sentence += words_unstripped[i]
    else:
        sentence += words_unstripped[i] + ' '
        
madlib2 = open('C:\\Users\\Eric\\Desktop\\python_learn\\madlib\\madlib2.txt', 'w')    
madlib2.write(sentence)
madlib2.close()

    #print madlib1_final.txt
madlib2 = open('C:\\Users\\Eric\\Desktop\\python_learn\\madlib\\madlib2.txt')
print(madlib2.read())
madlib2.close()
