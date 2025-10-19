
# # #Create a 2D list (matrix) and print it row-wise using nested loops.
a=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=" ")
    print()     