#QUES Q5: print pattern
n='*'
a=int(input("Enter a number"))
# print("n",n,)
# print("n",n,"*")
# print("n",n,"*","*")
# print("n",n,"*","*","*")
# print("n",n,"*","*","*","*","*")
i=1
for i in range(1,a):
    i=i*n
    print(i)

