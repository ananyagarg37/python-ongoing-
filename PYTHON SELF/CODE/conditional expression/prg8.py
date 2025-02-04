# write programm to calculate grade of student
marks = int(input())

if (marks>= 100 and marks>=90):
    grade = "ex"
elif (marks>=90 and marks >= 80):
    grade = "a"
elif (marks>=70 and marks >= 60):
    grade = "b"
elif (marks>=60 and marks >= 50):
    grade = "c"
else:
    grade = "fail"
    
print("end" , grade )