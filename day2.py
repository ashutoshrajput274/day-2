# Anonymous functions (Lambda)
#* They are defined using the keyword .
#* They can take several argument but can only have one expression.

'''a = lambda b: b + 4
print(a(4))

#output is : 8

c =lambda d,e : d + e
print(c(7,8))

# output is: 15

def ghost_number(n):
    return lambda f : f * n
ashu = ghost_number(2)
print(ashu(20))'''

#-----------------------------------------------------------------------
# What are decorators ?
# decorators are user to add new functionality to exiting objects like functions, method and classes without modifying its structure .
 
'''def my_decorator(function):
    def wrapper():
        my = function()
        convert_uppercase =my.upper()
        return convert_uppercase
    return wrapper
@my_decorator
def say_hello():
    return "hello world"
#decorate = my_decorator(say_hello)
print(say_hello()) '''
#------------------------------------------------------------------------
# what are data structure ?
# they structure which can hold some data together.
# they are used to store a collection of related data.
# python has the following built in data structure.
# List
# Tuple
# set 
# dictionary

# what is list ?
# A list is a collection of data which can be mixed type.
# items in a list are ordered by their index and changeable.
# list are created with square brackets.[]
# item in a list can assessed by their index.
# Each item in a list is separated by a comma .

# Creating a list 
'''friends =["ashu","mahindra","puspa","radhe","surya"]
for x in friends:
    print(x) # output : All name is print one by one.

print(friends)'''    # output : same list print

# Accessing Element of list 
# A can be accessed using their index or position in the list.
# the index is zero based. first element has a position of zero.
 
'''ashu =["ashu","yash","mahi","chiku"]
print(ashu[0]) # output: ashu

ashu =["ashu","yash","mahi","chiku"]
print(ashu[-1]) # output : chiku

ashu =["ashu","yash","mahi","chiku"]
print(ashu[1:]) # output: ['yash','mahi','chiku']

ashu =["ashu","yash","mahi","chiku"]
print(ashu[1:3]) #output: ['yash','mahi']

ashu =["ashu","yash","mahi","chiku"]
print(ashu[0:])
ashu[0] = "singh"
print(ashu) #output: ['singh', 'yash', 'mahi', 'chiku']'''

# extend() method --> Used to append or join list contents.

'''fruits = ["berries","apples","grapes","oranges"]
vegetables = ["kale","broccoli","lettuce"]

fruits.extend(vegetables)
print(fruits)''' # output : ['berries', 'apples', 'grapes', 'oranges', 'kale', 'broccoli', 'lettuce']

# append() method : -->  add an item to the end of the list.
'''fruits = ["berries","apples","grapes","oranges"]
fruits.append("banana")
print(fruits)''' #output : ['berries', 'apples', 'grapes', 'oranges', 'banana']

# sort() method --> orders list items. Ascending or descending

'''fruits = ["berries","apples","grapes","oranges"]
fruits.sort()
print(fruits) '''#output : ['apples', 'berries', 'grapes', 'oranges']

# count() method --> 

'''numbers =[1,2,3,5,2,5,55,515,1,15,]
print(numbers.count(2))''' # output : 2

# index() method --> index method se ham hamari value kis position par hai jaan sakte hai agr same name ki 
# value ya no ho to jo sabse pahle aati hai vo show ho jati hai 

'''numbers =[1,2,3,5,2,5,55,515,1,15,]
print(numbers.index(2)) ''' # output : 1 (2 kis index no par hai vo show hota hai)

# insert method --> basically insert add karne ka kam hi karta hai jis bhi jagah par jo bhi add karna ho to index no likh to do then "me value"

'''fruits = ["berries","apples","grapes","oranges"]
fruits.insert(0,"banana")
print(fruits)''' # output : ['banana', 'berries', 'apples', 'grapes', 'oranges']

# pop () method --> removes the last item from the list . but aapko list ke center se item remove karna hai to pop method me ()
# ke ander index value likhna padega vo us index par jo bhi item hoga usko hata dega ..

'''fruits = ["berries","apples","grapes","oranges"]
fruits.pop()
print(fruits)''' # output : ['berries', 'apples', 'grapes'] 

# remove() method --> Removes specified item from a list.

'''fruits = ["berries","apples","grapes","oranges"]
fruits.remove("apples")
print(fruits)''' #output : ['berries', 'grapes', 'oranges']

# del () method --> deletes list
'''fruits = ["berries","apples","grapes","oranges"]
del fruits
print(fruits)''' #output : nameError fruits is not define 

#----------------------------------------------------------------------------------------------

# what is a tuple ?
# A tuple is a list that can not be changed.(immutable)
# can be created using parenthesis.() and with a constructor.
# Element in a tuple can be accessed by their index .

# Creating a tuple with parenthesis.
 
# fruits = ("apples","banana","mango","cherry")

# lopping through tuple using a for loop

'''fruits = ("apples","banana","mango","cherry")
for x in fruits:
       print(x)'''
# print(fruits[2])

# Creating a tuple with a tuple constructor
'''animals = tuple(("lion","tiger","bear"))
#print(animals)
print(len(animals))'''

#-----------------------------------------------------------
# What is a python Set ?
# A set is a collection of value..
# Values in a set are not ordered.
# values in a set are not indexed.
# you can add values yo a set but not change values.

# how to create a set 
'''fruits ={"grapes","apples","berries"}
for x in fruits:
    print(x)'''
# basically constructor is a specially type of function

# Built in set method
# add()-> adds an element to a set.
# update() -> adds multiple element to a set.
# clear() -> removes all the element in a set 
# discard()-> removes a specified element or item.
# remove()-> removes a specified item from the set.
# del ()-> deletes the set.

# fruits = {"grapes","apples","berries"}
# animals =(("lion","tiger","bear"))
# fruits.add("banana")
# print(fruits)
# fruits.update(["mango","kiwi"])
# print(fruits)
# fruits.remove("kiwi")
# print(fruits)
# fruits.clear()
# print(fruits)
# ---------------------------------------------------------------

# What is a python dictionary 

# A dictionary is a collection of key value pairs.
# the values can be changed (mutable).
# The values have unique keys.
# you can store mixed data type.

# how to create a dictionary 

'''my = {
    "brand":"range rover",
    "model":"hse",
    "year":2017
}
print(my)

# how to create a dictionary with a constructor()

green = dict(fruits="green apples",vegetables = "kale")
print(green)'''

# Built-in dictionary methods 

# get() --> returns the value of specified key.
# Update()--> insert a specified ake:value pair in dictionary
# clear()--> Removes all key:value pair in dictionary
# keys()--> Return a list of dictionary keys.
# values()--> Returns a list of dictionary values. 
# pop() --> removes item
# clear() --> clear all
# del()--> del dict
'''my = {
    "brand":"range rover",
    "model":"hse",
    "year":2017
}'''
# print(my.get("brand")) # output : range rover
# my.update({"color":"silver"})
# print(my) # output: {'brand': 'range rover', 'model': 'hse', 'year': 2017, 'color': 'silver'}

# b = my.keys()
# print(b) # output : dict_keys(['brand', 'model', 'year'])
