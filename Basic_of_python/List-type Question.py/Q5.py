# Reverse a list in place without using built-in functions.
a=eval(input("Enter a number is: "))
b=len(a)
c=[]
for i in range(b-1, -1, -1):
    c.append(a[i])
print(c)
