Matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#Optimal Solution
def RotateMatrix(Matrix):
    n=len(Matrix)
    for i in range(0,n-1):
        for j in range(i+1,n):
            #Taking transpose
            Matrix[i][j],Matrix[j][i]=Matrix[j][i],Matrix[i][j]
    for i in range(0,n):
        Matrix[i].reverse()
    return Matrix
print(RotateMatrix(Matrix))
       