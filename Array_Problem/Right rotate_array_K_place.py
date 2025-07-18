#Example 4: Right rotate an array by K place
num=[1, 2, 3, 4, 5, 6, 7, 9]
nums=[1, 2, 3, 4, 5, 6, 7, 9]
def BruteSol(num,k):
    # n=k%len(num)
    for i in range(0,k):
        e=num.pop()
        num.insert(0,e)
    print(num)

BruteSol(num,3)

def BetterSol(num,k):
    n=len(num)
    num[:]=num[-k:]+num[:-k]
    print(num)
BetterSol(nums,3)