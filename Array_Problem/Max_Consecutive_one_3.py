def MaxConsecutiveOnes(nums,k):
    maxi=0
    left=0
    right=0
    zero=0
    n=len(nums)
    while right<n:
        if nums[right]==0:
            zero+=1
        if zero>k: 
            if nums[left]==0:
                zero-=1      
            left+=1
        if zero<=k:
            maxi=max(maxi,right-left+1)
        right+=1
    
    return maxi

print(MaxConsecutiveOnes([1,1,1,0,0,0,1,1,1,1,0],2))