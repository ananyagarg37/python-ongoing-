# write a program to find out weather student is passed or fail if it required a total 40 % or atleast 33% in each subject to pass. assume 3 subject and take input from user.
marks1 = int(input())
marks2 = int(input())
marks3 = int(input())

# total percentage 
total_percentage = (100*(marks1+marks2+marks3  ))/300

if (total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
    print("passed" , total_percentage)
else:
    print("failed" , total_percentage)
    