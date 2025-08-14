#Example 4 :Next Greater Element Leet Code 503

def NextGreaterElement(nums):
    n=len(nums)
    result=[-1]*n
    stack=[]
    for i in range(2*n-1,-1,-1):
        while len(stack)!=0 and nums[i%n]>=stack[-1]:
            stack.pop()
        if i<n:
            if len(stack)!=0:
                result[i]=stack[-1]
        stack.append(nums[i%n])
    return result
print(NextGreaterElement([2,10,12,1,11]))