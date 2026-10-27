class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isempty():
            return None

        temp = self.top
        self.top = temp.next
        temp.next = None
        return temp.data

    def print(self):
        if self.isempty():
            print("Stack is empty")
            return

        temp = self.top
        while temp:
            print(temp.data)
            temp = temp.next

def reverse_stack(st1, st2):
    while not st1.isempty():
        value = st1.pop()
        st2.push(Node(value))


st1 = Stack()
st2 = Stack()

st1.push(Node(10))
st1.push(Node(20))
st1.push(Node(30))
st1.push(Node(40))
st1.push(Node(50))

print("Original stack:")
st1.print()

reverse_stack(st1, st2)

print("Reversed stack:")
st2.print()