from collections import defaultdict, deque


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None


def spiralOrder(root):
    # if level is even,:left->right
    # if level is odd,: right->left
    result = defaultdict(deque)
    if not root:
        return result

    def helper(root, level=0):
        if root:
            if level % 2 == 0:
                result[level].append(root.val)
            else:
                result[level].appendleft(root.val)
            helper(root.left, level+1)
            helper(root.right, level+1)
    helper(root)
    return result


def spiralOrder_v1(root):
    levels = []
    queue = deque()
    queue.append(root)
    flag = 0

    while queue:
        nodeCount = len(queue)
        if flag:
            while nodeCount > 0:
                cur = queue.popleft()
                levels.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                nodeCount -= 1
        else:
            while nodeCount > 0:
                cur = queue.pop()
                levels.append(cur.val)
                if cur.right:
                    queue.appendleft(cur.right)
                if cur.left:
                    queue.appendleft(cur.left)
                nodeCount -= 1
        flag ^= 1
    return levels


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

res2 = spiralOrder_v1(root)
print(res2)
