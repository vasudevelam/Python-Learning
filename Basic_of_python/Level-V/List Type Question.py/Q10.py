# #Q10 PRINT A TABLE USING LIST

# a=[]
# n=int(input("Enter a number :"))
# for i in range(1,11):
#     a.append(n*i)
# print(a)



# #q11
# a=['APPLE','MANGO','ORANGE']
# b=len(a)
# for i in a:
#     print(i)

# a=[2,3,42,50,97,1,11,23]
# for i in a:
#     if i%2==0:
#         print("Even: ",i)


# a=[]
# for i in range(5):
#     n=int(input("Enter a number is : "))
#     a.append(n)
# print(a)


# a=[1,2,3,4,5,6]
# c=[]
# b=len(a)
# for i in range(b,0,-1):
#     c.append(i)
# print(c)


# a=[1,2,3,100,5,6]
# sum=0
# for i in a:
#     sum=sum+i
# print(sum)

# a=[1,2,3,10,5,6]
# max=a[0]
# min=a[0]
# for i in a:
#     if max<i:
#         max=i
#     elif min>i:
#         min=i

# print(max)
# print(min)

# a=[1,2,3,10,5,6]
# count1=0
# count2=0
# for i in a:
#     if i%2==0:
#         count1=count1+1
#     else:
#         count2=count2+1
# print('even no:',count1)
# print('odd no:',count2)
    

# a=[1,2,3,10,5,6]
# l=len(a)
# for i in range(l):
#     print(i,a[i])


# a=[1,2,67,5,5,10,102]
# l=len(a)
# largest=a[0]
# s_largest=a[0]
# for i in range(l):
#     if a[i] > largest:
#         s_largest = largest
#         largest = a[i]
#     elif a[i] > s_largest and a[i] != largest:
#         s_largest = a[i]
        
    

# print(largest)
# print(s_largest)


#q
# a=[1,2,3,4,5,6]
# l=len(a)
# s1=0
# s2=0
# if l%2==0:
#     for i in range(l//2):
#         s1=s1+i
#     for i in range(l//2,l):
#         s2=s2+i
#     if s1==s2:
#         print("0")
#     else:
#         print(abs(s1-s2))

# a=['VISHAL','RAJ','UTTAM','ASHU','AYUSH']
# for i in a:
#     if i[0]=='A':
#         print("Start with a: ",i)


# a=[1,2,3,4,5,6]
# c=[]
# for i in a:
#     b=i*i
#     c.append(b)

# print(c)

# a=eval(input("Enter a 10 number is :  "))
# l=len(a)
# c=50
# r=[]
# for i in range(l):
#     if a[i]>c:
#         x=a[i]
#         r.append(x)
# print(r)

# a = [20, 10, 20, 30, 35, 46, 35, 70]
# b = []
# l = len(a)
# for i in range(l):
#     if a.count(a[i]) == 1:
#         b.append(a[i])
# print(b)

# a=[1,2,3,4,5,20,67,99]
# b=[1,20,45,67,89,100,12,23]

# c=[]
# for i in a+b:
#     if i not in c:
#         c.append(i)
# print(c)

a=["Ram","Vishal","Vasudevalam"]
b=a[0]
for i in a:
    if len(i) > len(b):
        b=i
print(b)