# Create a function that prints the multiplication table of a number

def table(num):
    for i in range(1,11):
        print(num,'x',i,'=',num*i)
    return ''
    

    
num=int(input('Enter a number is : '))
print(table(num))