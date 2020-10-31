import collections


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
        if start:
            ret.append(start.val)
            ret = ret + self.preorder(start.left)
            ret = ret + self.preorder(start.right)
        return ret

    def inorder(self, start):
        """Left->Root->Right"""
        ret = []
        if start:
            ret = self.inorder(start.left)
            ret.append(start.val)
            ret = ret + self.inorder(start.right)
        return ret

    def postorder(self, start):
        """Left->Right->Root"""
        ret = []
        if start:
            ret = self.postorder(start.left)
            ret = ret + self.postorder(start.right)
            ret.append(start.val)
        return ret

    def levelorder(self, start):
        levels = collections.defaultdict(list)
        if not start:
            return levels

        def helper(start, level=0):
            if start:
                levels[level].append(start.val)
                helper(start.left, level + 1)
                helper(start.right, level + 1)

        helper(start)
        return levels

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
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))
print(tree.print_tree("levelorder"))

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
