num=[1,3,4,5,8,9,14,15,19,20,21]
def SearchInsert(nums,target):
    n=len(nums)
    lowerIndex=n
    low=0
    high=len(nums)-1
    while low<=high:
        mid =(low+high)//2
       
        if nums[mid] >=target:
            lowerIndex=mid
            high=mid-1
          
        else:
            low=mid+1  
    return lowerIndex
print(SearchInsert(num,2))