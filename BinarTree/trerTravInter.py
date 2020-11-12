import collections
import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traveral_type):
        if traveral_type == 'inorder':
            result = self.inorder(self.root)
        elif traveral_type == 'preorder':
            result = self.preorder(self.root)
        elif traveral_type == 'postorder':
            result = self.postorder(self.root)

        elif traveral_type == 'levelorder':
            result = self.levelorder(self.root)
            result = result.values()

        for val in result:
            print(val, end=' ')

    def preorder(self, start):
        """ root->left->right"""
        ret = []
        stack = collections.deque()
        cur = start
        stack.append(cur)

        while stack:
            cur = stack.pop()
            ret.append(cur.val)

            if cur.right:
                stack.append(cur.right)

            if cur.left:
                stack.append(cur.left)
        return ret

    def inorder(self, start):
        """Left->Root->Right"""
        ret = []
        stack = collections.deque()
        cur = start
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                ret.append(cur.val)
                cur = cur.right
        return ret

    def postorder(self, start):
        """Left->Right->Root"""
        ret = []
        cur = start
        stack = collections.deque()
        stack.append(cur)

        while stack:
            cur = stack.pop()
            ret.append(cur.val)

            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)

        return ret[::-1]

    def levelorder_v3(self, start):
        ret = []
        queue = collections.deque()
        queue.append(start)
        while queue:
            cur = queue.popleft()
            ret.append(cur.val)

            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return ret

    def revlevelorder(self, start):
        pass


        # Create a simple tree
        #        1
        #      /    \
        #     2      3
        #   /   \   /  \
        #  4     5  6   7
        #
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.print_tree("preorder"))
# print(tree.print_tree("inorder"))
# print(tree.print_tree("postorder"))
# print(tree.print_tree("levelorder"))

# Algorithm for Traversing a tree
# 1. Depth Search First
#  - post-order traversal
#    left->right->root
#  - in-order traversal
#    left->root->right
#  - pre-order traversal
#    root->left->right
#
# 2. Breath Search First
# root->left->right

# Pre-order Traversal
# 1 check if root is empty/null
# 2 Display the data part of the root (or current node)
# 3 Traverse the left subtree by recursively calling the pre-order fxn
# 4 Traverse the righ subtree by //////////////////
#
#


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
