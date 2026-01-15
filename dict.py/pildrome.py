n=input("Enter a number is : ")
a=len(n)
for i in range(a-1,-1,-1):
    print(n[i], end="")


n=int(input("Enter a number is : "))
temp=n
rev=0
while n>0:
    rev=rev*10+n%10
    n//=10
if temp==rev:
    print("Palidrome : ")
else:
    print("Not palidrome : ")


n=int(input("Enter a number is : "))
count=0
while n>0:
    count=count+1
    n//=10
print(count)

n=int(input("Enter a number is : "))
flag=True
if n<=1:
    flag=False
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        flag=False
        break
print("prime"if flag else "Not Prime")


n=int(input("Enter a number is "))
a=0
b=1
while n<
    print(a, end=" ")
    a,b=b,a+b


n=int(input("Enter a number is : "))
fac=1
for i in range(1,n+1):
    fac=fac*i
print(fac)

n=int(input("Enter a number is " ))
a=0
b=1
for i in range(n):
    print(a)
    a,b=b,a+b


n=int(input("Enter a number is : "))
l=len(str(n))
tem=n
rev=0
for i in range(l):
    rev=rev*10+n%10
    n=n//10
if tem==rev:
    print("Palidrome ")
else:
    print("Not Palidrome")

n=int(input("Enter a number is : "))
fac=1
for i in range(1,n+1):
    fac=fac*i
print(fac)

n=int(input("Enter a number is : "))
l=len(str(n))
tem=n
rev=0
for i in range(l):
    rev=rev*10+n%10
    n=n//10
print(rev)



n=int(input("Enter a number is : "))
sum=0
while n>0:
    sum=sum+n%10
    n//=10
print(sum)



a=eval(input("Enter a list "))
sum=0
l=len(a)
for i in a:
    sum=sum+i
print(sum)
m=sum/l
print(m)


a=eval(input("Enter a list "))
l=len(a)
se=int(input("Enter a Element is list is : "))
for i in range(l):
    if se==a[i]:
        print(se,"Yes is found ",i)
        break
else:
    print("Not found ")

a=eval(input("Enter a list "))
l=len(a)
m=max(a)
ind=a.index(m)
if ind<=(l/2):
    print("The max is ",m,"List in 1 half")
else:
    print("The max ",m,"List 2 half ")


a=eval(input("Enter a list 1 "))
max=a[0]
for i in a:
    if i>max:
        max=i
print(max)
b=eval(input("Enter a list 2 "))
max_2=b[0]
for j in b:
    max_2=j
print(max_2)
if max>max_2:
    print("Max a is grater ")
else:
    print("Max b is greater ")


# Write a Python program to find the difference between maximum and minimum elements in a list

l1=eval(input("Enter a list is : "))
ln=len(l1)
max=l1[0]
min=l1[0]
for i in l1:
    if i>max:
        max=i
    else:
        min=i
print("Max number in list is : ",max)
print("Min number in list is : ",min)
