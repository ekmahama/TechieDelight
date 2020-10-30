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


def splitList(head):
    cnt = 0
    cur = ptr = head
    while cur:
        cnt += 1
        cur = cur.next

    dummy1 = Node()
    dummy2 = Node()
    mid = (cnt//2)+1 if cnt % 2 else cnt//2
    num = 0
    while num < (mid-1):
        num += 1
        ptr = ptr.next
    dummy2.next = ptr.next
    ptr.next = None
    dummy1.next = head
    return dummy1.next, dummy2.next


def splitListV2(head):
    # using fast pointer
    if not head or not head.next:
        first = head
        second = None
        return first, second

    # Advance fast two nodes ahead of slow
    slow = head
    fast = head.next
    while fast:
        fast = fast.next
        if fast:
            fast = fast.next
            slow = slow.next

    # Slow is at the mid point of the list
    first = head
    second = slow.next
    slow.next = None
    return first, second


arr = [1, 2, 4, 5, 6]

head = creatList(arr)
# head1, head2 = splitList(head)
head1, head2 = splitListV2(head)
print()
