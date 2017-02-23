number=int(raw_input("Enter a number: "))
mood=str(raw_input("Enter your mood: "))
if(number>=5 and number<=25):
	print("In Range")
if(mood=="good" or mood=="Good" and number<5 and number>25):
	print(":-O")