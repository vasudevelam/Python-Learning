#Q11 Fibonacci Series up to n terms
def facb(n):
    a=0
    b=1
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b
        
facb(10)