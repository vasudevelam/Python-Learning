#EX 1
rno=[]
marks=[]
for i in range(4):
    r,m=eval(input("Enter a roll no and marks is : "))
    rno.append(r)
    marks.append(m)
Students={rno[0]:marks[0],rno[1]:marks[1],rno[2]:marks[2],rno[3]:marks[3]}
print("Student Dict is : ",Students)

# len=(di)
# if di[le]<75:
#     print("less than 75",di[2])
# else:
#     print("gr than 75 : ",di[2])

#EX 2
# a=[]
# b=eval(input("ffewwe"))
# c=a.append(b)
# print(b)

#EX 3
# c={"a":1,"b":2,"c":3,"d":4,"e":5}
# print(c)
# for i in c:
#     print(i,":",c[i])

#EX 4
# p={"Rohit":997765,"Vishal":454545,"yash":4559595,"prashant":656565}
# # for i in p:
# #     print(i," : ",p[i])
# print(p.keys())
# print(p.values())

#EX 5
# j={1:56,2:67,3:97,4:56}
# if 89.9 in j.values():
#     print("yes")
# else:
#     print("False")

# d={'a1':'1','a2':'2','a3':'3','a4':'4','a5':'5'}
# print(list(d.keys()))

# S={}
# for j in range(5):
#     r,m=eval(input("enter roll no:, Enter a marks is : "))
#     S[r]=m
# print(S)

# S1={}
# for k in range(3):
#     ro=int(input("Enter a roll no is : "))
#     m=int(input("Enter a marks is : "))
#     S1[ro]=m
# print(S1)

# s={1:34,2:45,3:67,4:80}
# r=int(input("Enter a number is : "))
# if r in s:
#     m=int(input("Enter a number is : "))
#     s[r]=m
#     print(s)
# else:
#     print("roll no found")

#Q
# d={1:"Ram",2:"Vishal",3:"RAj"}
# for i in d:
#     print(d[i])

# s={"Name":"Aman","Age":17}
# s["grade"]="a"
# # s.pop("grade")
# print(s)

# a="Hello"
# b={}
# for i in a:
#     if i in b:
#         b[i]=b[i]+1
#     else:
#         b[i]=1
# print(b)
# book={
# "a":{"Title":"python","Author":"RD","Price":267},
# "b":{"Title":"python","Author":"RD","Price":267}
# }
# print(book)


# d={"Vasu":100,"Vishal":78,"YAsh":56}
# c=max(d.values())
# for index,value in d.items():
#     if value==c:
#         print("Topper :",index)


# d={"Vasu":100,"Vishal":78,"YAsh":56}
# s=input("Enter key ")
# if s in d:
#     print("YEs")
# else:
#     print("no")



# d={"Eng":67,"Bst":45,"Acc":87,"IP":56}
# print(d["Eng"])
# print(d.get("Eco","not found"))

# d={x:x*x*x for x in range(1,6)}
# print(d)

# a={"x":1,"y":2}
# b={"y":3,"z":4}
# c=a|b
# d=c.copy()
# print(c)
# print(d)
# if "x" in d:
#     print("Exist")
# else:
#     print("Not exist")


# student={"RAj":67,"Vishal":56,"Yash":45,"Parth":33,"Shyam":56}
# a=max(student.values())
# print(a)
# for i,j in student.items():
#     if j==a:
#         print(i)


# l1=["a","b","c","d","e"]
# l2=[1,2,3,4,5]
# d={l1[i]:l2[i] for i in range(len(l1))}
# print(d)


# a={"RAj":67,"Vishal":56,"Yash":45,"Parth":33,"Shyam":56}
# d=[]
# for i in a.values():
#     d.append(i)
# print(d)

# c=list(a.values())
# print(c)




# a="today is good day is not good day and but python is all ways"
# c=a.split()
# b={}
# for i in c:
#     if i in b:
#         b[i]=b[i]+1
#     else:
#       b[i]=1
# print(b)



# d={"chips":60,"Maggi":112,"Apple":56,"milk":34}
# a=max(d.values())
# print(a)
# for i,j in d.items():
#     if j==a:
#         print(i)

# d={"chips":60,"Maggi":112,"Apple":56,"milk":34}
# sum=0
# for i in d.values():
#     sum=sum+i
# print(sum)



# d={x:x*x for x in range(1,11)}
# print(d)


# a={'a','b','c','d','e'}
# b={1,2,3,4,5,6}
# c=dict(zip(a,b))
# print(c)

# d=a|b
# print(d)



# rno=[]
# marks=[]
# for i in range(3):
#     r=eval(input("Enter a number is roll no is : "))
#     m=eval(input("Enter a number is marks is : "))
#     rno.append(r)
#     marks.append(m)
# di={rno[0]:marks[0],rno[1]:marks[1],rno[2]:marks[2]}
# print("Dict is : ",di)



# employe={
# "Raja":{"Age":45,"Salary":45000,"Location":"Nodia"},
# "Karan":{"age":42,"Salary":50000,"location":"Delhi"}
# }
# print(employe)
# employe["Karan"]["Salary"]=10000

# print(employe)

# a={1:23,2:89,3:78}
# a[1]=12
# print(a)




# d={}
# n=int(input("Enter a number is : "))
# for i in range(n):
#     na=input("Enter a name is : ")
#     val=int(input("Enter a values : "))
#     d[na]=val
    
# print(d)

# del d['ram']
# print(d)


# print(a)
# rno=int(input("Enter a roll deleted is : "))
# if rno in a:
#     del a[rno]
#     print("number is exist : ",rno)
# else:
#     print("number is not exist : ",rno)

# print(a)




# a={1:45,2:89,3:56,4:78,5:112}
# b={v:k for k,v in a.items()}
# print(b)
# import json

# print(json.dumps(a,indent=4))

# print(len(a))
# b=a.items()
# print(b)

# a={1:45,2:89,3:56,4:78,5:112}
# c=a.update({1:5})
# print(a)


# fruit={'banana':2,'apple':4}
# l1=['Apple','banana','apple']
# for i in l1:
#     if i in fruit:
#         fruit[i]+=1
#     else:
#         fruit[i]=1
# print(len(fruit))
# print(fruit)


# a='abracadbar'
# count={}
# for i in a:
#     count[i]=count[i]+1
#     print(count)



# def feb(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     return feb(n-1)+feb(n-2)
# def print_feb(n):
#     for i in range(n):
#         print(feb(i))

# print_feb(12)


# def F(n):
#     if n<=1:
#         return n
#     else:
#         return F(n-1)+F(n-2)
# print(F(10))

# a=[1,2,3,4,5]
# m=a[0]
# for i in a:
#     if i<m:
#         m=i
# print(m)



# a=[20,30,120,13,100]
# l=len(a)
# for i in range(0,l,2):
#     # print(a[i])


# def a(arr,i=0):
#     if i >= len(arr):
#         return 
#     print(arr[i], end=" ")
#     a(arr,i+2)
# arr=[12,34,56,78]
# a(arr)





# a=[12,34,5,678,90,100,120]
# l=len(a)
# max=a[l-1]
# leader=[max]
# for i in range(l-2,-1,-1):
#     if a[i]>max:
#         leader.append(a[i])
#         max=a[i]
# leader.reverse()
# print(leader)


# a=[12,10,5,6,3,2]
# l=len(a)
# sorting=True
# for i in range(0,l-1):
#     if a[i]>a[i+1]:
#         sorting=False
#         break

# print(sorting)


# a=[2,5,1,9,7,13,4]
# l=len(a)
# for i in range(l-1):
#     for j in range(l-i-1):
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]

# print(a)