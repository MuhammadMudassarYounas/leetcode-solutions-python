#Example 2:Search in Rotated Sorted in Array LeetCode 33
num=[17,18,20,1,3,4,5,7,8,10,11,13,14,16]
def SearchRotated(nums,target):
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
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
    return -1
print(SearchRotated(num,6))