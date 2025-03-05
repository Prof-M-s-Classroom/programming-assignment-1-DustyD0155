class Node:
    """
    Node class to be used in the linked list implementation of the stack.
    """
    def __init__(self, data):
        """Initialize a node with data and a pointer to the next node."""
        self.data = data
        self.next = None

class CircularStack:
    """
    Circular stack class using a linked list with a maximum size of 5 elements.
    """
    MAX_SIZE = 5

    def __init__(self):
        """Initialize the stack with an empty state."""
        self.head = None
        self.size = 0

    def push(self, temperature, humidity):
        """Add a new Temperature object to the stack, replacing the oldest entry if full."""
        new_node = Node(temperature)
        if self.size == 0:
            self.head = new_node

        elif self.size == CircularStack.MAX_SIZE:
            self.pop()
            new_node.next = self.head
            self.head = new_node

        self.size += 1
        return None

    def pop(self):
        """Remove the oldest entry from the stack."""
        current = self.head
        if self.size == 0:
            raise IndexError("Circular stack is empty")

        elif self.size == CircularStack.MAX_SIZE:
            for i in range(CircularStack.MAX_SIZE - 2):
                current = current.next
            current.next = None
        else:
            for i in range(self.size - 2):
                current = current.next
            current.next = None
            self.size -= 1
        return None


    def peek(self):
        """Return the most recent temperature entry without removing it."""
        return self.head.data

    def print_stack(self):
        """Print all stored readings in order from oldest to newest."""
        end_index = CircularStack.MAX_SIZE - 1
        current = self.head
        while end_index >= 0:
            for i in range(end_index):
                current = current.next
            print(current.data)
        return None



    def is_empty(self):
        """Return True if the stack is empty, otherwise False."""
        if self.size == 0:
            return True
        else:
            return False
