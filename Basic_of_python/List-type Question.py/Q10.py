
# Find the intersection and union of two lists (without using set).
a=[1,2,3,4,5,6]
b=[4,5,6,7,8,9]
c=a+b

inte=[]
union=[]
for i in c:
    if i not in union:
        union.append(i)
print("Union : ",union)

for j in c:
    if c.count(j)>1:
        if j not in inte:
            inte.append(j)
print("Inteesection :", inte)
        






