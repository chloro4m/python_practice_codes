import re
lineReal = "205.4 ABC 01/03/1992 02:57:59 01/4/1992 01:55:55"
 
lineRgx = re.compile(r'''(
    (\d{1,3}.\d) #score
    (\s+) #space
    ([A-Z]{3}) #team name
    (\s+) #space
    (\d{2}/\d{1,2}/\d{4}) #start date
    (\s+) #space
    (\d{2}:\d{2}:\d{2}) #start time
    (\s+) #space
    (\d{2}/\d{1,2}/\d{4}) #end date
    )''', re.VERBOSE)
 
#lineRgx = re.compile(r'(\d{1,3}.\d).*([A-Z]{3})')

matchObj = lineRgx.search(lineReal)
print(matchObj.group())
