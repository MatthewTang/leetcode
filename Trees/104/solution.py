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

    # solution 1
    # recursive dfs
    # time: O(n), space: O(h) given h is the height of the tree
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     def countD(root: Optional[TreeNode], d: int):
    #         if not root:
    #             return d
    #
    #         return max(countD(root.left, d + 1), countD(root.right, d + 1))
    #
    #     return countD(root, 0)

    # # solution 2
    # # queue bfs
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     q = [[root, 1]]
    #     m = 0
    #
    #     while q:
    #         node, l = q[0]
    #         if not node:
    #             q.pop(0)
    #         else:
    #             q.append([node.left, l + 1])
    #             q.append([node.right, l + 1])
    #             q.pop(0)
    #             m = l
    #
    #     return m

    # # sol 3
    # # queue bfs w/ deque
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     q = deque()
    #     if root:
    #         q.append(root)
    #
    #     level = 0
    #
    #     while q:
    #         for _ in range(len(q)):
    #             node = q.popleft()
    #             if node.left:
    #                 q.append(node.left)
    #             if node.right:
    #                 q.append(node.right)
    #         level += 1
    #     return level

    # sol 4
    # iterative dfs
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        out = 0
        while stack:
            n, l = stack.pop()

            if n:
                out = max(out, l)
                stack.append([n.left, l + 1])
                stack.append([n.right, l + 1])

        return out


if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(17)

    root2 = TreeNode(1)
    root2.right = TreeNode(2)

    root3 = TreeNode()
    root4 = None

    # printTree(root)

    print(solution.maxDepth(root))
    print(solution.maxDepth(root2))
    print(solution.maxDepth(root3))
    print(solution.maxDepth(root4))
