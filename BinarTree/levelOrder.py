import collections
import unittest


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(start):
    """Root->left->Right"""
    ret = []
    queue = collections.deque()
    queue.append(start)

    while queue:
        cur = queue.pop()
        ret.append(cur.val)

        if cur.left:
            queue.appendleft(cur.left)
        if cur.right:
            queue.appendleft(cur.right)
    return ret


def levelOrder_v1(start):
    levels = collections.defaultdict(list)
    if not start:
        return levels

    def helper(root, level=0):
        if root:
            levels[level].append(root.val)
            helper(root.left, level+1)
            helper(root.right, level + 1)

    helper(start)
    return levels


def height(start):
    if not start:
        return 0
    return 1 + max(height(start.left), height(start.right))


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

    def test_levelOrder(self):
        self.result = [15, 10, 20, 8, 12, 16, 25]
        self.assertTrue(levelOrder(self.root), self.result)

    def test_levelOrder_v1(self):
        pass


if __name__ == '__main__':
    unittest.main()
    # root = Node(15)
    # root.left = Node(10)
    # root.right = Node(20)
    # root.left.left = Node(8)
    # root.left.right = Node(12)
    # root.right.left = Node(16)
    # root.right.right = Node(25)

    # res = levelOrder(root)
    # res1 = levelOrder_v1(root)
    # res2 = height(root)
