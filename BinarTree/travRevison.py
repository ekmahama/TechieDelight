import collections
import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class binaryTree:
    def __init__(self, root=None):
        self.root = None

    def printTree(self, type):
        if type == 'preorder':
            result = self.preorder(self.root)

        if type == 'inorder':
            result = self.inorder(self.root)

        if type == 'postorder':
            result = self.postorder(self.root)

        for val in result:
            print(val, end='->')
        print('None')

    def preorder(self, start):
        # root->left->right
        ret = []
        if not start:
            return ret
        ret.append(start.val)
        ret += self.preorder(start.left)
        ret += self.preorder(start.right)
        return ret

    def inorder(self, start):
        # Left->root->right
        ret = []
        if not start:
            return ret
        ret = self.inorder(start.left)
        ret.append(start.val)
        ret += self.inorder(start.right)
        return ret

    def postorder(self, start):
        # Left->root->right
        ret = []
        if not start:
            return ret
        ret = self.inorder(start.left)
        ret += self.inorder(start.right)
        ret.append(start.val)
        return ret

    def levelOrder(self, start):
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

    def levelorder_v2(self, start):
        levels = []
        level = 1
        if not start:
            return levels

        def helper(root, level):
            if not root:
                return False
            if level == 1:
                levels.append(root.val)

            left = helper(root.left, level-1)
            right = helper(root.right, level-1)

            return left or right
        while helper(start, level):
            level += 1
        return levels

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
