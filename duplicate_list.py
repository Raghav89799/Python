list1 = [6,4,5,6,7,45,3,3,55,55,7]
my_dict = dict()
count = []
for i in list1:
    my_dict[i] = 0

for item in list1:
    for key,value in my_dict.items():
        if item == key:
            my_dict[key] = value+1
        j = 0

for key,value in my_dict.items():
    if value > 1:
        print(key)
        

        
