print("Enter three integers")
a=int(raw_input("a="))
b=int(raw_input("b="))
c=int(raw_input("c="))
print("If any of the two integers add up it will print true, if not it will print false.")
if(a+b==c):
	print("True")
elif(a+c==b):
	print("True")
elif(c+b==a):
	print("True")
else:
	print("False")
