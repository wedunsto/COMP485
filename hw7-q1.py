#Objective: Make a calculator class that adds, subtracts, multiplies, and divides any number of numbers

class Calculator():
	"This is a calculator class for any number of digits"

	def add(self,*inputValues):
		result = inputValues[0]
		for x in range (1,len(inputValues)):
			result += inputValues[x]
		print(result)

	def sub(self,*inputValues):
		result = inputValues[0]
		for x in range (1,len(inputValues)):
			result -= inputValues[x]
		print(result)

	def mult(self,*inputValues):
		result = inputValues[0]
		for x in range (1,len(inputValues)):
			result *= inputValues[x]
		print(result)

	def div(self,*inputValues):
		result = inputValues[0]
		for x in range (1,len(inputValues)):
			try:
				result /= inputValues[x]
			except ZeroDivisionError as e:
				print("Error: Division by zero is not defined! Fetching next number ...")
		print(result)

if __name__ == "__main__":
	calc = Calculator()
	calc.add(1,-2,3,8,0.32,-5)
	calc.sub(1,2,3,10,-15)
	calc.mult(-1,-2,-3,6,9,71,10,-0.5)
	calc.div(0,-2,1,0,5)
