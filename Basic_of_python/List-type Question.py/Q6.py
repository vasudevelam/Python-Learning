# Given a list of marks of students, find and print the average, highest, and lowest
a=eval(input('Enter a student marks :'))
b=sum(a)
avg =b/len(a)
c=max(a)
d=min(a)
print("Average : ",avg)
print("Highest : ",c)
print("Lowest : ",d)
