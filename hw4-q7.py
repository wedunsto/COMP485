#Objective:
#Perform user selected mathematical functions

from Addition import Addition #Import Addition function from module
from Subtraction import Subtraction #Import Subtraction function from module
from Multiplication import Multiplication #Import Multiplication function from module
from Division import Division #Import Division function from module

print("1.Add\n2.Subtract\n3.Multiply\n4.Divide") #Print the menu
userChoice = int(input("Enter your choice(1/2/3/4): ")) #Store the user operation

while userChoice > 4:
	userChoice = int(input("Enter your choice(1/2/3/4): ")) #Store the user operation

userFirstNumber = int(input("Enter first number: ")) #Store the first user entered number
userSecondNumber = int(input("Enter second number: ")) #Store the second user entered number

if userChoice == 1: #If the menu choice is 1
	print("{0} + {1} = {2}".format(userFirstNumber, userSecondNumber, int(Addition(userFirstNumber, userSecondNumber)))) #Print the sum of the user numbers
if userChoice == 2: #If the menu choice is 2
	print("{0} - {1} = {2}".format(userFirstNumber, userSecondNumber, int(Subtraction(userFirstNumber, userSecondNumber)))) #Print the difference of the user numbers
if userChoice == 3: #If the menu choice is 3
	print("{0} * {1} = {2}".format(userFirstNumber, userSecondNumber, int(Multiplication(userFirstNumber, userSecondNumber)))) #Print the product of the user numbers
if userChoice == 4: #If the menu choice is 4
	print("{0} / {1} = {2}".format(userFirstNumber, userSecondNumber, int(Division(userFirstNumber, userSecondNumber)))) #Print the quotient of the user numbers
