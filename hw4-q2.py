#Objective:
#Sort a list of positive and negative integers, and strings
original_list = [-3,"Ford",12,7,0,"BMW",1,-11,"Honda",100]#Original list

original_strings = (filter(lambda x : isinstance(x,str), original_list))#List of strings in original list
original_numbers = (filter(lambda x : isinstance(x,int), original_list))#List of ints in original list

original_strings = list(original_strings)#Cast content as a list
original_numbers = list(original_numbers)#Cast content as a list

original_strings.sort()#Sort the strings
original_numbers.sort()#Sort the numbers

result = original_strings + original_numbers#Concatenate 

print(result)#Print results
