import collections
import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def postorder(start):
    """Left->Right->Root"""
    # Recursively traverse Left
    # Recursively traverse right
    # Process root
    result = []

    if not start:
        return result

    result = postorder(start.left)
    result += postorder(start.right)
    result.append(start.val)
    return result


def postorder_v1(start):
    result = []
    if not start:
        return result

    stack = collections.deque()
    stack.append(start)

    while stack:
        cur = stack.pop()
        result.append(cur.val)

        if cur.left:
            stack.append(cur.left)

        if cur.right:
            stack.append(cur.right)

    return result[::-1]


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
        result = [8, 12, 10, 16, 25, 20, 15]
        self.assertTrue(postorder(self.root), result)

    def test_inorderTrav_v1(self):
        result = [8, 12, 10, 16, 25, 20, 15]
        self.assertTrue(postorder_v1(self.root), result)


if __name__ == "__main__":
    unittest.main()
