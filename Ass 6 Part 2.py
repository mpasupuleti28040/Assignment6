# Array Implementation
class Array:
    def __init__(self, size):
        self.array = [None] * size
        self.size = size
        self.length = 0

    # Insert element at a specific index
    def insert(self, index, value):
        if self.length >= self.size:
            raise Exception("Array is full")
        if index < 0 or index > self.length:
            raise IndexError("Index out of bounds")
        for i in range(self.length, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = value
        self.length += 1

    # Delete element at a specific index
    def delete(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        value = self.array[index]
        for i in range(index, self.length - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.length - 1] = None
        self.length -= 1
        return value

    # Access element at a specific index
    def access(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        return self.array[index]

    # Display array
    def display(self):
        return [self.array[i] for i in range(self.length)]


# Matrix Implementation
class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    # Insert element at a specific position
    def insert(self, row, col, value):
        if row >= self.rows or col >= self.cols:
            raise IndexError("Index out of bounds")
        self.matrix[row][col] = value

    # Access element at a specific position
    def access(self, row, col):
        if row >= self.rows or col >= self.cols:
            raise IndexError("Index out of bounds")
        return self.matrix[row][col]

    # Display matrix
    def display(self):
        for row in self.matrix:
            print(row)


# Stack Implementation
class Stack:
    def __init__(self, capacity):
        self.stack = [None] * capacity
        self.capacity = capacity
        self.top = -1

    # Push an element onto the stack
    def push(self, value):
        if self.top >= self.capacity - 1:
            raise Exception("Stack Overflow")
        self.top += 1
        self.stack[self.top] = value

    # Pop an element from the stack
    def pop(self):
        if self.top == -1:
            raise Exception("Stack Underflow")
        value = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return value

    # Peek the top element of the stack
    def peek(self):
        if self.top == -1:
            return None
        return self.stack[self.top]

    # Display the stack
    def display(self):
        return [self.stack[i] for i in range(self.top + 1)]


# Queue Implementation
class Queue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    # Enqueue an element to the queue
    def enqueue(self, value):
        if self.size == self.capacity:
            raise Exception("Queue Overflow")
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1

    # Dequeue an element from the front
    def dequeue(self):
        if self.size == 0:
            raise Exception("Queue Underflow")
        value = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value

    # Display the queue
    def display(self):
        return [self.queue[(self.front + i) % self.capacity] for i in range(self.size)]


# Singly Linked List Implementation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert element at the end of the list
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Delete a node by value
    def delete(self, key):
        current = self.head

        # If the head node itself holds the key
        if current is not None:
            if current.data == key:
                self.head = current.next
                current = None
                return

        # Search for the key to be deleted
        prev = None
        while current is not None:
            if current.data == key:
                break
            prev = current
            current = current.next

        # If the key is not present
        if current is None:
            return "Node not found"

        # Unlink the node from the linked list
        prev.next = current.next
        current = None

    # Display the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Rooted Tree Using Linked Lists
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    # Add a child node
    def add_child(self, child_node):
        self.children.append(child_node)

    # Display tree structure
    def display(self, level=0):
        print(" " * level + str(self.value))
        for child in self.children:
            child.display(level + 2)


# Example Usage

# Arrays
array = Array(5)
array.insert(0, 10)
array.insert(1, 20)
array.insert(2, 30)
print("Array:", array.display())

# Matrices
matrix = Matrix(3, 3)
matrix.insert(0, 0, 1)
matrix.insert(1, 1, 5)
matrix.insert(2, 2, 9)
print("Matrix:")
matrix.display()

# Stack
stack = Stack(5)
stack.push(10)
stack.push(20)
stack.push(30)
print("Stack:", stack.display())
stack.pop()
print("Stack after pop:", stack.display())

# Queue
queue = Queue(5)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print("Queue:", queue.display())
queue.dequeue()
print("Queue after dequeue:", queue.display())

# Linked List
ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
print("Linked List:")
ll.display()
ll.delete(2)
print("Linked List after deletion:")
ll.display()

# Rooted Tree
root = TreeNode(1)
child1 = TreeNode(2)
child2 = TreeNode(3)
root.add_child(child1)
root.add_child(child2)
child1.add_child(TreeNode(4))
child1.add_child(TreeNode(5))
child2.add_child(TreeNode(6))
print("Tree:")
root.display()
