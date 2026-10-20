class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Create Linked List / Insert at end
    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # 2. Traverse and print node values
    def traverse(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # 3. Insert node at a specific position (0-based)
    def insert_at_position(self, value, position):
        new_node = Node(value)

        if position < 0:
            print("Invalid position")
            return

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        index = 0

        while temp and index < position - 1:
            temp = temp.next
            index += 1

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        temp.next = new_node

    # 4. Find middle node
    def find_middle(self):
        if self.head is None:
            print("List is empty")
            return

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print("Middle node:", slow.data)

    # 5. Delete node by value
    def delete_node(self, value):
        temp = self.head
        prev = None

        while temp:
            if temp.data == value:
                break

            prev = temp
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        if prev is None:
            self.head = temp.next
        else:
            prev.next = temp.next

    # 6. Reverse linked list
    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev

    # 7. Sum of every two consecutive nodes
    def sum_consecutive(self):
        temp = self.head

        while temp and temp.next:
            total = temp.data + temp.next.data
            print(
                str(temp.data) + " + " +
                str(temp.next.data) + " = " + str(total)
            )
            temp = temp.next


# Main program
list1 = LinkedList()

# Create linked list
list1.append(10)
list1.append(20)
list1.append(30)
list1.append(40)
list1.append(50)

print("Original Linked List:")
list1.traverse()

# Insert at specific position
list1.insert_at_position(25, 2)
print("After inserting 25 at position 2:")
list1.traverse()

# Find middle node
list1.find_middle()

# Delete node
list1.delete_node(30)
print("After deleting 30:")
list1.traverse()

# Reverse linked list
list1.reverse()
print("Reversed Linked List:")
list1.traverse()

# Sum of consecutive nodes
print("Sum of consecutive nodes:")
list1.sum_consecutive() 