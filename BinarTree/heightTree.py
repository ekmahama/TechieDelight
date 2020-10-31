class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.left))


x = Node(15)
x.left = Node(10)
x.right = Node(20)
x.left.left = Node(81)
x.left.right = Node(12)
x.right.left = Node(16)
x.right.right = Node(25)

ans = height(x)
print(ans)
