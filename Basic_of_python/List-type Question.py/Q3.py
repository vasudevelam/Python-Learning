# Input a list and remove all elements that occur more than once.
a=eval(input("Enter a number is : "))
b=[]
for i in a:
    if a.count(i)==1:
        b.append(i)

print(b)