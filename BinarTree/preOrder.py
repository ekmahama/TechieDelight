import collections
import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def preorder(start):
    """Root->Left->Right"""
    # Process root
    # Recur on left subtree
    # Recur on right subtree
    result = []
    if not start:
        return result
    result.append(start.val)
    result += preorder(start.left)
    result += preorder(start.right)
    return result


def preorder_v1(start):
    """Left->Right->Root"""
    # Recur on left subtree
    # Recur on right subtree
    # Process root
    result = []
    if not start:
        return result
    stack = collections.deque()
    stack.append(start)

    while stack:
        cur = stack.pop()
        result.append(cur.val)
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)

    return result


class Test(unittest.TestCase):
    def setUp(self):
        self.root = Node(15)
        self.root.left = Node(10)
        self.root.right = Node(20)
        self.root.left.left = Node(8)
        self.root.left.right = Node(12)
        self.root.right.left = Node(16)
        self.root.right.right = Node(25)

    def tearDown(self):
        pass

    def test_inorderTrav(self):
        result = [15, 10, 8, 12, 20, 16, 25]
        self.assertTrue(preorder(self.root), result)

    def test_inorderTrav_v1(self):
        result = [15, 10, 8, 12, 20, 16, 25]
        self.assertTrue(preorder_v1(self.root), result)


if __name__ == "__main__":
    unittest.main()
