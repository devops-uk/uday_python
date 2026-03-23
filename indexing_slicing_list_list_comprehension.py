# list_1 = []
# print(type(list_1))

# list_1 = [1,"vasu",5.7,True,[1,2,3,4]]
# print(type(list_1))

# list_1 = list()
# print(type(list_1))

# my_list = [1, 2, 3, 'apple', 'banana']
# print(my_list[3])



# my_list = [10, 20, 30, 40, 50]
# #var[indexvalue]
# print(my_list[2])#30
# print(my_list[4])#50
# print(my_list[0])#50


# my_list = [10, 20, 30, 40, 50]
# print(my_list[-1])#50
# print(my_list[4])#50
# print(my_list[-3])#30
# print(my_list[-5])#10



# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# print(my_list[1:7])
# print(my_list[0:4])
# print(my_list[0:8])
# print(my_list[:8])
# print(my_list[:])
# print(my_list[::])
# print(my_list[::1])
# print(my_list[::3])
# print(my_list[::4])
# print(my_list[2:])



# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# # print(my_list[0:8:1])
# # print(my_list[8::-1])
# # print(my_list[2:8:1])
# # print(my_list[-6::1])
# # print(my_list[8:2:-1])
# print(my_list[2::-1])


# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# #.methodname(values)
# numbers.append(["vasu","raghavendra","indra"])
# print(numbers)

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5,"kiran"]
# numbers_2 = [3, 1, 4, 1, 5, 9, 2, 6, "vasukumar"]
# numbers.extend(numbers_2)
# print(numbers_2)
# print(numbers)

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5,"kiran"]
# numbers.extend(["apple","orangge"])
# print(numbers)


# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# copy_1 = numbers.copy()
# print(copy_1)

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# numbers.clear()
# print(numbers)

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5,2,3,4,2,2,2,2,2]
# print(numbers.count(2))

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# print(numbers.index(1))

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# numbers.remove(1)
# print(numbers)

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# obj = numbers.pop(5)
# print(numbers)
# print(obj*5)


# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# #.insert(index,element)
# numbers.insert(2,"vasu kumar")
# print(numbers)

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# numbers.reverse()
# # print(numbers[::-1])
# print(numbers)

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# numbers.sort(reverse=True)
# print(numbers)

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matrix[0][1]) #2
# print(matrix[1][1]) #5
# print(matrix[2][2]) #5

#syntax
# [expression for item in iterable]


# empty_list = []
# for i in range(6):
#     result = i*i
#     empty_list.append(result)
# print(empty_list)

# [expression for item in iterable]
# result = [i*i for i in range(6)]
# print(result)

# print([i*i for i in range(6)])

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5,1,1,1,1,1,1,1,1,11,1,1,1,5]
# empty_list = []
# for i in numbers:
#     if i!=1:
#         empty_list.append(i)
# print(empty_list)

# [expression for item in iterable if condition]
# result = [i for i in numbers if i!=1]
# print(result)

# print([i for i in numbers if i!=1])
# print([i for i in [3, 1, 4, 1, 5, 9, 2, 6, 5,1,1,1,1,1,1,1,1,11,1,1,1,5] if i!=1])

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5,1,1,1,1,1,1,1,1,11,1,1,1,5]
# print(len(numbers))
# print(numbers[21])
# print(numbers[-1])

















# list_1 = [1,2,3,4,5]

# print(list_1[:-1:])
# print(list_1[:4])

# print(list_1[4:2:-1])




# print(list_1[::1])
# print(list_1[-4:])
# print(list_1[3::-1])
# print(list_1[3:0:-1])



# print(list_1[::-1])

