#Example 2:Min Stack Get Minimum 0,1  Leet Code 155
class MinStack(object):
    def __init__(self):
        self.items=[]
    def push(self,val):
        if len(self.items)==0:
            self.items.append([val,val])
        else:
            mini=min(val,self.items[-1][1])
            self.items.append([val,mini])

    def pop(self):
        return self.items[-1]
    def getMin(self):
        if (len(self.items)==0):
            return 0
        return self.items[-1][1]
    def Top(self):
        return self.items[-1][0]
    
        