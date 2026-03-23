#syntax
# class classname():
    #class body


# class january():#class definition
#     name = "kiran" #attributes
#     name_2 = "charan" #attributes
#     def details(self):#methods
#         print("this is class methods")
#         print(self.name)
#     def details_1(self):#methods
#         print("this is class method 2")
#         self.details()
# #syntax
# #objectname = classname()
# obj = january()
# # print(obj.name)
# # print(obj.name_2)
# # obj.details()
# obj.details_1()





# class Mobiles():
#     brand_name = "Samsung"
#     brand_color = "white"
#     storage = "128GB"
#     def calling(self,brand):
#         print("you are calling...!!",brand)
#     def camera(self):
#         print("capturing photo....")
#     def browsing(self):
#         print("you are browsing..")
#         self.calling("oppo")
# #objectname = classname()
# samsung = Mobiles()
# print(samsung.brand_name)
# samsung.calling("samsung")
# # samsung.browsing()
# # samsung.camera()
# apple = Mobiles()
# apple.calling("apple")
# oppo = Mobiles()
# oppo.calling("oppo")
# oppo.browsing()


# class car():
#     def __init__(self,bn,color,model):
#         self.bn = bn
#         self.color = color
#         self.model = model
#     def driving(self):
#         print("you are driving",self.bn)
#     def engine(self):
#         print("start/off")
# tata = car("tata","white",2024)
# mahendra = car("mahendra","black",2023)
# tata.driving()
# mahendra.driving()

# class atm():
#     def __init__(self,bn):
#         self.bn = bn
#     def credit(self):

#     def withdraw(self):

#     def bal(self):

# sbin = atm("sbin")
# sbin.credit()

# Write a Python function square_all(numbers) that takes a list of numbers as input and returns a new list containing the square of each number in the input list. Use the map() function with a lambda function to implement this.
# numbers = int(input("enter the number:"))
# obj = map(lambda i:i**2,list(numbers))
# print(list(obj))


# def square_all(numbers):
#     return list(map(lambda x:x**2,numbers))
# user = input("enter numbers:")
# numbers = list(map(int,user.split()))
# square = square_all(numbers)
# print(square)



















