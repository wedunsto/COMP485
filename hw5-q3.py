#Objective:
#Find the longest word in each line
#Store the longests words in a seperate file

userPath = input("enter a path to a text file\n") #Store datapath
maxWordLengths = [] #Create a list that will hold all the longest words in each line
with open(userPath, 'r') as file_reader: #Opens the text file
		fileLines = file_reader.read().split('\n') #Stores each line in its own list element

for parts in fileLines: #Iterates over the lines
	if len(parts) > 0: #Omits the spaces
		words = parts.split() #Splits each line word by word
		maxWordLengths.append(max(words, key = lambda word : len(word))) #Stores the largest word per line in a list

staticPath = "./result.txt"

with open(staticPath, 'w') as file_writer: #Opens the destination file
	for largestWords in maxWordLengths: #Iterate through the list
		file_writer.write(largestWords+" ") #Stores the largest words in a new file
