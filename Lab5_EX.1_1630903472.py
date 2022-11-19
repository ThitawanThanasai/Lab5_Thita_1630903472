class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = Node(data)
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def print_list(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next
print("LinkList")
head = LinkedList()
head.insert(1)
head.insert(2)
head.insert(3)
head.insert(4)
head.print_list()
