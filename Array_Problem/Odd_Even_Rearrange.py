#Odd Even Linked list Rearrange Nodes leet code 328  
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
    def OddEven(self):
        result=[]
        temp=self.head
        while temp and temp.next:
            result.append(temp.val)
            temp=temp.next.next
        temp=self.head.next
        while temp and temp.next:
            result.append(temp.val)
            temp=temp.next.next
        index=0
        while temp is not None:
            temp.val=result[index]
            index+=1
            temp=temp.next
    #optimal solution
    def OddEvenLinkedList(self):
        if self.head and self.head.next is None:
            return self.head
        odd=self.head
        even=self.head.next
        even_head=even
        while even is not None and even.next is not None:
            odd.next=odd.next.next
            odd=odd.next
            even.next=even.next.next
            even=even.next
        odd.next=even_head
        return self.head
        
sll= Single_Linked_List()
sll.Append(10)
sll.Append(20)
sll.Append(30)
sll.Append(40)
sll.Append(50)
sll.Append(60)
sll.Append(70)
print(sll.OddEvenLinkedList())