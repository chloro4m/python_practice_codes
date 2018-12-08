#print scores of games longer than 2 mins
#format: [score][team][start date/time][end date/time]
import re
'''
lineTest = "hello 69 sam"

lineRgxTest = re.compile(r'\d\d')
matchObjTest = lineRgx.search("69")
print(matchObj.group())
'''

lineReal = "205.4 ABC 01/03/1992 02:57:59 01/4/1992 01:55:55"
lineReal2 = "2.4 ABC 01/9/1992 02:57:53 01/09/1992 02:55:55"

lineRgx = re.compile(r'''(
    (?P<score>\d{1,3}.\d) #score
    (\s+) #space
    (?P<teamName>[A-Z]{3}) #team name
    (\s+) #space
    (?P<startDate>\d{2}/\d{1,2}/\d{4}) #start date
    (\s+) #space
    (?P<startTime>\d{2}:\d{2}:\d{2}) #start time
    (\s+) #space
    (?P<endDate>\d{2}/\d{1,2}/\d{4}) #end date
    (\s+) #space
    (?P<endTime>\d{2}:\d{2}:\d{2}) #end time
    )''', re.VERBOSE)

matchObj = lineRgx.search(lineReal)
print(matchObj.group("score"))
print(matchObj.group("teamName"))
print(matchObj.group("startDate"))
print(matchObj.group("startTime"))
print(matchObj.group("endDate"))
print(matchObj.group("endTime"))

#logic to check that the line is valid
#simplest solution (may not be 100% valid), is check that...
#...all groups (6 total) are there

#LOTS of logic to split() values by m,d,y,h,m,s...

#if valid line:
#must cascade down by comparing LARGEST time properties
#compare end-start property
#if equivalent, go to next largest prop. and compare
#if not equiv., if end>start, return score...

#...UNLESS you get to the :minutes: section:
#if minutes end <= start, dont print score
#if minutes end - start is 3 or more, return score
#if minutes end-start == 2: make sure seconds end is...
#...same or GREATER, and return score


