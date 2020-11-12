import collections
import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorderTrav(start):
    """Left->Root->Right"""
    # Recur on left subtree
    # Process root
    # Recur on right subtree

    result = []
    if not start:
        return result
    result = inorderTrav(start.left)
    result.append(start.val)
    result += inorderTrav(start.right)
    return result


def inorderTrav_v1(start):
    result = []
    stack = collections.deque()
    cur = start

    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            result.append(cur.val)
            cur = cur.right
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
        result = [8, 10, 12, 15, 16, 20, 25]
        self.assertTrue(inorderTrav(self.root), result)

    def test_inorderTrav_v1(self):
        result = [8, 10, 12, 15, 16, 20, 25]
        self.assertTrue(inorderTrav_v1(self.root), result)


if __name__ == "__main__":
    unittest.main()
