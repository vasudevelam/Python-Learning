#Q9 ROTAE NUMBER 1 THEN PRINT 


a=eval(input("Enter a list  : "))
b=len(a)
c=a[len(a)-1]
for i in range(len(a)-1,0,-1):
    a[i]=a[i-1]
a[0]=c
print(a)

