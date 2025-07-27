matrix=[[1,2,3,4,5,6],[20,21,22,23,24,7],[19,32,33,34,25,8],[18,31,36,35,26,9],[17,30,29,28,27,10],[16,15,14,13,12,11]]
def SpiralOrder(matrix):
    if not matrix or not matrix[0]:
        return[]
    n=len(matrix)
    Left=0
    Top=0
    Right=len(matrix[0])-1
    Bottom=n-1
    Result=[]
    while Left<=Right and Top<=Bottom:
        for i in range(Left,Right+1):
            Result.append(matrix[Top][i])
        Top+=1
        for i in range(Top,Bottom+1):
            Result.append(matrix[i][Right])
        Right-=1
        if Top<=Bottom:
            for i in range(Right,Left-1,-1):
                Result.append(matrix[Bottom][i])
            Bottom-=1
        if Left<=Right:
            for i in range(Bottom,Top-1,-1):
                Result.append(matrix[i][Left])
            Left+=1
    return Result    
print(SpiralOrder(matrix))