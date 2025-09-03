#Example 1: Assign Cookies Leet code 455
greedy=[2,6,8,1,4]
cookies=[4,2,7,1,2,3]
def AssignCookies(Greedy,cookies):
    Greedy.sort()
    cookies.sort()
    g=len(Greedy)
    c=len(cookies)
    left=0
    right=0
    count=0
    while left<g and right<c:
        if Greedy[left]<=cookies[right]:
            count+=1
            left+=1
        right+=1
    return count
print(AssignCookies(greedy,cookies))   