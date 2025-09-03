#Example 7 Jump Game 2 Leet code 45
#Optimal Solution
def GameJump(nums):
    jump=0
    left=0
    right=0
    while right<len(nums)-1:
        fastest=0
        for i in range(left,right+1):
            fastest=max(fastest,i+nums[i])
        left=right+1
        right=fastest
        jump+=1
    return jump
print(GameJump([2,3,5,4,1,1,1,4]))

