#Objective:
#Store a user-defined datapath and integer
#Print the last n lines in the text file at the datapath

userInteger = int(input("enter an integer\n")) #Stores the user-defined integer
userPath = input("enter a path to a text file\n") #Stores the datapath

with open(userPath, 'r') as file_reader: #Opens the file at the datapath in read mode
	fileList = file_reader.readlines() #Store file as an array
	lineCount = len(fileList)+1 #Number of lines in the file
	lastLines = lineCount - userInteger #Number of lines until the end of file is reached
	
	for lines in range (lastLines,lineCount): #Increment to userInteger
		print(f"line {lastLines} is : {fileList[lastLines-1]}") #print last lines
		lastLines += 1 #Increment to the next to last line
