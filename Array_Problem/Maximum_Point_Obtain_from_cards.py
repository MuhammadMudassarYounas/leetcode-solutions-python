#Example 4:Maximum Point You can Obtain from cards leet code 1423
def MaximumPoint(nums,k):
    n = len(nums)
    if k == n:
        return sum(nums)
    LSum = 0
    RSum = 0
    for i in range(0, k):
        LSum += nums[i]
    maxi = LSum
    right_index = n - 1
    for i in range(k - 1, -1, -1):
        LSum -= nums[i]           
        RSum += nums[right_index] 
        maxi = max(maxi, LSum + RSum)
        right_index -= 1
    return maxi

print(MaximumPoint([1,2,3,4,5,6,1],3))