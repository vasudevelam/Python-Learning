n=int(input("Enter a number is : ="))
i=1
for i in range(1,n+1):
    if i==1:
        print("1=1")
    else:
        x=0
        for j in range(2,i):
            if i%j==0:
                x=x+1
                break
            if x==0:
                print(i,"=",i,"(Prime)")
            else:
                num=i
                f=[]
                a=2
                while num>1:
                    if num%a==0:
                        f.append(str(a))
                        num//=a
                    else:
                        a=a+1
                        print(i,"=","x".join(f))

    
        
