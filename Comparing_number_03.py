num1 = int(input("Enter the First Number value : "))
num2 = int(input("Enter the Second Number value : "))
num3 = int(input("Enter the Third Number value : "))
num4 = int(input("Enter the Fourth Number value : "))


if num1 > num2:
    higher_result_01 = num1
    lower_result_01 = num2
else:
    higher_result_01 = num2
    lower_result_01 = num1

if num3 > num4:
    higher_result_02 = num3
    lower_result_02 = num4
else:
    higher_result_02 = num4
    lower_result_02 = num3

if higher_result_01 > higher_result_02:
    print(higher_result_01,"is the highest")
else:
    print(higher_result_02,"is the highest")

if lower_result_01 > lower_result_02:
    print(lower_result_02,"is the lowest")
else:
    print(lower_result_01,"is the lowest")
