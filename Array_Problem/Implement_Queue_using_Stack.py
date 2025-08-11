from collections import deque

class QueueUsingStack:
    def __init__(self):
        self.st1=deque()
        self.st2=deque()

    def push(self,items):
        while self.st1:
            self.st2.append(self.st1.pop())
        self.st1.append(items)
        while self.st2:
            self.st1.append(self.st2.pop())

    def pop(self):
        return self.st1.pop()
    
QUS=QueueUsingStack()
QUS.push(1)
QUS.push(2)
QUS.push(3)
QUS.push(4)
print(QUS.pop())
