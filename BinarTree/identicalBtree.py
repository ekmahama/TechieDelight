import collections


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sameBtree(root1, root2):
    if not root1 and not root2:
        return True

    # Check if both tree root are not empty and equal
    rootEqual = (root1 and root2) and (root1.val == root2.val)
   # Compare left and right branches for both trees
    leftRrightEqual = sameBtree(root1.left, root2.left) and sameBtree(
        root1.right, root2.right)

    # if rootEqual and leftRrightEqual ==> tree is equal

    return rootEqual and leftRrightEqual


def sameBtreeV1(root1, root2):
    """This Depth First Search(DF) Implementation: Uses stack"""
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    stack = collections.deque()
    stack.append((root1, root2))

    while stack:
        x, y = stack.pop()
        if x.val != y.val:
            return False

        if x.left and y.left:
            stack.append((x.left, y.left))
        elif x.left or y.left:
            return False

        if x.right and y.right:
            stack.append((x.right, y.right))
        elif x.right or y.right:
            return False

    return True


def sameBtreeV2(root1, root2):
    """This Breath First Search(DF) Implementation: Uses Queue"""
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    queue = collections.deque()
    queue.append((root1, root2))

    while queue:
        x, y = queue.popleft()
        if x.val != y.val:
            return False

        if x.left and y.left:
            queue.append((x.left, y.left))
        elif x.left or y.left:
            return False

        if x.right and y.right:
            queue.append((x.right, y.right))
        elif x.right or y.right:
            return False

    return True


x = Node(15)
x.left = Node(10)
x.right = Node(20)
x.left.left = Node(81)
x.left.right = Node(12)
x.right.left = Node(16)
x.right.right = Node(25)

# construct second tree
y = Node(15)
y.left = Node(10)
y.right = Node(20)
y.left.left = Node(8)
y.left.right = Node(12)
y.right.left = Node(16)
y.right.right = Node(25)

print(sameBtree(x, y))
print(sameBtreeV1(x, y))
print(sameBtreeV2(x, y))
