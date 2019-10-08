'''
Implementation of Binary Tree data structure
'''

class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

class BinaryTree:
    def __init__(self):
        self.root=None
        self.q=[]
    def set_root(self,root):
        self.root=root
    def inorder(self,root):
        if(root!=None):
            inorder(root.left)
            print(root.data)
            inorder(root.right)
    def preorder(self,root):
        if(root!=None):
            print(root.data)
            preorder(root.left)
            preorder(root.right)
    def postorder(self,root):
        if(root!=None):
            postorder(root.left)
            postorder(root.right)
            print(root.data)
    def levelorder(self,root):
        print(root.data)
        if(len(q)!=0):
            if(self.is_leaf(root)==False):
                self.q.append(root.left)
                self.q.append(root.right)
            a=self.q.pop(0)
            self.levelorder(a)
    def is_leaf(self,node):
        return node.left==None and node.right==None
