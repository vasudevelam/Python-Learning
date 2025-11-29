# 1. Simple Calculator using def /

def calculator():
    num1=int(input("Enter 1 number is : "))
    num2=int(input("Enter 2 number is : "))
    operation=input("Enter operation (+, -, *, /) is : ")
    if operation=='+':
        return num1+num2
    elif operation=='-':
        return num1-num2
    elif operation=="*":
        return num1*num2
    elif operation=="/":
        return num1/num2
    else:
        return "Invalid operation"
    


print("Using simple caculation is :",calculator())