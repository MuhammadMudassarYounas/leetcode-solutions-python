#Example 2: Reverse a Linked List LeetCode 206
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
    #Brute Solution:
    def Reverse(self):
        temp=self.head
        stack=[]
        while temp is not None:
            stack.append(temp.val)
            temp=temp.next
        temp=self.head
        while temp is not None:
            temp.val=stack.pop()
            temp=temp.next
        return self.head
    def ReverseLinkedList(self):
        temp=self.head
        prev=None
        
        while temp is not None:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
            self.head=prev
        return self.head
sll= Single_Linked_List()
sll.Append(10)
sll.Append(20)
sll.Append(30)
sll.Append(40)
sll.Append(50)
sll.Append(60)
sll.Reverse()