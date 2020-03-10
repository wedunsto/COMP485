#Objective:
#Create a function that counts the number of upper and lower case letters in a string

userString = input("Enter a string \n")

results = {'UPPER_CASE' : 0, 'LOWER_CASE' : 0} #Resulting dictionary

def CountUpperLowerCase(userString): #Define the function
	for letters in userString: #Loop through string
		if letters.isupper(): #If the letter is upper case 
			results['UPPER_CASE'] = results['UPPER_CASE'] + 1 #Increment the appropriate counter
		elif letters.islower(): #If the letter is lower case
			results['LOWER_CASE'] = results['LOWER_CASE'] + 1 #Increment the appropriate counter

CountUpperLowerCase(userString) #Call the function

print(results) #Print results
