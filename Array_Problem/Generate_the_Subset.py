#Example 3: Generate the Subset of Array LeetCode 78
num=[1,2,3]
def GenerateSubSet(nums):
    n=len(nums)
    total_subset=1<<n
    Result=[]
    for num in range(0,total_subset):
        lst=[]
        for i in range(0,n):
            if(num & (1<<i)!=0):
                lst.append(nums[i])
        Result.append(lst)
    return Result

print(GenerateSubSet(num))