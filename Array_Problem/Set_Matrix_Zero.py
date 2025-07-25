nums=[[1,2,3,4],[5,6,0,7],[8,0,9,1],[2,3,4,5]]
def SetZero(nums):
    Rows=len(nums)
    Columns=len(nums[0])
    RowTrack=[0 for i in range(Rows)]
    ColumnTrack=[0 for j in range(Columns)]
    for i in range(0,Rows):
        for j in range(0,Columns):
            if nums[i][j]==0:
                RowTrack[i]=-1
                ColumnTrack[j]=-1

    for i in range(0,Rows):
        for j in range(0,Columns):
            if RowTrack[i]==-1 or ColumnTrack[j]==-1:
                nums[i][j]=0
    return nums
print(SetZero(nums))