(°F - 32) x 5/9 = °C 
Ask the user to enter the temperate in Fahrenheit
Convert the temperature from Fahrenheit to Celsius 
Display the temperature in both Fahrenheit and Celsius to the user.
Give the user the option of continuing the program or exiting.

'''

def Main():
	
	Line1 = " "
	while Line1 != "Done":
		Line1 = input("please enter Temp in Fahrenheit.  When Finished Enter Done")
		if Line1 == "Done":
			break
		else:
			FahrToCelsius(int(Line1))
			
def FahrToCelsius(FahrTemp):
	CelTemp = (FahrTemp - 32) * 5 // 9
	print("Fahrenheit", FahrTemp, "Celsius" , CelTemp) 

Main()
