from typing import Optional


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

    # solution 2
    # queue bfs
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = [{"n": root, "l": 1}]
        m = 0

        while len(q):
            nxt = q[0]
            node = nxt["n"]
            l = nxt["l"]
            if not node:
                q.pop(0)
            else:
                q.append({"n": node.left, "l": l + 1})
                q.append({"n": node.right, "l": l + 1})
                q.pop(0)
                m = l

        return m


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
    # print(solution.maxDepth(root2))
    # print(solution.maxDepth(root3))
    # print(solution.maxDepth(root4))
