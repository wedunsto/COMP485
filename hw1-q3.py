#William Dunston
#02/02/2020
#Homework 1 question 3

UserInput = input("Please eneter a string: ")
Iterate = UserInput[0]
Iterations = int(UserInput.count(Iterate))
print("\'{}\' has been repeated {} times".format(Iterate,Iterations))
print(Iterate+UserInput[1:].replace(Iterate,"*"))
