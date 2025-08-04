#Remove the nth element of linked list leet code 19  
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
    def Remove(self):
        n=2
        length=0
        temp=self.head
        while temp is not None:
            length+=1
            temp=temp.next
        if length == n:
            new_node=self.head.next
            del new_node
            return new_node 
        Total=length-n
        temp=self.head
        count=1
        while count<Total:
            temp=temp.next
            count+=1 
        temp.next=temp.next.next
        return self.head
     #optimal solution
    def RemoveElement(self):
        n=3
        temp=self.head
        prev=self.head
        for i in range(n):
            temp=temp.next
        if temp==None:
           new_node=self.head.next
           del self.head
           return new_node
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=prev.next.next
        return self.head


sll= Single_Linked_List()
sll.Append(10)
sll.Append(20)
sll.Append(30)
sll.Append(40)
sll.Append(50)
sll.Append(60)
sll.Remove()