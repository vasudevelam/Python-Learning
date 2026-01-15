# # Take a list of numbers and separate it into two new lists — one containing even numbers and one containing odd numbers.

a=eval(input('Enter a number is : '))
even=[]
odd=[]
for i in a:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)


