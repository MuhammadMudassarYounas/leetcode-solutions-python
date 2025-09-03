#Example 6: Jump Game Leet Code 55
def JumpGame(nums):
    max_index=0
    for i in range(0,len(nums)):
        if i>max_index:
            return False
        max_index=max(max_index,i+nums[i])
    return True
print(JumpGame([3,2,1,4,0,2,1,5]))