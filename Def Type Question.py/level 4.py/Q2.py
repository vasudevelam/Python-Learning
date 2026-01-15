# 1. Student Marks Calculator
# 🎯 Objective:

# To calculate a student’s total marks, average, and grade using a function and conditional statements.

# 🧩 Problem Statement:

# Create a function that takes marks of 5 subjects (as a list).

# Calculate:

# Total marks

# Average marks

# Grade:

# A: 90–100

# B: 80–89

# C: 70–79

# D: 60–69

# F: Below 60

# Display total, average, and grade.


def student_performance():
    sum=0
    subject=[]
    marks=[]
    for i in range(5):
        su=input("Enter the subject name is : ")
        subject.append(su)
        num=int(input("Enter the marks is : "))
        marks.append(num)
        for j in range(len(marks)):
            sum=sum+marks[j]
            average=(sum/500)*100
            if average>=90 and average<=100:
                grade='A'
            elif average>=80 and average<90:
                grade='B'
            elif average>=70 and average<80:
                grade='C'
            elif average>=60 and average<70:
                grade='D'
            else:
                grade='F'
    return f"Total Marks: {sum}, Average Marks: {average}, Grade: {grade}"

    
    
print(student_performance())