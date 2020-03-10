#Objective:
#Calculate the fibonacci sequence of user entered number
#Calculate the number of functioncals

userNumber = int(input("Enter an integer\n")) #Stores the user entered number
functionCalls = 1 #Stores the number of function calls

def FibonacciSequence(userNumber): #Defines the function that will calculate the fibonacci sequence and number of function calls
	if(userNumber < 2): return userNumber #if userNumber is 1 or 0 return 1 or 0
	global functionCalls #Points to global variable
	functionCalls = functionCalls + 2 #Increments the function calls counter when the function is called
	return FibonacciSequence(userNumber - 1) + FibonacciSequence( userNumber - 2) #return f(n-1) + f(n-2)

fibonacciResults = FibonacciSequence(userNumber) #Stores the fibonacci sequence results

print("fibonacci[{0}] = {1}. It has been calculated with {2} function call(s)".format(userNumber,fibonacciResults,functionCalls)) #Prints results

