'''
Array Implementation of Stack
Functions:
push(element)- pushes element into the top of the stack. Has a complexity of O(1)
pop()- pops element off the top of the stack and returns it. Has a complexity of O(1)
peek()- returns the topmost element of the stack. Has a complexity of O(1)
size()- returns real time size of the stack. Has a complexity of O(1)
is_empty()- returns a boolean value which shows if the stack is empty. Has a complexity of O(1)
'''

class Stack:
    # Parametrized constructor which sets the size of the stack
    def __init__(self,size):
        self.container=[None]*size
        self.size=size
        # 2 variables sz and top: sz to denote the real time size of stack and top to denote the top index of stack
        self.sz=0
        self.top=-1
    # push function
    def push(self,element):
        if(self.top<=self.size-1):
            self.top+=1
            self.container[self.top]=element
            self.sz+=1
            self.print_stack()
        else:
            print("Stack is full")
    # pop function
    def pop(self):
        if(self.top>-1):
            temp=self.container[self.top]
            self.container[self.top]=None
            self.top-=1
            self.sz-=1
            self.print_stack()
            return temp
        else:
            print("Stack is empty")
            return None
    def peek(self):
        return self.container[self.top]
    # size function
    def size(self):
        return self.sz
    # isempty function
    def is_empty(self):
        return self.sz==0
    # print stack function - arbitrary function to help visualizing
    def print_stack(self):
        print(self.container)