class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertEnd(self, data):
        newNode = Node(data)
        if (self.head):
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def insertF(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insertBtw(self, pos, data):
        if (pos == 1):
            self.insertF(data)
        elif (pos > self.len()):
            self.insertEnd(data)
        newNode = Node(data)
        if (self.head):
            count = 1
            current = self.head
            while (pos-1) != count:
                current = current.next
                count += 1
            newNode.next = current.next
            current.next = newNode

    def len(self):
        count = 0
        current = self.head
        while (current):
            count += 1
            current = current.next
        return count

    def pop(self):
        if self.head is None:
            print("The list is empty")
        else:
            self.head = self.head.next

    def pop_End(self):
        current = self.head
        if self.head is None:
            print("The list is empty")
        elif self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            current.next = None

    def pop_Btw(self, pos):
        if pos == 1:
            self.pop()
        elif pos >= self.len():
            self.pop_End()
        else:
            count = 2
            current = self.head
            while (pos) != count:
                current = current.next
                count += 1
            current.next = current.next.next

    def printr(self):
        current = self.head
        while (current):
            print(current.data, end="->")
            current = current.next
        print(" ")


ll = LinkedList()
ll.insertEnd(1)
ll.insertEnd(3)
ll.insertEnd(4)
ll.insertBtw(2, 2)
ll.pop_Btw(3)
ll.printr()
