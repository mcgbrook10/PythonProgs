
'''
Write a program that outputs a table of Celsius temperatures from 0-100, in increments of 5. 
In addition the corresponding Fahrenheit temperature should be listed
'''
def MakeTempTbl():
    start1 = 0
    stop1 = 101
    incr1 = 5
    print("Celsius", "Fahrenheit")
    print("-------","----------")
    for CelsTemp in range(start1,stop1, incr1):
        FahrTemp = (CelsTemp * 9 / 5 ) + 32
        print(str(CelsTemp).center(7,' '), str(FahrTemp).center(10))  
        
    return()
 
  	
MakeTempTbl()    