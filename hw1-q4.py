#William Dunston
#02/02/2020
#Homework 1 question 3

#Capture positive space seperated numbers from user
#Print LIST in descending order
#Print max digit and it occurence

Output = []

UserNumbers = input("Please enter positive numbers: ")
UserNumbers = UserNumbers.replace(" ","")
Output = list(UserNumbers)
list.sort(Output, reverse = True)

print(Output)
