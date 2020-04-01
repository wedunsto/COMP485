# Findall(): finds all the matches and returns them as a list of strings, each string = 1 match
# findall(pattern, string)
# Same special characters
import re
arp = '22.22.22.1  0  b4:a4:5a:ff:c8:45 VLAN#222   L'
# match = re.findall(r"\d\d\.\d{2}\.[0-9][0-9]\.[0-9]{1,3}", arp)  # finds the ip address
# shows how to do with different attempts
match = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", arp)  # finds the ip address
# \d{1,3}.: finds 1 to 3 # followed by a (.)
mystring = "I enjoy learning programming languages such as Python 3"
match = re.search(r"\S+", mystring)  # Returns I
match = re.search(r"\AI enjoy", mystring)  # I am looking for something that start with I enjoy
# If it is found, it will return the pattern stating that the pattern match was found
# Returns none if pattern not found
print(match.group())
