from typing import Optional
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
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def traverse(tree, p, q, res):
            if not tree:
                return

            if traverse(tree.left, p, q, res) and traverse(tree.right, p, q, res):
                res.append(tree)
                return

            return tree.val == p.val or tree.val == q.val

        res = []
        traverse(root, p, q, res)

        print(res)

        return 1


if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)

    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)

    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)

    p = root.left
    # q = root.right
    q = root.left.right

    printTree(root)
    print(solution.lowestCommonAncestor(root, p, q))
