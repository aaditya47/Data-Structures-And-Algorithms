'''
Array Implementation of Queue
Functions:
enqueue(element)- adds element into the rear of the queue. Has a complexity of O(1)
dequeue()- removes element off the front of the queue and returns it. Has a complexity of O(1)
front()- returns the frontmost element of the queue. Has a complexity of O(1)
size()- returns real time size of the queue. Has a complexity of O(1)
is_empty()- returns a boolean value which shows if the queue is empty. Has a complexity of O(1)
'''

class Queue:
    # Parametrized constructor which sets the size of the queue
    def __init__(self,size):
        self.container=[None]*size
        self.size=size
        self.sz=0
        self.front=self.rear=-1
    # Enqueue function
    def enqueue(self,element):
        if(self.rear<=self.size-1):
            if(self.rear==self.front==-1):
                self.front+=1
                self.rear+=1
            else:
                self.rear+=1
            self.container[self.rear]=element
            self.sz+=1
            self.print_queue()
        else:
            print("Queue is empty")
    # Dequeue function
    def dequeue(self):
        if(self.is_empty()==True):
            print("Queue is empty")
            return None
        else:
            temp=self.container[self.front]
            self.container[self.front]=None
            self.front+=1
            self.sz-=1
            self.print_queue()
            return temp
    # Front function
    def front(self):
        return self.container[self.front]    
    # Size function
    def size(self):
        return self.sz
    # Is empty function
    def is_empty(self):
        return self.sz==0
    # Print queue function
    def print_queue(self):
        print(self.container)