# Level 2: Intermediate List Operations

# Write a program to find the sum and average of all numbers in a list.

# Write a program to find the maximum and minimum numbers in a list without using max() and min().

# Input a list of numbers and count how many are positive and negative.

# Write a program to reverse a list without using the reverse() function.














# a =eval(input("Enter a list is : "))
# b=[]
# i=len(a)-1
# ind=a.index(a)
# b.append(ind)
# print(b)
# c=reversed(a)
# print(list(c))
# while i>=0:
#     b.append(a[i])
#     i=i-1
# print(b)








    


#q3
a=eval(input("Enter a list  : "))
b=len(a)
c=a[len(a)-1]
for i in range(len(a)-1,0,-1):
    a[i]=a[i-1]
a[0]=c
print(a)


# a=[]
# n=int(input("Enter a number :"))
# for i in range(1,11):
#     a.append(n*i)
# print(a)