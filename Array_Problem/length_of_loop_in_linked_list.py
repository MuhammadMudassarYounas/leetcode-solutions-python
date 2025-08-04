#find length of loop in linked list  
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
    def length(self):
        temp=self.head
        travel=0
        my_dict={}
        while temp is not None:
            if temp in my_dict:
                return travel-my_dict[temp]
            my_dict[temp]=travel  
            travel+=1
            temp=temp.next
        return 0
     #optimal solution
    def LengthOfLoop(self):
        slow =self.head
        fast=self.head
        travel=0
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                slow=slow.next
                travel=1
                while slow!=fast:
                    slow=slow.next
                    travel+=1
                return travel
        return 0

sll= Single_Linked_List()
sll.Append(10)
sll.Append(20)
sll.Append(30)
sll.Append(40)
sll.Append(50)
sll.Append(60)