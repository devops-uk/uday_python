# set_1 = {1,2,3,4}
# print(type(set_1))

# set_2 = set()
# print(type(set_2))

# sample = {"vasu","kumar",1,5.7,(1,2),"vasu","kumar",1,1,1,1,1,1,1,1,}
# print(sample)

# set_1 = {"mahesh","radhakrishna","Ram","vasu",1234}
# set_1.add("indra")
# print(set_1)

# set_1 = {"mahesh","radhakrishna","Ram","vasu",1234}
# set_1.clear()
# print(set_1)

# set_1 = {"mahesh","radhakrishna","Ram","vasu",1234}
# set_2 = set_1.copy()
# print(set_2)

# set_1 = {"mahesh","radhakrishna","Ram","vasu",1234}
# set_1.pop()
# print(set_1)


# set_1 = {"mahesh","radhakrishna","Ram","vasu",1234}
# set_1.remove(1234)
# print(set_1)

# set_1 = {"mahesh","radhakrishna","Ram","vasu",1234}
# print(set_1)
# set_2 = {"rajesh","python",1234,5678,9}
# set_1.update(set_2)
# print(set_1)


# set_1 = {1,2,3,4}
# set_2 = {4,5,6,7}
# set_3 = set_1.union(set_2)
# print(set_3)

# set_1 = {1,2,3,4}
# set_2 = {4,5,6,7}
# set_3 = set_1.intersection(set_2)
# print(set_3)


# set_1 = {1,2,3,4}
# set_2 = {4,5,6,7}
# set_3 = set_1.difference(set_2)
# print(set_3)

# set_1 = {1,2,3,4}
# set_2 = {4,5,6,7}
# set_3 = set_1.symmetric_difference(set_2)
# print(set_3)

# set_1 = {1,2,3,}
# set_2 = {4,5,6,7}
# print(set_1.isdisjoint(set_2))

# set_1 = {1,2,3,4}
# set_2 = {1,2,3,5,4}
# # print(set_1.issuperset(set_2))
# # print(set_2.issubset(set_1))
# print(set_2.issuperset(set_1))


# set_1 = {1,2,3,4} #--> mutable
# set_1.add(5)
# # print(set_1)
# set_2 = frozenset(set_1) ##---> immutable version of set
# print(set_2)
# set_2.add(6)
# print(set_2)



###########   TUPLE  ######################
# tuple_1 = (1,2,3,"vasu",(1,2),(2,3))
# print(type(tuple_1))

# tuple_2 = ()
# print(type(tuple_2))

# tuple_3 = tuple()
# print(type(tuple_3))

# tuple_1 = (1,2,3,1,2,3,5,5,5,5,5,5,5)
# # print(len(tuple_1))
# # print(tuple_1[1])
# # print(tuple_1.count(5))
# print(tuple_1.index(5))
# print(tuple_1[1:7])


# tuple_1 = (1,"vasu","ibm",4,5)
# print(tuple_1[1])
# print(tuple_1[-1])


# tuple_1 = (1,2,3,1,2,3,5,5,5,5,5,5,5,)
# print(all(tuple_1))

# items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]
# total_price = 0

# print("-"*10)