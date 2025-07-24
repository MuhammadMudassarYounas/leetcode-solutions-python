num=[1,99,101,98,2,5,3,100,1,1]
def LongestConsecutive(nums):
    nums.sort()
    last_Small=float("-inf")
    count=0
    max_count=0
    for i in range(0,len(nums)):
        if nums[i]-1==last_Small:
            count+=1
            last_Small=nums[i]
        elif nums[i]!=last_Small:
            count =1
            last_Small=nums[i]
        max_count=max(max_count,count)
    return max_count
print(LongestConsecutive(num))