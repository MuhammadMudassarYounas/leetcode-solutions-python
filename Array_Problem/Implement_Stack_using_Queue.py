from collections import deque

class StackUsingQueue:
    def __init__(self):
        self.items=deque()
    def enqueue(self,item):
        self.items.append(item)
        for i in range(len(self.items)-1):
            self.items.append(self.items.popleft())
    
    def pop(self):
        if len(self.items)==0:
            print("Stack is Empty")
        x=self.items.popleft()
        return x
    
SUQ=StackUsingQueue()
SUQ.enqueue(1)
SUQ.enqueue(2)
SUQ.enqueue(3)
SUQ.enqueue(4)
SUQ.enqueue(5)
print(SUQ.pop())