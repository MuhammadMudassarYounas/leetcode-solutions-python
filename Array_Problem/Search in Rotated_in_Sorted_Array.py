#Example 3:Search in Rotated in Sorted Array LeetCode 81
num=[7,7,7,7,7,7,7,7,7,1,2,3,4,5,6,7,7,7]
def SearchRotated(nums,target):
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return True
        if nums[low]==nums[mid]==nums[high]:
            low+=1
            high-=1
            continue
        if nums[mid]<=nums[high]:
            if nums[mid]<=target<=nums[high]:
                low=mid+1
            else:
                high=mid-1
        else:
            if nums[low]<=target<=nums[mid]:
                high=mid-1
            else:
                low=mid+1
    return False
print(SearchRotated(num,6))