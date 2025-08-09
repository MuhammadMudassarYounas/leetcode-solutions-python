nums=[5,5,1,2,1,2,7,7,3]
def SingleNumber(nums):
    ans =0
    for i in nums:
        ans =ans^ i
    return ans
print(SingleNumber(nums))