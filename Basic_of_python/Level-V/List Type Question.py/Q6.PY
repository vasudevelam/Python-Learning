#Q6 INPUT A LIST AND THEN COUNT NUMBER OF TIMES IS DIGITIS 

a=eval(input("Enter a numbers: "))
count=0
b=int(input("Enter a number :"))
leng=len(a)
for i in range(0,leng):  
    if b==a[i]:
        count=count+1
    i=i+1
print(count)