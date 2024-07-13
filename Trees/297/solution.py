from typing import Deque, Optional, List
from collections import deque
import unittest
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        # Check if 'other' is an instance of TreeNode
        if not isinstance(other, TreeNode):
            return False
        # Compare the current node's value
        if self.val != other.val:
            return False
        # Recursively compare the left subtree
        if self.left or other.left:
            if not self.left or not other.left:
                return False
            if not self.left == other.left:
                return False
        # Recursively compare the right subtree
        if self.right or other.right:
            if not self.right or not other.right:
                return False
            if not self.right == other.right:
                return False
        # If all checks pass, the trees are equal
        return True

    def __repr__(self) -> str:
        return f"{self.val}"


def printTree(root: TreeNode, level=0):
    if root is None:
        return
    printTree(root.right, level + 1)
    print("\t" * level, root.val)
    printTree(root.left, level + 1)


class TestSolution(unittest.TestCase):
    def test1(self):
        root = None
        
        printTree(root)

        ser = Codec()
        deser = Codec()
        serialized = ser.serialize(root)
        print(serialized)
        deserialized = deser.deserialize(serialized)
        printTree(deserialized)

        ans = deser.deserialize(ser.serialize(root))
        self.assertEqual(root, ans)

    def test2(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)
        
        printTree(root)

        ser = Codec()
        deser = Codec()
        serialized = ser.serialize(root)
        print(serialized)
        deserialized = deser.deserialize(serialized)
        printTree(deserialized)

        ans = deser.deserialize(ser.serialize(root))
        self.assertEqual(root, ans)


class Codec:
    def serialize(self, root: TreeNode):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        q = deque()
        if root:
            q.append(root)

        while q:
            curr = q.popleft()
            if not curr:
                res.append(None)
                continue

            res.append(curr.val)
            if curr.left:
                q.append(curr.left)
            else:
                q.append(None)
            if curr.right:
                q.append(curr.right)
            else:
                q.append(None)

        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        q = deque(data)

        if not q:
            return None

        root = TreeNode(q.popleft())
        node_queue: Deque[TreeNode] = deque([root])

        while node_queue:
            curr = node_queue.popleft()
            if not curr.val:
                continue

            if q:
                v = q.popleft()
                if v:
                    n = TreeNode(v)
                    node_queue.append(n)
                    curr.left = n
            if q:
                v = q.popleft()
                if v:
                    n = TreeNode(v)
                    node_queue.append(n)
                    curr.right = n

        return root


if __name__ == "__main__":
    unittest.main()
