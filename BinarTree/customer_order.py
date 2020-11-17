class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque, defaultdict
def custom_1(root):
    #        1
    #      /    \
    #     2      3
    #   /   \   /  \
    #  4     5 6    7
    # res = [1,2,3,4,7,5,6]
    result = []
    q1 = deque()
    q2 = deque()

    result.append(root.val)
    q1.append(root.left)
    q2.append(root.right)

    while q1 and q2:
        n = len(q1)
        while n > 0:
            cur1 = q1.popleft()
            result.append(cur1.val)
            if cur1.left:
                q1.append(cur1.left)
            if cur1.right:
                q1.append(cur1.right)

            cur2 = q2.popleft()
            result.append(cur2.val)
            if cur2.right:
                q2.append(cur2.right)
            if cur2.left:
                q2.append(cur2.left)
            n -=1
    return result

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    res = custom_1(root)