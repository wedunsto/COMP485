#William Dunston
#Homework 3: Question 2
#Objective:
#Return a dictionary that shows how many words start with a value
userSentence = str(input())
userSentence = userSentence.lower()

result = {}#Creates the dictionary

result["a"] = 0#Initializes the value associated to the key
result["e"] = 0#Initializes the value associated to the key
result["i"] = 0#Initializes the value associated to the key
result["o"] = 0#Initializes the value associated to the key
result["u"] = 0#Initializes the value associated to the key

words = list(userSentence.split(" "))#seperate all the words

for word in words:#traverse all words in the sentence
	if(word[0] == "a"):#if the word begins with this letter increment its value
		result["a"] = result["a"] + 1
	if(word[0] == "e"):#if the word begins with this letter increment its value
		result["e"] = result["e"] + 1
	if(word[0] == "i"):#if the word begins with this letter increment its value
		result["i"] = result["i"] + 1
	if(word[0] == "o"):#if the word begins with this letter increment its value
		result["o"] = result["o"] + 1
	if(word[0] == "u"):#if the word begins with this letter increment its value
		result["u"] = result["u"] + 1

print("result ="+str(result))
