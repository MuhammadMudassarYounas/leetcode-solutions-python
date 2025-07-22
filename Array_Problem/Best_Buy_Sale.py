nums=[8,7,6,5,4,3,2,1]
def BestBuySell(nums):
    min=float("inf")
    max=0
    for i in range(0,len(nums)):
        if nums[i]<min:
            min=nums[i]
        profit=nums[i]-min
        max= max(max, profit)
        if max<0:
            return 0
    return max
print(BestBuySell(nums))