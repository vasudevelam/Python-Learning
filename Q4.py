#Q4 his simple program takes your marks as input and tells your grade (A, B, C, D, or Fail).
def grade(marks):
    if marks>90:
        return 'A'
    elif marks>80:              
        return 'B'
    elif marks>70:
        return 'C'
    elif marks>60:
        return 'D'
    else:
        return 'Fail'
    

marks=int(input("Enter your marks : "))
print(grade(marks))
