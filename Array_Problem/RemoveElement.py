def removeElement(nums, val):
    count =0
    for i in nums:
            if(nums[i] != val):
                nums[count] =nums[i]
                count+=1
    return count

# print(removeElement([3,2,3,2], 3))
print(removeElement([0,1,2,2,3,0,4,2],2))