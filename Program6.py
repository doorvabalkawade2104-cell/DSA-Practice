class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Add node at the end
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = new_node

    # Delete a node
    def delete_node(self, value):
        temp = self.head
        prev = None

        while temp:
            if temp.data == value:
                break

            prev = temp
            temp = temp.next

        if temp is None:
            print("Value is not there in the list")
            return

        # If deleting first node
        if prev is None:
            self.head = temp.next
        else:
            prev.next = temp.next

    # Display the linked list
    def print(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Creating linked list
list = LinkedList()

list.append(Node(10))
list.append(Node(20))
list.append(Node(30))
list.append(Node(40))

print("Original Linked List:")
list.print()

list.delete_node(20)

print("After deleting 20:")
list.print()

list.delete_node(50)