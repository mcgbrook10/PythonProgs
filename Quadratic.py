
def Main():
    print("This Program solves an equation in the form AX^2 + BX + C. Please Enter the following Values.")  
    a=int(input("What is the Value of A"))
    b=int(input("What is the Value of B"))
    c=int(input("What is the Value of C"))
    x=int(input("What is the Value of X"))
    QuadTotal = (a * (x**2)) + (b * x) + c
    print("This is the Equation you Entered: " + constfmt(a) + "X^2 " + sign(b) + " " + constfmt(b) + "X " + sign(c) + " " + str(c))
    print("The value of the Equation is: " + str(QuadTotal))
    return()

   
def constfmt(quadvar):
	if quadvar == 1:
		return ""
	else:
		return str(quadvar)
		
def sign(quadvar):
	if quadvar >= 0:
		return "+"
	else:
		return ""
		
Main()	