#! python 3

#This is instrucitonal on a Class with Fraction objects
#Note an extra gcd function is used
#My task is to write methods to implement *, /, -, <, >

def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
     def __init__(self,top,bottom):
         self.num = top
         self.den = bottom

     def __str__(self):
         return str(self.num)+"/"+str(self.den)

     def show(self):
         print(self.num,"/",self.den)

     def __add__(self,otherfraction):
         newnum = self.num*otherfraction.den + \
                      self.den*otherfraction.num
         newden = self.den * otherfraction.den
         common = gcd(newnum,newden)
         return Fraction(newnum//common,newden//common)

     def __eq__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den
         return firstnum == secondnum

#implement *, /, -, <, > DONE-EMPTY ONES ARE EASY...
     def __mul__(self, other):
         newNum = self.num * other.num
         newDen = self.den * other.den
         gcdd = gcd(newNum, newDen)
         return Fraction(newNum/gcdd, newDen/gcdd)
        
##    def __truediv__(self, other):
##        
##    def __sub__(self, other):
##        
     def __lt__(self, other):
         a = self.num/self.den
         b = other.num/other.den
         return a < b
        
##    def __gt__(self, other):        

x = Fraction(1,2)
y = Fraction(2,3)
print('x is ' + str(x))
print('y is ' + str(y))
