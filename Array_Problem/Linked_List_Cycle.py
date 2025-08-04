#Example 3:Linked List Cycle Floyd Cycle Detection Leet code 141
#first make Linked List
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
    #Brute Solution:
    def Cycle(self):
        my_set=set()
        temp=self.head
        while temp is not None:
            if temp in my_set:
                return True
            my_set.add(temp)
            temp=temp.next    
            return False
    #optimal solution
    def CycleInLinkedList(self):
        slow=self.head
        fast=self.head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                return True
        return False
sll= Single_Linked_List()
sll.Append(10)
sll.Append(20)
sll.Append(30)
sll.Append(40)
sll.Append(50)
sll.Append(60)
print(sll.Cycle())
 