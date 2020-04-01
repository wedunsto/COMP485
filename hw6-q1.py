#Objective:
#Remove excessive white space between words in a string

import re #import the module that deal with regular expressions
userString = input("Enter a sentence with extra spaces between words:\n")#Stores user entered string
print("The sentence after removing white spaces is:\n")

test = re.findall(r"\S{1,}\s{0,1}",userString)

for words in test:
	print(words,end="")
print()
