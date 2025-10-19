#Q8 Area of Triangle
def triangle_area(height,base):
    height=float(height)
    base=float(base)
    area=0.5*height*base
    return area

height=input("Enter a height :")
base=input("ENter a base : ")
print(triangle_area(height,base))

