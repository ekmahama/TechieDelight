class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class sLinkedList:
    def construct(self, keys):
        root = None
        for val in reversed(keys):
            root = Node(val, root)
        return root

    def printList(self, root):
        ptr = root
        while ptr:
            print(f'{ptr.val}->', end='')
            ptr = ptr.next
        print('None')

    def addNode(self, root, neVal):
        newNode = Node(neVal)
        if not root:
            return newNode
        newNode.next = root
        return newNode

    def findVal(self, root, newVal):
        ptr = root
        while True:
            if ptr.val == newVal:
                return 'Value in list'
            ptr = ptr.next
            if not ptr:
                return 'Value not in list'


keys = [1, 2, 3, 4, 5]
examp = sLinkedList()
head = examp.construct(keys)
# examp.printList(head)
head = examp.addNode(head, 6)
examp.printList(head)
res = examp.findVal(head, 7)
print(res)
