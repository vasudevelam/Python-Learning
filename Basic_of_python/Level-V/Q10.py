#Calculator Program

#Perform basic arithmetic (+, −, ×, ÷).

#Use functions for each operation.

a =float(input("Enter a numbeer is :  "))
b =float(input("Enter a numbert is :  "))
op =input("Enter a sgin ['+','-','*','/']")
if op=="+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op=="*":
    print(a*b)
elif op=="/":
    if b!=0:
        print(a/b)
    else:
        print("Erro")
else:
    print("Invalid")
