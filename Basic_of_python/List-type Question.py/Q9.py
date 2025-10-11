# Find the second smallest element in a list (without using sort).
a=eval(input('Enter a number is :'))
l=len(a)
for i in range(l):
    for k in range(l-1):
        if a[k]>a[k+1]:
            a[k],a[k+1]=a[k+1],a[k]
print(a)
        