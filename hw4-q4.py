#Objective:
#Create a function that counts the number of upper and lower case letters in a string

results = {'Upper_Case' : 0, 'Lower_Case' : 0} #Resulting dictionary

def CountUpperLowerCase(userString): #Define the function
	for letters in userString: #Loop through string
		if letters.isupper(): #If the letter is upper case 
			results['Upper_Case'] = results['Upper_Case'] + 1 #Increment the appropriate counter
		elif letters.islower(): #If the letter is lower case
			results['Lower_Case'] = results['Lower_Case'] + 1 #Increment the appropriate counter

CountUpperLowerCase(userString) #Call the function

print(results) #Print results
