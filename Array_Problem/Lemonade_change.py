#Example 4:Lemonade change  leet code 860 
def lemonadeChange(bill):
    five=0
    ten=0
    n=len(bill)
    for i in range(0,n):
        if bill[i]==5:
            five+=1
        elif bill[i]==10:
            if five>=1:
                five-=1    
                ten+=1
            else:
                return False
        else:
            if five>=1 and ten>=1:
                five-=1
                ten-=1
            elif five>=3:
                five-=3
            else:
                return False
    return True
print(lemonadeChange([5,5,5,10,10,20]))
            