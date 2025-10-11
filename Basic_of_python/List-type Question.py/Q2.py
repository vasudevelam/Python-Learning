# Take a list of integers and rotate it right by one position (last element becomes first).

a=eval(input('Enter a number is : '))

l=len(a)
x=a[l-1]

for i in range(l-1,0,-1):
    a[i],a[i-1]=a[i-1],a[i]
print(a)