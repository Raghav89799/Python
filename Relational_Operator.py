# Program 01 for Relational operator

print(5 == 5)
print(7 == 4)
print(7 > 8)
print(2 < 9)
print(10 != 3)

# Program 02 for Relational operator

num = int(input("Enter the value of Num : "))

if num != 10:
    print("Num is not equal 10")
else:
    print("Num is equal to 10")

# Program 03 for Relational operator

num1 = int(input("Enter the First Number value : "))
num2 = int(input("Enter the Second Number value : "))

if num1 > 5 and num2 > 5:
    print("Both are greater than 5")
elif num1 > 5 or num2 > 5:
    print("One of the Num is greater than 5")
elif num1 == 5 and num2 == 5:
    print("Both are equal to 5")
elif num1 == 5 or num2 == 5:
    print("One of the num is equal to 5")
else:
    print("Both are less than 5")


