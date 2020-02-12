#William  Dunston
#Homework 2: Question 1

diamond = int(input("Please enter an odd integer: "))+1 #Used to collect the odd integer
start = int(diamond / 2) #Keeps track of the halfway point to print the spaces
stop = start + 1#Keeps track of the second halftway point to print the 

star = "" #Creates the string that wil hold the final diamond

for stars in range(diamond): #Populate the output string with stars
	star += "*"

#starts to iteratively build the diamond

for stars in range(int(diamond/2-1)): #Indexes for first half of the diamond
	print(star[:start].replace("*"," ")+star[start:stop]+star[stop:].replace("*"," ")) #Builds the first half of the diamond
	start -= 1 #reduce start by 1
	stop += 1 #increase stop by 1

i = 2
j = diamond-1
for stars in range(int(diamond/2)-2): #Indexes for last half of the diamond
	i += 1
	j -= 1
	print(star[:i].replace("*"," ")+star[i:j]) #Builds the second half of the diamond
