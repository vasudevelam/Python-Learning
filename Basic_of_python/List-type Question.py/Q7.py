# Write a program to find all duplicates in a list

a=eval(input('Enter a number is :'))
b=[]
for i in a:
    if a.count(i)>=1 and i not in b:
        b.append(i)
print(b)