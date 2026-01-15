# # tem converte celsius and fahrenheti 
# #f = (c * 9/5) + 32
# # c = (f - 32) * 5/9
# def tem_conv():
#     for i in range(100):
#         print("1.Celsius To Fahrenheti")
#         print("2.Fahrenheti To Celsius")
#         print("3.Exist")
#         choice=int(input("Enter a number (1 to 3 ) "))
#         if choice==1:
#             c=float(input("Enter a number is celsius : "))
#             f = (c * 9/5) + 32
#             print("Temp is F :",f)
#         elif choice==2:
#             f=float(input("Enter a number is Fahreheti : "))
#             c = (f - 32)* 5/9
#             print("Temp is C : ",c)
#         elif choice==3:
#             print("Exist: ")
#             break
#         else:
#             print("Invalid")



# tem_conv()

#print("Vasu","is","a",23,sep="\n")
# print("Vasu","is","a",23,end=" ")
# print("Vasu","is","a")



# n="*"
# for i in range(1,5):
#     print(i*n)

# n=10
# for i in range (1,n+1):
#     for j in range(i):
#         print("*", end="")
#     print()

# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ") 
#     print()
        

# n=int(input("Enter a number is : "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()
# print(chr(65))
# alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# n=5
# for i in range (1,n+1):
#     for j in range(i):
#         print(chr(65+j), end=" ")
#     print()




# l1=[1,2,3,4,5,6,7,8]
# temp=l1.copy()
# k=3
# max=None
# for i in range(0,k):
#     max=temp[0]
#     for j in temp:
#         if j>max:
#             max=j
#     temp.remove(max)

# print("MAx",max)
    