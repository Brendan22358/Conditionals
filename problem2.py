print("Your going to input three integers, and going from 1 to 3 if it is going up then its going to return Up and rysing, if its going down, falling down\n and if the middle is the biggest it's going to return over the mountain, lastly if the middle is the smallest it's going to return in the dog house.")
a1=int(raw_input("#1="))
a2=int(raw_input("#2="))
a3=int(raw_input("#3="))
if(a1<a2<a3):
	print("Up and risying")
elif(a1>a2>a3):
	print("Falling down")
elif(a1<a2>a3):
	print("Over The Mountain")
elif(a1>a2<a3):
	print("In the dog house")
else:
	print("Error, #'s can not be the same, #'s must be integers.")
