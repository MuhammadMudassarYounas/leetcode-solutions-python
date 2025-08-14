#Example 3: Next Greater Element  //Geek For Geek Interview question
#Brute Solution
def NextGreater(nums):
    n=len(nums)
    result=[-1]*n 
    for i in range(0,n):
        for j in range(i+1,n):
            if nums[j]>nums[i]:
                result[i]=nums[j]
                break
    return result
print(NextGreater([19,4,2,11,6,5,3,10]))
#Optimal Solution
def NextGreaterElement(nums):
    n=len(nums)
    result=[-1]*n
    stack=[]
    for i in range(n-1,-1,-1):
        while len(stack)!=0 and nums[i]>=stack[-1]:
            stack.pop()
        if len(stack)!=0:
            result[i]=stack[-1]
        stack.append(nums[i])
    return result
print(NextGreaterElement([19,4,2,11,6,5,3,10]))


#Leet
stack = []
        next_greater = {}

        for num in nums2[::-1]:  # reverse iterate nums2
            while stack and num >= stack[-1]:
                stack.pop()
            if stack:
                next_greater[num] = stack[-1]
            else:
                next_greater[num] = -1
            stack.append(num)

        return [next_greater[num] for num in nums1]