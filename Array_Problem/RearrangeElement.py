num=[5,10,-3,-1,-10,6]
def RearrangeElementSign(nums):
    n=len(nums)
    result=[0]*n
    P=0
    N=1
    for i in range(0,n):
        if nums[i]>=0:
            result[P]=num[i]
            P+=2
        else:
            result[N]=nums[i]
            N+=2
    return result
print(RearrangeElementSign(num))