#!/usr/bin/env python
# coding: utf-8

# In[1]:


## higher order function ##
    


# In[8]:


#fuction as a Parameter

#normal function
def sum_numbers(nums):
    return sum(nums)


#fuction as a parameter    
def higher_order_function(f,lst):
    summation = f(lst)
    return summation
    
result = higher_order_function(sum_numbers,[1,2,3,4,5])

print(result)


# In[32]:


# working on it......
#sum = 1([1,2,3,4,5])
#print(sum)


# In[35]:


#function as a return value

def square(x):   # a sqaure function 
    return x ** 2

def cube(x):     # a cube function
    return x ** 3

def absolute(x):
     if x >= 0:
            return x
     else:
        return -(x)


def h_o_f(type): # higher order function
    
    if type == "square":
       return square
    
    elif type == "cube":
        return cube
    
    elif type == "absolute":
        return absolute
    
# all results   
result = h_o_f("square")
print(result(3))

result = h_o_f("cube")
print(result(3))
    
result = h_o_f("absolute")
print(result(3))
    


# In[37]:


# python Closures
# a nested function to access the outer scope of the enclosing function

def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))
print(closure_result(10))


# In[41]:


#python Decorators

#A decorator is a design pattern in python that allow a user to add new fuctionality to an existing object without modifying its strucher. Decorators are usually called the before the difinition of a function you want to decorate.


# creating a Decorators
# TO creat a decorator function , we need an outer fuction with an inner wrapper function




#NORMAL FUNCTION

def greeting():
    return "Welcome to python"

def uppercase_decoration(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

g = uppercase_decoration(greeting)
print(g())




# DECORATOR FUNCTION 
#This decorator function is a higher order function that takes a function as a parameter

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@uppercase_decorator
def greeting2():
      return "welcome to decorated python"
    
print(greeting2())
    


# In[44]:


#Applying Multiple Decorators to a Single Function


#first decoratorab
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

@split_string_decorator
@uppercase_decoration
def greeting():
    return "hello iam from decorated functions"

print(greeting())


# In[48]:


# Accepting Parameter in Decorator function

def dec_with_parameter(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
         
            
    return wrapper_accepting_parameters     
             
            
@dec_with_parameter
def print_full_name(first_name, last_name, country):
    print("I am {} {}. l love to learning.".format(first_name, last_name, country))  
    
    
print_full_name("kazi","samir","Bangladesh")    



# In[62]:


# Built-in higher Order Function

# map() _filter_ _reduce_
#Lambda function


# Map function
#the map function is a built-in function that takes a function and iterable as parameters.
# map(function, iterable) [syntax]

"""
nums = [1,2,3,4,5] # iterable
def square(x):
   return x ** 2

num_square = map(square,nums)
#print(list(num_square))
print(list(num_square)) 
"""


numbers = [1, 2, 3, 4, 5] # iterable
def square(x):
   return x ** 2
numbers_squared = map(square, numbers)
print(numbers_squared)
#print(list(numbers_squared))


# applying with a lambda function

nums = [1,2,3,4,5]
num_square = map(lambda x:x ** 2, nums)
print(num_square)




nums_str = ['1','2','3','4','5'] #iterable
   
nums_int = map(int, nums_str)
print(nums_int)


names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable

def change_to_upper(name):
   return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# Let us apply it with a lambda function
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']


#What actually map does is iterating over a list. For instance, it changes the names to upper case and returns a new 


# In[70]:


#python filter function

numbers = [1,2,3,4,5]

def is_even(num):
    if num % 2==0:
        return True
    return False

even_number = filter(is_even,numbers)
print(list(even_number))




numbers = [1, 2, 3, 4, 5]  # iterable

def is_odd(num):
    if num % 2 != 0:
        return True
    return False

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))       # [1, 3, 5]



# Filter long name
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable
def is_name_long(name):
    if len(name) > 7:
        return True
    return False

long_names = filter(is_name_long, names)
print(list(long_names))         # ['Asabeneh']


# In[74]:


### Python - Reduce Function

#The _reduce()_ function is defined in the functools module and we should import it from this module. Like map and filter it takes two parameters, a function and an iterable. However, it does not return another iterable, instead it returns a single value.
#**Example:1**

numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15


# In[ ]:




