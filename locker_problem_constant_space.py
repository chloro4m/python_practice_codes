#locker problem
#There are 100 lockers and 100 students.
##When a student visits a locker he will open it if it's closed, or he will close it if it's open.
##All lockers are initially closed. Student 1 visits every locker (so he will open them all).
##Student 2 visits every other locker (so he will close the 2nd, 4th, 6th...).
##Student 3 visits every third locker (so he will change the state of the 3rd, 6th, 9th...).
##This continues until all 100 students have had a turn with the lockers.
##Which lockers are still open? Can you write an algorithm to figure it out? In constant space?

def flip(listt, idx):
    if listt[idx] == 1:
        listt[idx] = 0
    elif listt[idx] == 0:
        listt[idx] = 1
    else:
        print("PROBLEM: Locker value isn't 1 or 0, or something else!!!")

#a '1' is closed, a '0' is open
#set idx 0 to 9 as number 1
locker = [1] * 100
print("Initially locker looks like this; 1 is closed, 0 is open: ")
print(locker)

#students 1 to 100
for studentNum in range(1,101):
    print("Here's iteration %s so far of locker..."%studentNum)
    print(locker)
    for lockerIdx in range(100):
        if (lockerIdx + 1) % studentNum == 0:
            flip(locker, lockerIdx)

print("After 100 students, it looks like this: ")
print(locker)
