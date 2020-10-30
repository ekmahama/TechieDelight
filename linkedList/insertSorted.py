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


def creatList(arr):
    if not arr:
        return None
    if len(arr) == 1:
        return Node(arr[0])

    head = Node(arr[0])
    head.next = creatList(arr[1:])
    return head


def insertSortedV1(head, val):
    newNode = Node(val)
    # case 1
    if not head or head.val >= val:
        newNode.next = head
        return newNode
    # case 2

    cur = head
    while cur.next and cur.next.val < val:
        cur = cur.next
    newNode.next = cur.next
    cur.next = newNode
    return head


def insertSortedV2(head, val):
    # Use dummy node
    newNode = Node(val)
    dummy = cur = Node()
    dummy.next = head
    # case 1
    if not head or head.val >= val:
        newNode.next = head
        return newNode

    while cur.next and cur.next.val < val:
        cur = cur.next
    newNode.next = cur.next
    cur.next = newNode
    return dummy.next


arr = [1, 2, 4, 5]

head = creatList(arr)
printList(head)
res = insertSortedV1(head, -1)
printList(res)
res1 = insertSortedV1(res, 2)
printList(res1)
res2 = insertSortedV2(res1, 6)
printList(res2)
