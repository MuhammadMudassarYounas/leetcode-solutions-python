def Fruit_In_Basket(nums):
    maxi=0
    n=len(nums)
    left=0
    right=0
    my_dic={}
    while right<n:
        my_dic[nums[right]]=my_dic.get(nums[right],0)+1
        if len(my_dic)>2:
            my_dic[nums[left]]-=1
            if my_dic[nums[left]]==0:
                del my_dic[nums[left]]
            left+=1
        if len(my_dic)<=2:
            maxi=max(maxi,right-left+1)
            right+=1
    return maxi 

print(Fruit_In_Basket([3,3,3,1,2,1,1,2,3,3,4]))
