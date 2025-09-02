def LongestSubStringCharacter(s):
    my_dic={}
    left=0
    right=0
    maxi=0
    n=len(s)
    while right<n:
        if s[right] in my_dic:
            left=max(left,my_dic[s[right]]+1)
        maxi=max(maxi,right-left+1)
        my_dic[s[right]]=right
        right+=1
    return maxi

print(LongestSubStringCharacter("CADBZABCD"))