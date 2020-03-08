class LinkedList:
    def __init__(self, head=None):
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


def rearrange(linkedlist):
    if type(linkedlist) != LinkedList:
        raise ValueError('Not a linked list')

    p1 = linkedlist.head
    p2 = linkedlist.head.next
    
    while p2.next is not None:    
        p1 = p1.next
        p2 = p2.next.next
        print(p1.value, p2.value)
    p2 = p1.next
    p1 = linkedlist.head
    while p1.next is not None:
        temp = p1.next
        p1.next = p2
        p2.next = temp
        print(p1.value, p2.value)
        p1 = p1.next
        p2 = p2.next


linkedlist = LinkedList()
n12 = Node(1)
n11 = Node(2)
n10 = Node(3)
n9 = Node(4)
n8 = Node(5)
n7 = Node(6)
n6 = Node(10)
n5 = Node(20)
n4 = Node(30)
n3 = Node(40)
n2 = Node(50)
n1 = Node(60)
linkedlist.add(n1)
linkedlist.add(n2)
linkedlist.add(n3)
linkedlist.add(n4)
linkedlist.add(n5)
linkedlist.add(n6)
linkedlist.add(n7)
linkedlist.add(n8)
linkedlist.add(n9)
linkedlist.add(n10)
linkedlist.add(n11)
linkedlist.add(n12)
linkedlist.traverse()
rearrange(linkedlist)
