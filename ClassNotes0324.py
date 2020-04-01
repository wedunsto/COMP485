# Class Notes Mar. 24
# Regular Expressions
# Regex is a sequence of characters that define a search pattern
# import re
# Match(): attempts to match RE pattern to string with optional flags
# Match() only looks at the beginning of a string
# re.match(pattern,  string, flags = 0):
# Returns a match object on success and none on failure
import re

mystr = 'You can learn any programming language, whether it is Python2, Python3, Perl, Java,Javascript, or PHP.'
match1 = re.match("You", mystr)  # At the beginning of the string, case sensitive
match2 = re.match("you", mystr, re.I)  # Ignores case sensitivity
match3 = re.match("it", mystr)  # Even though this is in the string it is not in the beginning, no match
print(type(match1), type(match2))

# group(): refers to a group of patterns i.e. : telephone numbers, AND email addresses
print(match1.group())  # Prints "You"
print(match2.group())  # Still prints "You" capital 'Y'

# Search(): More sophisticated version of match()
# re.search(pattern, string, flags = 0)

# Patterns:
# r: raw string: put this before defining the pattern, avoid python interpreter conflict
# (): defines the beginning and end of a group
# A-Za-z 0-9: ordinary characters - just match themselves exactly
# .^ $ * + ? {[] \ | (): Meta-characters - special meanings
# .: matches any single character except \n
# ^= start, $= end - matches the start or end of a string
# \w - match a word character: a letter or digit or underbar
# \W = matches any non-word character
# \s - matches a single whitespace character - space, newline, return, tab (\n\r\t
# \S - any non white space character
# \t\n\r - tab, newline, return
# \d - decimal digit [0-9]
# \D - any non decimal digit
# \: inhibit the specialness of a character
# []: indicate a set of chars, i.e: [abc] matches 'a' or 'b' or 'c'
# [a-z]: range of matches
# [^ab]: anything except 'a' or 'b'
# [abc-]: dont care what follows but much have 'a' or 'b' or 'c'
# +: 1 or more occurrences of the pattern to its left. i.e. 'i+' = one or more i's
# *: 0 or more occurrences of the pattern to its left
# ?: matches 0 or 1 occurrences of the pattern to its left
# {m,n}: m to n (both inclusive)
# {m}: exactly m times

# arp break down:
# r: raw input to avoid conflict
# first group refer to ip address
# (.)+ dont have a new line
# (.+) + not just a sequence of numbers. but the plus will continue until 1 or more white space we dont want that
# (.+?) when finished with ip address stop
# (\d) expect digits in a group
# (.+?) sequence of A-Za-z 0-9 ,./;', etc. no new line
# \s: whitespace
# \s{2,} 2 whitespace until you stop
# \w: anything
# (\w)*: capture anything with any repetition
# print(match.group()) returns all the groups in a tuple
# print(match.group(i)) returns just the desired group

# findall(): most useful function in re module
# finds all the matches and returns them as a list of strings, with each string representing one match
# re.findall(pattern, string, flags = 0)
