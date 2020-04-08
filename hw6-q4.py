#Objective: Print out all comments in the Python file

import re

filePath = "./newfile.py" #Stores the data path to the text file

print("Assume the input python file has the following content:\n")

with open(filePath,'r') as file_reader: #Opens the file in read mode
	text = file_reader.read()
	commentedWords = re.findall(r"[#']*[^#']*[\n']+",text) #Finds all single and multi-line comments
print(commentedWords)

