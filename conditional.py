# Syntax:
# if condition:
#      statement 1
#      statement 2
#      statement n

age = 16
if age>=18:
    print("you are eligible to vote")
    print(f"you'r age is {age} years old")
print("this is outside of block of code")
        
# number = 6
# if number > 5:
#     # Calculate square
#     print(number * number)
# print('Next lines of code')



#else
# if condition: ---> #False
#     #block of code
# else:
#     #alternative block of code 


# age = 17
# if age>=18:
#     print(f" you are eligible to vote {age}")
# else:
#     print(f"you are not eligible to vote ")
#     print(f"you'r age is {age}")



# user_name = input("enter username: ")
# password = input("enter the password: ")
# if user_name == "harsha" and password == 1234:
#     print("login success")
# else:
#     print("invalid credentials")



# Syntax:
# if condition-1:  
#      statement 1 
# elif condition-2:
#      stetement 2 
# elif condition-3:
#      stetement 3 
#      ...         
# else:            
#      statement


#grade system checking..........
# marks = int(input("enter the marks: "))
# if marks >= 90 and marks <=100:
#     print(f"you got A grade you obtained {marks} marks.")
# elif marks>=80:
#     print(f"you got B grade you obtained {marks} marks.")
# elif marks>=70:
#     print(f"you got C grade you obtained {marks} marks.")
# elif marks>=60:
#     print(f"you got D grade you obtained {marks} marks.")
# elif marks>=35:
#     print(f"you got PASS grade you obtained {marks} marks.")
# else:
#     print(f"you are failed you obtained {marks} marks")


# Syntax:
# if condition1:
#     # code block for condition1
#     if condition2:
#         # code block for condition2
#     else:
#         # code block for condition2 being false
# else:
#     # code block for condition1 being false



# user_name = input("enter username: ")
# password = input("enter the password: ")
# if user_name == "harsha" and password == 1234:
#     print("login success")
# else:
#     print("invalid credentials")



# user_name = input("enter username: ")
# password = input("enter the password: ")
# if user_name == "kumar":
#     if password == "1234":
#         print("Login success")
#     else:
#         print("invalid password")
# else:
#     print("invalid username")



# Syntax:
# result = value_if_true if condition else value_if_false

# age = 17
# if age>=18:
#     print(f" you are eligible to vote {age}")
# else:
#     print(f"you are not eligible to vote ")

# print("you are eligible to vote") if 18>=18 else print("not elgible")


# number = int(input("enter the number: "))
# if number%2 == 0:
#     print(f"{number} is even ")
# else:
#     print(f"{number} is odd ")

# print(f"{number} is even \t next line , \n next line",) if number%2==0 else print(f"{number} is odd")



#  Input from user
# principal = float(input("Enter the principal amount: "))
# rate = float(input("Enter the rate of interest (in %): "))
# time = float(input("Enter the time period (in years): "))

# # Calculate Simple Interest
# SI = (principal * rate * time) / 100
# print(f"Simple Interest: {SI}")