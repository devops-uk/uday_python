#Syntax 
#lambda arg:exp


# def add(a,b):#function definition
#     return a+b #function body
# obj = add(10,10)
# print(obj)

# result = lambda a,b:a+b
# print(result(10,10))


# result = lambda num_1,num_2: num_1 * num_2
# print(result(5,2))
# print(result(5,4))
# print(result(5,6))
# print(result(10,2))


# list_1 = [1,2,3,4,5,6,7,8,9,10]
# empty_list = []
# for i in list_1:
#     if i%2==0:
#         empty_list.append(i)
# print(empty_list)

# def even(i):
#     return i%2==0
# print(even(8))

#syntax
#filter(function,iterable)
# list_1 = [1,2,3,4,5,6,7,8,9,10]
# def even(i):
#     return i%2==0
# obj = filter(even,[1,2,3,4,5,6,7,8,9,10])
# print(list(obj))

#lambda arg:exp
#filter(function,iterable)
# obj = filter(lambda i:i%2==0,[1,2,3,4,5,6,7,8,9,10])
# print(list(obj))


# list_1 = [1,2,3,4,5,6,7,8,9,10]
# empty_list = []
# for i in list_1:
#     square = i**2
#     empty_list.append(square)
# print(empty_list)

#Syntac	
# map(function, iterable, ...)
# list_1 = [1,2,3,4,5,6,7,8,9,10]
# def square(i):
#     return i**2
# obj= map(square,[1,2,3,4,5,6,7,8,9,10])
# print(list(obj))

# map(function, iterable, ...)
#lambda arg:exp
# obj = map(lambda i:i**2,[1,2,3,4,5,6,7,8,9,10])
# print(list(obj))


# from functools import reduce
# reduce(function, iterable[, initializer])#initializer--optional

# def add(a,b,c,d,e):
#     return a+b+c+d+e
# print(add(10,10,10,10,10))
# from functools import reduce
# def add(a,b):
#     return a+b
# obj = reduce(add,[1,2,3,4,5,6,7,8,9,10])
# print(obj)





"""
generator function --  a genetor -function is defined like a normal function
but whenever its need to generate a value
it does so with the yeild keyword rather than return
if body contain yield , the function  automatically
becomes a generator function.
"""


# def my_func():
#     yield 1  #pause or hold
#     yield 2  #pause or hold
#     yield 3  #pause or hold
# obj = my_func()
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())

# def numbers():
#     for i in range(1,1000):
#         yield i
# obj = numbers()
# for i in obj:
#     print(i)