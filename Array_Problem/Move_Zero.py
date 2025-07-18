def MoveZeroToRight(num):
    if len(num)==0:
        return
    i=0
    while i<len(num):
        if i==0:
            break
        i+=1
    if i==len(num):
        return
    j=i+1
    while j<len(num):
        if num[j]!=0:
            num[i],num[j]=num[j],num[i]
            i+=1
        j+=1
    print(num)
MoveZeroToRight(num)
    

