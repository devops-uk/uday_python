# # Creating strings
# single_quoted_string = 'Hello, World!'
# double_quoted_string = "Python Strings"
# triple_quoted_string = '''Triple quotes allow
# strings to span multiple lines.'''
# print(type(single_quoted_string))
# print(type(double_quoted_string))
# print(type(triple_quoted_string))

# sample = str()
# print(type(sample))

# my_string = "Python"
# print(my_string[5])
# print(my_string[0])
# print(my_string[-2])

# my_string = "Python"
# #seq[s:s:s]
# print(my_string[1:5])
# print(my_string[0:6])
# print(my_string[::])
# print(my_string[::-1])

# user = "mahesh ravuri"
# print(user[7])
# print(user[5:9])

# user = "mahesh ravuri"
# caps = user.upper()
# print(caps)

# user = " mahesh MAHESH RAVURI 123456 @"
# low = user.lower()
# print(low)

# password = "Vasu@1234"


# sentence = "This is a sample sentence."
# count_i = sentence.count('sample')
# print(count_i) 

# whitespace_string = "   This is a string with leading and trailing whitespace.   "
# print(len(whitespace_string))
# stripped_string = whitespace_string.strip()
# print(len(stripped_string))

# data = "Pythonlife,Kiran,123456"
# data1 = data.split(',')
# print(data1)

# original_string = "Python is fun!"
# modified_string = original_string.replace('fun', 'awesome')
# print(modified_string) 
# print(original_string)
# modified_string_2 = modified_string.replace("Python","pythonlife")
# print(modified_string_2)


# filename = "example.txt"
# starts_with = filename.startswith("ex")
# ends_with = filename.endswith(".txt")
# print(starts_with)  
# print(ends_with) 




# email_list = ["example1@gmail.com", "example2@yahoo.com", "example3@gmail.com", "example4@hotmail.com","example5@outlook.com"]
# empty_list = []
# for i in email_list:
#     if i.endswith("@gmail.com"):
#         empty_list.append(i)
# print(empty_list)


#[exp for i in iterable if condition]
# result = [i for i in email_list if i.endswith("@gmail.com")]
# print([i for i in email_list if i.endswith("@gmail.com")])
# print([i for i in ["example1@gmail.com", "example2@yahoo.com", "example3@gmail.com", "example4@hotmail.com","example5@outlook.com"] if i.endswith("@gmail.com")])






# sentence = "This is a sentence."
# # position_a = sentence.find('vasu')
# position_i = sentence.index('vasu')
# # print(position_a) 
# print(position_i) 

# text = "python programming language"
# capitalized_text = text.capitalize()
# print(capitalized_text) 

# numeric_string = "12345"
# alpha_string = "Python"

# is_numeric = numeric_string.isdigit()
# is_alpha = alpha_string.isalpha()

# print(is_numeric)  
# print(is_alpha)  

# word_list = ['Hello', 'World']
# joined_string = ' '.join(word_list)

# print(joined_string)


