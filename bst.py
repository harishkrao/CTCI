class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None

    def get(self):
        return self.val

    def set(self, val):
        self.val = val

    def getChildren(self):
        children = []
        if self.leftChild is not None:
            children.append(self.leftChild)
        if self.rightChild is not None:
            children.append(self.rightChild)
        return children


class BST:
    def __init__(self):
        self.root = None

    def setRoot(self, val):
        self.root = Node(val)

    def insert(self, val):
        return self.insertNode(val, self.root)

    def insertNode(self, val, rootval):
        while rootval.leftChild is not None and rootval.rightChild is not None:
            if rootval > val:
                rootval = rootval.rightChild
                return self.insertNode(val, rootval)
            elif rootval < val:
                rootval = rootval.leftChild
                return self.insertNode(val, rootval)
        if val > rootval:
            rootval.rightChild = Node(val)
        else:
            rootval.leftChild = Node(val)


    def find(self, val):
        return self.findNode(val, self.root)

    def findNode(self, val, rootval):
        if self.root.val == val:
            return "found"
        else:
            while self.root.leftChild is not None and self.root.rightChild is not None:
                if self.root > val:
                    rootval = rootval.leftChild
                    return self.findNode(val, rootval)
                else:
                    rootval = rootval.rightChild
                    return self.findNode(val, rootval)
        return "not found"
