#William Dunston
#Homework 3: Question 1
#Objective:
#Print out the dictionary pair with the most even values

d1 = (2,4,6,8)
d2 = (0,-2,1,11,3)
d3 = (17,15,12,100,122)

d = {"l1" : d1, "l2" : d2, "l3" : d3} #Create dictionary 

evenCounter = []#List that keeps track of number of even numbers
index = 0#Keeps track of the index where the greatest number is in the evenCounter list

for values in d.values():#Traverse the dictionary 
	counter = 0#Reinstantiates the counter variable
	for num in values:#Traverse the tuple in the dictionary keys
		if num % 2 == 0:#If the value in the tuple is even 
			counter = counter + 1#Increment the counter
	evenCounter.append(counter)#When all values are traversed, add to the even counter list

index = evenCounter.index(max(evenCounter))#stores the index where the most even numbers key is

mostEven = list(d.keys())[index]#stores the key that has the most even numbers in the values

print("'"+mostEven+"'"+":"+str(list(d[mostEven]))+"----> "+str(max(evenCounter)))#prints out the format
