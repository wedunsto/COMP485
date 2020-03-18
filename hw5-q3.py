#Objective:
#Find the longest word in each line
#Store the longests words in a seperate file

userPath = input("enter a path to a text file")
with open(userPath, 'r') as file_reader:
	fileLines = file_reader.readline()
