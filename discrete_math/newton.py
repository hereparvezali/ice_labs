def equ(x):
	return x*x-3*x+2
def dequ(x):
	return 2*x-3

errlimit=float(input("Enter the err limit: "))
x=float(input("assumed initial value: "))
y=equ(x)
while abs(y)>errlimit:
	x=x-equ(x)/dequ(x)
	y=equ(x)
print("The approximate root: ",x)
