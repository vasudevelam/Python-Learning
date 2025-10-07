pr=input("Enter a purchase iteam is:=")
pri=int(input("Enter a price is:="))
oq=int(input("Enter a quantiy of iteam is:="))


gst=int(input("Enter a gst is:="))
v=(pri*oq)
fv=v+(v*(gst/100))
print("store bill ")
print("purchase item is =",pr)
print("Price  of Iteam is=",pri)
print("quantity of iteam is=",oq)
print("Final bill is=",fv)