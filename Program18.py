# BST using Linked List (Nodes)

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # INSERT
    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
        else:
            temp = self.root

            while True:
                if new_node.data < temp.data:
                    if temp.left is None:
                        temp.left = new_node
                        return
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp = temp.right

    # DELETE NODE
    def del_node(self, rt, val):
        if rt is None:
            return None

        if val < rt.data:
            rt.left = self.del_node(rt.left, val)

        elif val > rt.data:
            rt.right = self.del_node(rt.right, val)

        else:
            # Node has no left child
            if rt.left is None:
                return rt.right

            # Node has no right child
            if rt.right is None:
                return rt.left

            # Node has both left and right children
            succ = self.get_successor(rt)
            rt.data = succ.data
            rt.right = self.del_node(rt.right, succ.data)

        return rt
    def search(self,key):
        temp=self.root
        while temp:
            if temp.data==key:
                return True
            elif key<temp.data:
                temp=temp.left
            else:
                temp=temp.right
        return False
    
    # GET SUCCESSOR
    def get_successor(self, temp):
        temp = temp.right

        while temp.left is not None:
            temp = temp.left

        return temp

    # INORDER
    def inorder(self, rt):
        if rt is None:
            return

        self.inorder(rt.left)
        print(rt.data, end=" ")
        self.inorder(rt.right)

    # PREORDER
    def preorder(self, rt):
        if rt is None:
            return

        print(rt.data, end=" ")
        self.preorder(rt.left)
        self.preorder(rt.right)

    # POSTORDER
    def postorder(self, rt):
        if rt is None:
            return

        self.postorder(rt.left)
        self.postorder(rt.right)
        print(rt.data, end=" ")

    # COUNT NODES
    def count(self, rt):
        if rt is None:
            return 0

        return 1 + self.count(rt.left) + self.count(rt.right)

    # FIND MINIMUM AND MAXIMUM
    def findminmax(self):
        if self.root is None:
            print("Tree is empty")
            return

        temp = self.root

        while temp.left is not None:
            temp = temp.left

        print("\nMin:", temp.data)

        temp = self.root

        while temp.right is not None:
            temp = temp.right

        print("Max:", temp.data)


# MAIN PROGRAM

b1 = BST()

b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(0))
b1.insert(Node(65))
b1.insert(Node(300))

print("\nInorder:")
b1.inorder(b1.root)

print("\nNo of nodes:", b1.count(b1.root))

print("\nPreorder:")
b1.preorder(b1.root)

print("\nPostorder:")
b1.postorder(b1.root)

b1.findminmax()

print("\nInorder before deletion:")
b1.inorder(b1.root)

# Delete node
b1.root = b1.del_node(b1.root,10 )

print("\nAfter deletion:")
b1.inorder(b1.root)

print("\nNo of nodes after deletion:", b1.count(b1.root))
if b1.search(450):
    print("\n Found the node")
else:
    print("\n not found")