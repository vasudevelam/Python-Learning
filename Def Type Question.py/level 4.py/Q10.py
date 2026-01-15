# create afunction odd even ,multiple of tables an check number larger smallest and factorala

def multe_fun():
    for i in range(100):
        print("1.Check Even/odd")
        print("2.Multiple")
        print("3.Check largest/smallest")
        print("4.Exist")
        choice=int(input("Enter choice (1 tO 4:  )"))
        if choice==1:
            num=int(input("Enter a numbers is : "))
            if num%2==0:
                print("Even number ",num)
            else:
                print("Odd number ",num)
        elif choice==2:
            num=int(input("Enter a numbers is : "))
            for i in range(1,11):
                print(num,"*",i,"=",num*i)
        elif choice==3:
            a=int(input("Enter a 1 numbers is : "))
            b=int(input("Enter a 2 number is : "))
            if a>b:
                print("1 is Largest number ",a) 
            elif b>a:
                print("2 is largest number ",b)
            else:
                print("Both are same",a,b)
        elif choice==4:
            print("Exist")
            break
        else:
            print("Invalid ")

multe_fun()
