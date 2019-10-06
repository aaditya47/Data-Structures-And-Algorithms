'''
Implementation of linked list
Functions:
insert_to_head(element)- inserts an element to the head. Has a complexity of O(1)
insert_to_tail(element)- inserts an element to the tail. Has a complexity of O(n) in singly linked list and O(1) in doubly linked list
remove_from_head()- removes an element from the head and returns it. Has a complexity of O(1)
remove_from_tail()- removes an element from the tail and returns it. Has a complexity of O(n) in singly and O(1) in doubly linked list
size()- returns the size of the linked list. Has a complexity of O(1)
is_empty()- returns a boolean value denoting if the stack is empty. Has a complexity of O(1)
'''
class HeaderOrTrailer:
    def __init__(self):
        self.next=None
        self.prev=None # to be used only in doubly linked list

# Singly linked list node
class SinglyNode:
    def __init__(self,data):
        self.data=data
        self.next=None

# Doubly linked list node
class DoublyNode:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

# Implementation of singly linked list
class SinglyLinkedList:
    # Default constructor to initialize header and trailer pointers
    def __init__(self):
        self.header=HeaderOrTrailer()
        self.trailer=HeaderOrTrailer()
        self.sz=0
    # Insert to head
    def insert_to_head(self,element):
        new=SinglyNode(element)
        if(self.sz==0):
            self.header.next=new
            new.next=self.trailer
        else:
            self.header.next=new
        self.sz+=1
    # Insert to tail
    def insert_to_tail(self,element):
        new=SinglyNode(element)
        if(self.sz==0):
            self.header.next=new
            new.next=self.trailer
        else:
            temp=self.header.next
            while(temp.next!=self.trailer):
                temp=temp.next
            temp.next=new
            new.next=self.trailer
        self.sz+=1
    # Remove from head
    def remove_from_head(self):
        if(self.sz==0):
            print("List is empty")
            return None
        else:
            temp=self.header.next
            temp2=self.header.next.next
            self.header.next=temp2
            temp.next=None
            self.sz-=1
            return temp.data
    #Remove from tail
    def remove_from_tail(self):
        if(self.sz==0):
            print("List is empty")
            return None
        else:
            temp=self.header.next
            while(temp.next.next!=self.trailer):
                temp=temp.next
            temp2=temp.next
            temp.next=temp2.next
            temp2.next=None
            self.sz-=1
            return temp2.data
    # size
    def size(self):
        return self.sz
    # Is empty
    def is_empty(self):
        return self.sz==0

class DoublyLinkedList(SinglyLinkedList):
    # Default constructor to initialize header and trailer pointers
    def __init__(self):
        super()
    # Insert to head
    def insert_to_head(self,element):
        new=DoublyNode(element)
        if(self.sz==0):
            self.header.next=new
            new.prev=self.header
            new.next=self.trailer
            self.trailer.prev=new
        else:
            self.header.next=new
        self.sz+=1
    # Insert to tail
    def insert_to_tail(self,element):
        new=SinglyNode(element)
        if(self.sz==0):
            self.header.next=new
            new.prev=self.header
            new.next=self.trailer
            self.trailer.prev=new
        else:
            temp=self.trailer.prev
            temp.next=new
            new.next=self.trailer
            self.trailer.prev=new 
        self.sz+=1
    # Remove from head
    def remove_from_head(self):
        if(self.sz==0):
            print("List is empty")
            return None
        else:
            temp=self.header.next
            temp2=temp.next
            self.header.next=temp2
            temp2.prev=self.header
            temp.next=None
            temp.prev=None
            self.sz-=1
            return temp.data
    # Remove from tail
    def remove_from_tail(self):
        if(self.sz==0):
            print("List is empty")
            return None
        else:
            temp=self.trailer.prev
            temp2=temp.prev
            temp2.next=temp.next
            self.trailer.prev=temp2
            self.sz-=1
            return temp.data
    # Size
    def size(self):
        return self.sz
    # Is empty
    def is_empty(self):
        return self.sz==0