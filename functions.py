#Syntax
# def funcname():
#     #block of code
#     #block of code

# def greet(): #function definition
#     print("this is sample function") #function body
# #syntax for function calling
# # functionname()
# greet()


# def add(): #function definition 
#     num_1 = 10
#     num_2 = 20
#     result = num_1 + num_2 #here performed addition
#     print(result)
# add() #function calling


# def details(user,id):#function defintion
#     print(user)
#     print(id)
# details("charan","1234")
# details(["vasu","kumar"],1234)

# def multiply(x, y): 
# 	print( x * y )
# multiply(3, 4) # Here, 3 and 4 are arguments

# def add(num_1,num_2): #function definition 
#     print(num_1 + num_2)
# add(10,10) #function calling


# def add(num_1,num_2): #function definition 
#     return num_1 + num_2    
# obj = add(10,10) #function calling
# print(obj*2)


# def details(user=None,dept=None,id=None):
#     print(user,dept,id)
# details("charan","fe",1234)
# details("indra","be")
# details("harsha")
# details()


#arbitary arguments--> function can accept a variable number of arguments by using *args(syntax)
# def my_func(*a):
#     print(a)
# my_func(1,"vasu","kumar",[1,2,3])

# # * ---> all  (tuple)


#keyword arguments :-->keyword arguments are passed to a function with a keyword and a value, allowing for more explicit parameter passing
# def myfunc(**a):
#     print(a)
# myfunc(a=1,b=2,c=3)

# *--> tuple
# ** ---> dict

# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def expo(a,b):
#     return a**b


#variables  --> two types ---> local variables ---> global variable
#1. local variable ---> function ( inside the function)

# def sample():
#     num_1 = 10
#     num_2 = 20
#     print(num_1+num_2)
#     print(num_1 * 10)
#     print(num_2 * 10)
# sample()


# balance = 1000 #global variables
# def credit(amount):
#     print(amount)
#     print(balance)
# credit(500)
# print(balance)



"""
Local and Global Variables in Python
Local Variable:
A variable declared inside a function and accessible only within that function is called a local variable.
Example:
def greet():
    name = "John"  # Local variable
    print("Hello", name)
greet()
# Output: Hello John
Global Variable:
A variable declared outside of all functions and accessible throughout the program, including inside functions, is called a global variable.
Example:
name = "John"  # Global variable
def greet():
    print("Hello", name)
greet()
# Output: Hello John
Modifying a Global Variable Inside a Function
To modify a global variable within a function, use the global keyword.
Example:
count = 10  # Global variable
def update_count():
    global count  # Access and modify the global variable
    count += 5
    print("Count inside function:", count)
update_count()
print("Count outside function:", count)
# Output:
# Count inside function: 15
# Count outside function: 15
Key Points:
    Local variables are limited to the function scope.
    Global variables are accessible throughout the program but can only be modified inside a function if declared as global.

"""










# balance = 500
# def credit(amount):
#     global balance
#     balance +=amount
#     print(balance)
# credit(1000)
# print(balance)

# def debit()


# def balance()
    





# without functions source code

#functions re-write