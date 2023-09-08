# Series using for loop

start_num = int(input("Enter the Start Number : "))
end_num = int(input("Enter the End Number : "))

for i in range(start_num,end_num,1):
    print(i)
for i in range(start_num,end_num,-1):
    print(i)

# Series using while loop

start_num = int(input("Enter the Start Number : "))
end_num = int(input("Enter the End Number : "))

while start_num <= end_num:
    print(start_num)
    start_num += 1

while start_num >= end_num:
    print(start_num)
    start_num -= 1