#Objective:
#Store a user-defined datapath and integer
#Print the first n lines in the text file at the datapath

userInteger = int(input("enter an integer\n")) #Stores the user-defined integer
userPath = input("enter a path to a text file\n") #Stores the datapath

with open(userPath, 'r') as file_reader: #Opens the file at the datapath in read mode
	for lines in range (userInteger): #Increment to the user-defined integer
		print("line "+str(lines)+" is: "+file_reader.readline(), end = ' ') #Print the next line in the file
