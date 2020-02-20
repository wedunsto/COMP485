#William Dunston
#Homework #2: Question #2

sentence = input("Type a sentence:\n")#store the user entered sentence
letter = input("What letter are you looking for?\n")#store the user entered letter

words = sentence.split()#split all the words in the sentence into list entries

total = 0#keeps track of how many times the letter repeats in the whole sentence

for individuals in words:#traverse the list
	if letter in individuals:#if the letter being searched is in a word
		count = individuals.count(letter)#Count how many times the letter appears
		total += count
		results = "'{}' has {} '{}'".format(individuals,count,letter) #designs the desired output
		print(results)#print out the results

final = "Totally, there are {} '{}'(s) in your sentence.".format(total,letter)#designs the desired output
print(final)#prints the final result
