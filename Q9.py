#Q9 Area of Circle
def circle_area(r):
    r=float(r)
    pi=float(3.14)
    area=pi*r*r
    return area


r=input("Enter a number :")
print(circle_area(r))
