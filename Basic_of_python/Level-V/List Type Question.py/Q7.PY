#Q7 SWAP THE NUMBER KTH ELEMENT AND SWAP USING LIST 


a=eval(input("Enter a list  : "))
k=int(input("Enter a number : "))
l=len(a)
a[k-1],a[l-k]=a[l-k],a[k-1]
print(a)