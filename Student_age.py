student_age_01 = int(input("Enter the First Student Age : "))
student_age_02 = int(input("Enter the Second Student Age : "))
student_age_03 = int(input("Enter the Third Student Age : "))

if student_age_01 > student_age_02:
    result_age = student_age_01
    additional_result = "Student 1st"
else:
    result_age = student_age_02
    additional_result = "Student 2nd"

if student_age_03 > result_age:
    print("Student 3rd age is highest",student_age_03)
else:
    print(additional_result,"age is highest",result_age)