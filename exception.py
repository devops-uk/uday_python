# types of errors
# 1. syntax errors
# 2. runtime errors
# 3. logical errors ---> user need to be identified ( very difficult to find )

# a = 5
# b = 5
# c = a-b
# print(c)

# 1. syntax errors  --> compile time errors
# for i in iterable:
#     block of code


# for i in range(10):
#     print(i)



# 2. runtime errors  ---> which disturbs the flow of execution ( during the execution ) also called exceptions
# num_1= int(input("enter the number: "))
# num_2= int(input("enter the number: "))
# print(num_1 + num_2)
# try:
#     print(num_1 / num_2)
# except:
#     print("some error occured...")
# print(num_1 - num_2)




# list_1 = [1,2,3,4,5,6]
# print(list_1[0])
# try:
#     print(list_1[6])
# except:
#     print("some error occured")
# print(list_1[4])
# print(list_1[5])




# num_1= int(input("enter the number: "))
# num_2= int(input("enter the number: "))
# try:
#     print(num_1 + num_2)
#     print(num_1 / num_2)
#     print(num_1 - num_2)
# except:
#     print("some error occured")
# else:
#     print(num_1 ** num_2)


# try:
#     num_1= int(input("enter the number: "))
#     num_2= int(input("enter the number: "))
# except:
#     print("some error occured")
# else:
#     print(num_1 + num_2)
# finally:
#     print(num_1 / num_2)


# try:
#     num_1= int(input("enter the number: "))
#     num_2= int(input("enter the number: "))
# except Exception as e:
#     print(e)


# try:
#     print(10/0)
# except Exception as e:
#     print(f"ZeroDivisionError: {e}")



# try:
#     # code that might raise any exception
# except Exception as e:
#     print(f"Exception: {e}")




# github account creation 
# github linking to git