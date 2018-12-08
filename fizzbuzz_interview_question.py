##Write a program that prints the numbers from 1 to 100.
##But for multiples of three print “Fizz” instead of the
##number and for the multiples of five print “Buzz”.
##For numbers which are multiples of both three
##and five print “FizzBuzz”.

for i in range (1,101):
    if i % 15 == 0:
        print("Number: %i FizzBuzz 3n5"%i)
        continue
    elif i % 5 == 0:
        print("Number: %i Buzz 5"%i)
        continue
    elif i % 3 == 0:
        print("Number: %i Fizz 3"%i)
        continue
    else:
        print("Number: %i"%i)
    

#WTF???? this shit is so easy. really man..    
              
