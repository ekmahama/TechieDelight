class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def printList(head):
    ptr = head
    while ptr:
        print(f'{ptr.val}->', end='')
        ptr = ptr.next
    print('None')


class creatList:
    def method1(self):
        e = Node(5)
        d = Node(4, e)
        c = Node(3, d)
        b = Node(2, c)
        a = Node(1, b)
        return a

    def method2(self, A):
        # Method 2 : suitable for large array, space: O(n)
        node = ['None']*len(A)

        for i in range(len(A)):
            node[i] = Node(A[i], None)
            if i > 0:
                node[i-1].next = node[i]
        head = node[0]
        return head

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


if __name__ == '__main__':
    # # Method1
    # e = Node(5)
    # d = Node(4, e)
    # c = Node(3, d)
    # b = Node(2, c)
    # a = Node(1, b)

    # Method 2 : suitable for large array
    A = [1, 2, 3, 4, 5]
    # node = ['None']*len(A)

    # for i in range(len(A)):
    #     node[i] = Node(A[i], None)
    #     if i > 0:
    #         node[i-1].next = node[i]
    # head = node[0]
    # printList(head)

    # Method 3 uses less space
    # prev = head = None
    # for val in A:
    #     node = Node(val, None)
    #     if prev == None:
    #         head = node
    #     else:
    #         prev.next = node
    #     prev = node
    examp = creatList()
    head1 = examp.method1()
    printList(head1)

    head2 = examp.method2(A)
    printList(head2)

    head3 = examp.method3(A)
    printList(head2)
