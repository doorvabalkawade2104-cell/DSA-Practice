class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class LQueue:
    def __init__(self):
        self.front=self.rear=None
    def enqueue(self,new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node

    def dequeue(self):
        temp=self.front
        print("Deleted node:",temp.data)
        self.front=self.front.next

        if self.front==None:        #if there is only one node
            self.rear=None
            print("que is empty")
        temp=None

    def print(self):
        temp=self.front
        while temp:
            print(temp.data, end="->")
            temp=temp.next
        print("None")


que=LQueue()
que.enqueue(Node(23))
que.enqueue(Node(63))
que.enqueue(Node(78))
que.enqueue(Node(20))

que.print()
que.dequeue()
que.dequeue()
que.dequeue()
que.dequeue()
que.print()