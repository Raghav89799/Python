# Check Square using For loop

start_num = int(input("Enter the Start Number : "))
end_num = int(input("Enter the End Number : "))
j = 1
for i in range(start_num,end_num):
    if j**2 > start_num and j**2 < end_num:
       print(j,"square is",j*j)
    if j**2 > end_num:
        break
    j += 1

# Check Square using while loop

start_num = int(input("Enter the Start Number : "))
end_num = int(input("Enter the End Number : "))

i = 1

while True:
    if i**2 > start_num and i**2 < end_num:
       print(i,"square is",i*i)
    i += 1
    if i**2 > end_num:
        break
    