#Example 1: Middle of the Linked List LeetCode 876
#first make linked list
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class Single_Linked_List:
    def __init__(self):
        self.head=None
    def Append(self,val):
        new_Node=Node(val)
        if self.head==None:
            self.head=new_Node
        else:
            curr =self.head
            while curr.next is not None:
                curr= curr.next
            curr.next=new_Node
    #Brute Solution
    def Middle(self):
        temp=self.head
        n=0
        while temp is not None:
            n+=1
            temp=temp.next
        temp=self.head
        for i in range(0,n//2):
            temp=temp.next
        return temp.val
    #Optimal Solution: Use Tortoise and Hare Approach
    def MiddleElement(self):
        slow=self.head
        fast=self.head
        while fast!=None and fast.next!=None:
            fast=fast.next.next
            slow=slow.next
        return slow.val

sll= Single_Linked_List()
sll.Append(10)
sll.Append(20)
sll.Append(30)
sll.Append(40)
sll.Append(50)
sll.Append(60)
print(sll.Middle())
print(sll.MiddleElement())