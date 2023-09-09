# # Program to add item in tuple by casting method

# my_tuple = ()
# my_tuple = list(my_tuple)

# items = int(input("Enter the Item you want to add in tuple : "))

# for item in range(items):
#     item = input("Enter the item : ")
#     my_tuple.append(item)

# my_tuple = tuple(my_tuple)
# print(my_tuple)

# # Program to remove item in tuple by casting method

# my_tuple = ()
# my_tuple = list(my_tuple)

# items = int(input("Enter the Item you want to add in tuple : "))

# for item in range(items):
#     item = input("Enter the item : ")
#     my_tuple.append(item)

# item = input("Enter the item to remove : ")
# my_tuple.remove(item)

# my_tuple = tuple(my_tuple)
# print(my_tuple)

# # Program to replace item in tuple by casting method

# my_tuple = ()
# my_tuple = list(my_tuple)

# items = int(input("Enter the Item you want to add in tuple : "))

# for item in range(items):
#     item = input("Enter the item : ")
#     my_tuple.append(item)

# item = input("Enter the item to replace into : ")
# replace_item = input("Enter the item to replaced : ")

# for i in range(len(my_tuple)):
#     if my_tuple[i] == item:
#         item_index = i
# my_tuple.remove(item)
# my_tuple.insert(item_index,replace_item)

# my_tuple = tuple(my_tuple)
# print(my_tuple)

# # Program to print length of tuple

# my_tuple = ()
# my_tuple = list(my_tuple)

# items = int(input("Enter the Item you want to add in tuple : "))

# for item in range(items):
#     item = input("Enter the item : ")
#     my_tuple.append(item)

# my_tuple = tuple(my_tuple)
# print("Len of Tuple",len(my_tuple))

# # Program to print highest,lowest in tuple

# my_tuple = ()
# my_tuple = list(my_tuple)
# highest = 0

# items = int(input("Enter the Item you want to add in tuple : "))

# for item in range(items):
#     item = int(input("Enter the item : "))
#     my_tuple.append(item)
    
# lowest = my_tuple[0]
# for i in my_tuple:
#     if highest < i:
#         highest = i
    
#     if lowest > i:
#         lowest = i

# my_tuple = tuple(my_tuple)
# print("Highest in tuple is",highest)
# print("Lowest in tuple is",lowest)

# # Program to reverse tuple 

# my_tuple = ()
# my_tuple = list(my_tuple)
# new_tuple = ()
# new_tuple = list(my_tuple)

# items = int(input("Enter the Item you want to add in tuple : "))

# for item in range(items):
#     item = input("Enter the item : ")
#     my_tuple.append(item)
    
# i = len(my_tuple)
# for j in range(len(my_tuple)):
#     new_tuple.append(my_tuple[i-1])
#     i -= 1

# my_tuple = tuple(my_tuple)
# new_tuple = tuple(new_tuple)
# print(my_tuple)
# print(new_tuple)

# # Program to check even or odd

# my_tuple = ()
# my_tuple = list(my_tuple)

# items = int(input("Enter the Item you want to add in tuple : "))

# for item in range(items):
#     item = int(input("Enter the item : "))
#     my_tuple.append(item)

# for i in my_tuple:
#     if i%2==0:
#         print(i,"is even")
#     else :
#         print(i,"is odd")
        
# Program to check duplicate in tuple

my_tuple = ()
my_tuple = list(my_tuple)
extra_tuple = ()
extra_tuple = list(my_tuple)
dup_tuple = ()
dup_tuple = list(my_tuple)

items = int(input("Enter the Item you want to add in tuple : "))

for item in range(items):
    item = input("Enter the item : ")
    my_tuple.append(item)
    
for i in my_tuple:
    if i not in extra_tuple:
        extra_tuple.append(i)
    else:
        dup_tuple.append(i)

my_tuple = tuple(my_tuple)
dup_tuple = tuple(dup_tuple)
print("Original Tuple : ",my_tuple)
print("Duplicate tuple : ",dup_tuple)

