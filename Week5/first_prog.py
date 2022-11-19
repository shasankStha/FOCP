# taking input from user and storing it in number
number = input("Enter a number: ")
# converting type of data to integer
number = int(number)
# printing the entered number
print("The numbered entered was", number)
# checking whether the number is odd or even. If condition meets, if will execute, if not else will execute.
if (number % 2) == 0 and (number %10) == 0:
	print("That is an even number and divisible by 10")

elif(number % 2)==0:
    print("That is an even number")
else:
	print("That is an odd number")