nums=[-2,1,-3,4,-1,2,1,-5,4]
def SubArraySum(nums):
    total=0
    maximum=float("-inf")
    for i in range(0,len(nums)):
        total=total+nums[i]
        if total>maximum:
            maximum=total
        if (total<0):
            total=0  
    return maximum
print(SubArraySum(nums))

