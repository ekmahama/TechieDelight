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


def sortedInsert(head, val):
    newNode = Node(val)
    # case 1
    if not head or head.val >= val:
        newNode.next = head
        return newNode

    # Case 2

    cur = head
    while cur.next and cur.next.val < val:
        cur = cur.next
    newNode.next = cur.next
    cur.next = newNode

    return head


def sortLinkedList(head):
    result = None
    cur = head

    while cur:
        next = cur.next
        result = sortedInsert(result, cur)
        cur = next
    return result


# Method 2 Recursion


def helper(head):

    # A helper function just to return the head of the original list
    sortLinkList(head)
    return head


def sortLinkList(head):

    if not head or not head.next:
        return
    if head.val > head.next.val:
        # Sort first two nodes
        tmp = head.val
        head.val = head.next.val
        head.next.val = tmp
    # sort from second node onward
    sortLinkList(head.next)
