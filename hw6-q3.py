#Objective: return URLs in a string

import re

userInput = input("Enter a string:\n")
urls = re.findall(r"http[s]{0,1}://www\.[A-Za-z 0-9 -]{0,}\.[a-z]{0,}",sudoInput)
print(urls)
