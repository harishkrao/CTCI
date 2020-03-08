class LinkedList:
    def __init__(self, head):
        self.head = head
        self.next = None
  
    def add(self, node):
        temp = self.head
        self.head = node
        node.next = temp

    def traverse(self):
        print('Elements in linked list')
        curr = self.head
        while curr.next is not None:
            print(curr.value)
            curr = curr.next
        print(curr.value)

    def delete(self, value):
        if self.head is None:
            return 'Element not found'
        curr, prev = self.head, self.head
        while curr.next is not None:
            if curr.value == value:
                if prev == curr:
                    self.head = curr.next
                    return self.traverse()
                else:
                    prev.next = curr.next
                    return self.traverse()
            else:
                prev = curr
                curr = curr.next
        # print(curr.value, curr.next)
        if curr.value == value:
            curr.value = None


class Node:
    def __init__(self, val, next=None):
        self.value = val
        self.next = next

