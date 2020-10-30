class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printList(head):
    ptr = head
    while ptr:
        print(f'{ptr.val}->', end='')
        ptr = ptr.next
    print('None')


class creatList:
    def method3(self, A):
        # Method 3 : suitable for large array, space : 0(1)
        prev = head = None
        for val in A:
            node = Node(val, None)
            if prev == None:
                head = node
            else:
                prev.next = node
            prev = node
        return head

    def cloneList(self, head):
        # Naive method
        current = head
        newList = None
        tail = None

        while current:
            if not newList:
                newList = Node(current.val, newList)
                tail = newList
            else:
                tail.next = Node(current.val)
                tail = tail.next
            current = current.next
        return newList

    def copyList(self, head):
        # Using push method
        current = head
        newList = None
        tail = None

        while current:
            if not newList:
                newList = Node(current.val, newList)
                tail = newList
            else:
                # Add each node to the tail
                tail.next = Node(current.val, tail.next)
                tail = tail.next  # Advance the tail to the new node
            current = current.next  # Advance head of the origina list ot the next node
        return newList

    def copyListv1(self, head):
        # Using push method
        current = head
        dummy = tail = Node()

        while current:
            if not tail:
                tail = Node(current.val, tail)
            else:
                # Add each node to the tail
                tail.next = Node(current.val, tail.next)
                tail = tail.next  # Advance the tail to the new node
            current = current.next  # Advance head of the origina list ot the next node
        return dummy.next

    def copyListv2(self, head):
        # Using recursion
        if not head:
            return None
        # Allocate space for new node
        newNode = Node(head.val)

        # copy the next node and set it as the next field for the created node
        newNode.next = self.copyListv2(head.next)

        return newNode


if __name__ == '__main__':

    A = [1, 2, 3, 4, 5]
    examp = creatList()
    head3 = examp.method3(A)
    headc = examp.cloneList(head3)
    dup = examp.copyListv1(head3)
    printList(dup)
