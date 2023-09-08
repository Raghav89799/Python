age = int(input("Enter the age : "))

if age > 0 and age <=12:
    print("You are Kid")
elif age > 12 and age <= 19:
    print("You are Teenager")
elif age > 19 and age <= 40:
    print("You are young")
elif age > 40 and age <= 60:
    print("You are recently old")
elif age > 60 and age <= 100:
    print("You are very old")
else:
    print("Wrong age entered !!!!!!!!!!!!!")
