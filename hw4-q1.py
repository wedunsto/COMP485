#Objective:
#Print out strings that match the requirements
userEnteredStrings = str(input("Enter a list of strings seperated by a space\n"))#Gets user strings
userEnteredPattern = str(input("Enter the pattern you are looking for\n"))#Gets the require sub-string

userStrings = list(userEnteredStrings.split(' '))#Store user entered strings in a list
userResults = list()#Store strings that follow pattern

followsPattern = lambda x,y,z : x.append(y) if z in y else False #lambda function to add to userResults


for words in userStrings: #Iterate through user entered words
    followsPattern(userResults,words,userEnteredPattern)#Calls the lambda function

print(userResults)#Prints out the results
