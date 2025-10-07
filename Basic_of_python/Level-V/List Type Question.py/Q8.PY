# Q8 ENTER A LIST AND INPUT A NUMBER THEN MORE THAN SUBRACT FOR SAMLL THEN COUNT OPREATION HOW MANY TIME 

a=eval(input("Enter a list  : "))
k=int(input("Enter a number : "))
count=0
l=len(a)
for i in range(l):
    while a[i]>k:
        a[i]=a[i]-k
        count=count+1
print("Count",count)