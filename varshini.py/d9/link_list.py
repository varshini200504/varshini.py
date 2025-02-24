class LinkedList:
    def __init__(self):
        self.start=None

    def insert_front(self,data):
        new_node=Node(data)
        if self.start==None:
            self.start=new_node
        else:
            new_node.next=self.start
            self.start=new_node

    def insert_end(self,data):
        new_node=Node(data)
        if self.start==None:
            self.start=new_node
            return
        temp=self.start
        while temp.next!=None:
            temp=temp.next
        temp.next=new_node

    def display(self):
        temp=self.start
        while temp!=None:
            print(temp.data,end=' ')
            temp=temp.next


    def insert_pos(self,data):
        new_node=Node(data)
        pos=int(input("enter the position tht u want to insert:"))
        temp=self.start
        prev=temp
        if self.start==None:
            self.start=new_node
        for i in range(1,pos):
            prev=temp
            temp=temp.next
        prev.next=new_node
        new_node.next=temp

    def delete_front(self):
        if self.start==None:
            print("list is empty")
        temp=self.start
        self.start=self.start.next

    def delete_end(self):
        if self.start==None:
            print("list is empty")
        elif self.start.next==None:
            self.start=None
        else:
            temp=self.start
            prev=temp
            while temp.next!=None:
                prev=temp
                temp=temp.next
            prev.next=None
            

    def delete_pos(self,pos):
        if self.start==None:
            print("list is empty")
            return 
        
        temp=self.start
        prev=temp
        if pos==0:
            self.start=self.start.next
            temp=None
            return
        for i in range(pos-1):
            prev=temp
            temp=temp.next
            if temp==None:
                print("position out  of range")
                return
        if temp.next==None:
            print("position out of range")
            return
        prev.next=temp.next
        temp=None


        



        
    
class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None


    

l1=LinkedList()
l1.insert_front(9)
l1.insert_end(12)
l1.delete_pos(1)
l1.display()