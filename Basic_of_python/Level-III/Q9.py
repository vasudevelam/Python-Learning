#QUES 9: input secon and converte hours , minute
sec=float(input("ENter second is : ="))
hor=(sec//3600)
min=(sec%60)//60
sec=(sec%60)
print(hor,":",min,":",sec)