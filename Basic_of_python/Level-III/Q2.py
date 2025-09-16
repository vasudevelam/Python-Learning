#QUES 2: three subject input marks av , per ,grade
acc=float(input("Enter a com marks is: ="))
bst=float(input("Enter a bst number is : ="))
eco=float(input("Enter a eco marks is : ="))
marks=(acc+bst+eco)
a=marks/3
per= (marks/300)*100
print("3 SUBJECT OF AVERAGE IS : =",a)
print("3 SUBJECT OF PER IS : =",per)
if per>90:
    print(" GOOD MARKS ")
elif per>50:
    print("AVERAGE MARKS")
else:
    print("FAIL")
