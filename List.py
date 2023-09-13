# Program to add item in List

my_list = []

items = int(input("Enter the Item you want to add in List : "))

for item in range(items):
    item = input("Enter the item : ")
    my_list.append(item)

print(my_list)

# Program to remove item in List

my_list = []

items = int(input("Enter the Item you want to add in List : "))

for item in range(items):
    item = input("Enter the item : ")
    my_list.append(item)

item = input("Enter the item you want to remove : ")

while item not in my_list:
    print("Item is not in List")
    item = input("Enter the item you want to remove : ")
    
my_list.remove(item)
print(my_list)

# Program to replace item in List

my_list = []

items = int(input("Enter the Item you want to add in List : "))

for item in range(items):
    item = input("Enter the item : ")
    my_list.append(item)

item = input("Enter the item you want to replace with : ")

while item not in my_list:
    print("Item is not in List")
    item = input("Enter the item you want to replace with : ")

replace_item = input("Enter the item you want to replaced : ")

for i in range(len(my_list)):
    if my_list[i] == item:
        item_index = i
        
my_list.remove(item)
my_list.insert(item_index,replace_item)

print(my_list)

# Program to print length of List

my_list = []

items = int(input("Enter the Item you want to add in List : "))

for item in range(items):
    item = input("Enter the item : ")
    my_list.append(item)

print("Len of List : ",len(my_list))

# Program to print highest,lowest in List

my_list = []
highest = 0
items = int(input("Enter the Item you want to add in List : "))

for item in range(items):
    item = int(input("Enter the item : "))
    my_list.append(item)

lowest = my_list[0]

for item in my_list:
    
    if highest < item:
        highest = item
        
    if lowest > item:
        lowest = item
        
print("Highest in list :",highest)
print("Lowest in List :",lowest)

# Program to reverse List

my_list = []
new_list = []
items = int(input("Enter the Item you want to add in List : "))

for item in range(items):
    item = input("Enter the item : ")
    my_list.append(item)

i = len(my_list)

for j in range(len(my_list)):
    new_list.append(my_list[i-1])
    i -= 1
    
print("Original List : ",my_list)
print("Reverse List : ",new_list)

# Program to check even or odd in List

my_list = []

items = int(input("Enter the Item you want to add in List : "))

for item in range(items):
    item = int(input("Enter the item : "))
    my_list.append(item)

for item in my_list:
    if item%2==0:
        print("Item is Even : ",item)
    else:
        print("item is Odd : ",item)
        
# Program to check duplicate in tuple

my_list = []
extra_list = []
dup_list = []

items = int(input("Enter the Item you want to add in List: "))

for item in range(items):
    item = input("Enter the item : ")
    my_list.append(item)
    
for i in my_list:
    if i not in extra_list:
        extra_list.append(i)
    else:
        dup_list.append(i)

print("Original List : ",my_list)
print("Duplicate List : ",dup_list)