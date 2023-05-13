# List : Collection of several type of data
# Indexing method is used and it starts with zero
# Eg.
# l1 = [1,2,3,4]
# print(l1)
# print(type(l1))
# Access list elements through indexing
# print(l1[3])

# Negative Indexing
# print(l1[-3])
# print(l1[len(l1)-3])
# print(l1[4-3])
# print(l1[1])

# To find a element in list and same thing apply for String
# if 5 in l1:
#     print("Yes")
# else:
#     print("No")

# l2 = [1,12,33,"Jay",2222,"@",544,4,5,77]

# print(l2[1:8])
# print(l2[1:8:5])
# print(l2[0:len(l2)])
# print(len(l2))

# List Comprehension
# lst= [i for i in range(4)]
# print(lst)
# lst2= [i**2 for i in range(10)]
# print(lst2)

# List Methods

l = [11,4,51,2,3,4]
print(l)

# Sort the list
l.sort()
print(l)

# Reverse the list
l.reverse()
print(l)

# Count a element present in list

print(l.count(4))

# Copy the list

m = l.copy()
m[0]= 0
print(l)
print(m)
# Insert a element at a given Index
l.insert(2, 43)
print(l) 
# Add one list with another
color = ['Red','Yellow','orange', 'green']
rainbow = ['violet','indigo','blue']
rainbow.extend(color)
print(rainbow)
# concatenation of list
l1 =[1,2,3,4]
l2 =[5,6,7,8]
l3 = l1 +l2
print(l3)