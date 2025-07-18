#Example 2:Find missing number in list
#brute Solution
num=[1,0,2,3,4,6,7,8,9]
n=9
def MissingNumber(num,n):
    i=0
    while i<=n:
        if (i not in num):
            return i
        i+=1    
print(MissingNumber(num,n))

def MissingNumberList(num,n):
    frequency={}
    for i in range(0,n+1):
        frequency[i]=0
    for j in num:
        frequency[j]=1
    for k,v in frequency.items():
        if v==0:
            return k
print(MissingNumberList(num,9))
