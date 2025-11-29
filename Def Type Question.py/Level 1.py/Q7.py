
# # # # n=input("Enter a string :")
# # # # l=len(n)
# # # # c=""
# # # # for i in range(l-1,-1,-1):
# # # #     c=c+n[i]
# # # # print(c)
    
# # # def rev(a):
# # #     l=len(a)
# # #     c=""
# # #     for i in range(l-1,-1,-1):
# # #         c=c+a[i]
# # #     return c

# # # a=input("Enter : ")
# # # print(rev(a))


# # # x = 'awesome'


# # # def myfunc():
# # #   global x
# # #   x = 'fantastic'
# # #   return x
# # # # myfunc()
# # # print('Python is ' + x)

# # txt="hello world"
# # a="HELLO WORLD"
# # # print(txt.strip(""))
# # # print(len(txt))
# # print(txt.capitalize())
# # print(a.casefold())
# # b=a.center(40)
# # l=len(b)
# # print(l

# # for i in range(5):
# #     n=input("ENter a name is :")
# #     print(n)

# # n=int(input("ENter a number is : "))
# # a , b =0,1
# # for i in range(n):
# #     print(a, end=" ")
# #     a,b=b,a+b


# n=eval(input("Enter a numbers is : "))
# min=n[0]
# for i in n:
#     if i<min:
#         min=i
# print(min)

# n=eval(input("Enter a number is : "))
# ev=0
# od=0
# for i in n:
#     if i%2==0:
#         ev=ev+1
#     else:
#         od=od+1
# print(ev)
# print(od)

# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         print(i)


# s=input("Enter a string is : ")
# v=["a","e","i","o","u"]
# for i in s:
#     if s in v:
#         print("VOlwes ")
#     else:
#         print("Consent ")


# s=eval(input("Enter a list is : "))
# sum=0
# for i in s:
#     sum=sum+i
# print(sum)

#second largest 
# n=eval(input("Enter a numbers is : "))
# max=n[0]
# l=len(n)
# for i in n:
#     if i>max:
#         max=i
# # print(i)
# a=sorted(n)
# print(a[-2])


# n=eval(input("Enter a numbers is : "))
# lar=n[0]
# slar=n[0]
# for i in n:
#     if i>lar:
#         lar=slar
#         slar=i
# print(slar)



# a=(input("Enter a string is "))
# vol=["a","e","i","o","u"]
# count_vol=0
# count_con=0
# count_digit=0
# count_space=0
# for char in a:
#     if char in vol:
#         count_vol=count_vol+1
#     elif char.isalpha():
#         count_con=count_con+1
#     elif char.isdigit():
#         count_digit=count_digit+1
#     elif char.isspace():
#         count_space=count_space+1
# print(count_vol)
# print(count_con)
# print(count_digit)
# print(count_space)

# a=input("ENtr a string is : ")
# if a==a[::-1]:
#     print("palidrome")
# else:
#     print("Not palidrpome")

# a=input("Enter a string is : ")
# v=["a","e","i","o","u"]
# c=""
# for char in a:
#     if char not in v:
#         c=c+char
# print(c)


# a=input("Enter a string is :  ")
# spe=[" ","_"]
# c=""
# for char in a:
#     if char not in spe:
#         c=c+char
# print(c)

# n=eval(input("Enter a numbers is : "))
# ev=[]
# for i in n:
#     if i%2==0:
#         ev.append(i)
# print(ev)

# a=eval(input("Enter a list 1 is : "))
# b=eval(input("Enter a list 2 is : "))
# c=[]
# c.append(a+b)
# print(c)


# a=int(input("Enter a number is : "))
# for i in range(1,a):
#     print(i)

# for i in range(2,101):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)


# a=int(input("Enter a number is : "))
# length=len(str(a))
# sum=0
# temp=a
# while temp>0:
#     digit=temp%10
#     sum=sum+digit**length
#     temp=temp//10
# if sum==a:
#     print("Armstronde : ",a)
# else:
#     print("Not Aramstronge : ",a)

# a=int(input("Enter a number is : "))
# for a in range (1,10000):
#     sum=0
#     for i in range(1,a):
#      if a%i==0:
#          sum=sum+i

#     if sum==a:
#         print("Prefect number is :",a)


# a=int(input("Enter a number is : "))
# sq=a*a
# count=0
# temp=a
# while temp>0:
#     count=count+1
#     temp//=10
# last_digit=sq%(10**count)
# if last_digit==a:
#     print("Autoronic: ",a)
# else:
#     print("Not Autoronic: ",a)


n=int(input("Enter a number is : "))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)
        














