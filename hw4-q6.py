#Objective:
#If the cube of an integer in the original list is in the original list, print the number

from math import pow #Get the power function from the math class

original_list = [-2,1,13,4,2,36,7,5,100,-8,71,26,8,64,125] #Original list
result_list = [] #list that holds the results
FindCube = lambda x,y,z : z.append(x) if pow(x,3) in y else False #Lambda function to find the cubes

for number in original_list: #Iterate through the original list
	FindCube(number,original_list,result_list) #Call the lambda function
	
print(result_list) #Print results
