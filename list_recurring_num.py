items = int(input("Enter the items number you want to add in list : "))

my_list = []
duplic_list = []
extra_list = []

for item in range(items):
    item = input("Enter the item : ")
    my_list.append(item)

i = 0
j = 1
while i < len(my_list):
    if my_list[i] not in extra_list:
        extra_list.append(my_list[i])
    else:
        duplic_list.append(my_list[i])
    i += 1
    
print(duplic_list)