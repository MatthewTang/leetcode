from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"{self.val}"


def printTree(root: TreeNode, level=0):
    if root is None:
        return
    printTree(root.right, level + 1)
    print("\t" * level, root.val)
    printTree(root.left, level + 1)


class Solution:
    # recursive
    # time: O(n), space: O(n)
    def _kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def t(node: Optional[TreeNode], q):

            if not node:
                return

            t(node.left, q)
            q.append(node.val)
            if len(q) == k:
                return node.val
            t(node.right, q)

        q = []
        t(root, q)
        return q[k - 1]

    # iterative
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        stack = [curr]
        out = []
        # n = 0

        while curr and stack:
            while curr.left:
                curr = curr.left
                stack.append(curr)
            t = stack.pop()
            # n += 1
            # if n == k:
            #     return curr.val

            out.append(t.val)
            if t.right:
                stack.append(t.right)
                curr = t.right

        return out[k - 1]


if __name__ == "__main__":
    solution = Solution()

    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)

    root2 = TreeNode(5)
    root2.left = TreeNode(3)
    root2.right = TreeNode(6)
    root2.left.left = TreeNode(2)
    root2.left.right = TreeNode(4)
    root2.left.left.left = TreeNode(1)

    test1 = {"root": root, "k": 1}
    test2 = {"root": root2, "k": 3}

    tests = [test1, test2]

    for test in tests:
        print("---------------------------------------")
        printTree(test["root"])
        print(solution.kthSmallest(test["root"], test["k"]))
