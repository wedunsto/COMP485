#Objective:
#Sort a list of dictionaries by the price keys

car = [{'make':'Acura','year':2019,'model':'RDX','color':'Black','price':24700},{'make':'Buick','year':2014,'model':'Encore','color':'White','price':14200},{'make':'Ford','year':2016,'model':'Edge','color':'Brown','price':19900},{'make':'Lexus','year':2016,'model':'NX','color':'Red','price':28500}]#Creates the list of dictionaries

priceSort = lambda x : x['price']#Creates lambda function to sort by price

car.sort(key = priceSort)#Apply sort key function

print(car)#Print results
