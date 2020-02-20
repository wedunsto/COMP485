#William Dunston
#Homework 3: Question 3
#Objective:
#Return the indices of 2 elements whose values are equal to user entered value

userValues = str(input("enter the elements of a list\n"))
indexing = int(input("enter your desired integer\n"))

userList = []

for number in userValues:
	if(number != " "):
		userList.append(int(number))

print(userList)
print(indexing)

