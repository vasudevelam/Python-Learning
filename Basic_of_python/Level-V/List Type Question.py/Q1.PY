#Q1 FIND MID VALUE 

a=[1,2,4,5,8,26,20]
a.sort()
b=len(a)
mid=b//2
if b%2==0:
    m1,m2=mid-1,mid
    mid=a[m1]+a[m2]/2
else:
    mid=a[mid]
print(mid)