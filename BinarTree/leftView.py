class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

def leftView1(root):
    res = []
    if not root:
        return res
    
    q = deque()
    q.append(root)

    while q:
        i=0
        n = len(q)

        while i< n:
            cur = q.popleft()
            i +=1
            if i == 1:
                res.append(cur.val)

            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
    return res

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    res = leftView1(root)