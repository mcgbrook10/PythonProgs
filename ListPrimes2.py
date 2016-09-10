
'''
Prime is a number only divisible by itself and 1.
Program Based on 2 observations - 
1) To test if a number has any divisors - it only has to try prime 
numbers because any other number could be divisible by a smaller number
2) The largest Prime number list would be bounded by sqrt(100), since if 
one multiplier is larger than 10 the other one would have to be smaller 
than 10 to reach 100 and would have already been tested

'''
import math
    
def ListPrimes():
    for n in range (2,101):
        if TestPrime(n): 
            print(str(n), "Is a Prime") 
        else:
            print(str(n), "Not a Prime")                     
    return()

def TestPrime(n):
    global List1
    for x in List1:
        if n == x:
            return True
        elif n % x == 0:
            return False
    return True

def BuildPrimeList(maxPrime): 
    primeInd = False
    highPrime = int(math.sqrt(maxPrime))
    PList = []
    for h in range(2,highPrime + 1):
        if  len(PList) == 0:
            PList.append(h)
        else:
            primeInd = False
            for t in PList: 
                if h % t == 0:
                    primeInd = True 
                    break
        if (not primeInd) and (h > 2): 
            PList.append(h) 
    return(PList)               

List1 = BuildPrimeList(100) 
ListPrimes()


