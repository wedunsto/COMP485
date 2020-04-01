#Objective:
#Read a file line by line and return list of all compound words seperated by underscore
import re

filePath = "./Example.txt" #Stores the data path to the text file
result = ""

print("Assume you have a text file with the following content:\n")

with open(filePath,'r') as file_reader: #Opens the file in read mode
	text = file_reader.read()
	compoundWords = re.findall(r"\S{1,}-\S{1,}",text) #Finds all words seperated by a '-'

print(text)
print()
for words in compoundWords:
	result += words+" "
print("Your script needs to return "+result)
